import discord
import random
import collections
from random import randint


client = discord.Client()
Card = collections.namedtuple('Card', ['rank','suit'])

#Deck class
class Deck:
    ranks=[str(n) for n in range(2,11)] + list('JQKA')
    suits= '♣️ ♦️ ♥️ ♠️'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                for rank in self.ranks]*6

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

    def __delitem__(self,position):
        del self._cards[position]

#Bot 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #simple guess game
    if message.content.startswith('$guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')
        
        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

    if message.content.startswith('$game'):
        #initialize deck and clear lists
        deck=Deck()
        mothercards = []
        playercards = []


        #check choice hit or stand
        def choice_check(m):
            if (m == 'hit' or  m == 'stand'):
                return m;
            return m;

        #choose random card for either mother or player
        def choose_random_card(person_choosing):
            randomnum = randint(1,51)
            string_to_return =  "{} {}".format(deck[randomnum].rank , deck[randomnum].suit)
            if(person_choosing == "formother"):
                mothercards.append(deck[randomnum])
            else:
                playercards.append(deck[randomnum])
            del deck[randomnum]
            return string_to_return
    
        def sum_of_player_cards(player):
            sum = 0
            rank = 0
            A_exists = False
            number_of_A_inHand = 0
            if(player == "mother"):
                for card in mothercards:
                    try:
                        rank = int(card.rank)
                        sum += rank 
                    except:
                         if card.rank == "A":
                            A_exists = True
                            number_of_A_inHand +=1
                            sum +=11
                         else:
                            sum +=10
            else:
                for card in playercards:
                    try:
                        rank = int(card.rank)
                        sum += rank
                    except:
                        if card.rank == "A":
                            A_exists = True
                            number_of_A_inHand +=1
                            sum +=11
                        else:
                            sum +=10
            #Check the sum in case of Alpha change its value
            while (number_of_A_inHand >0):
                number_of_A_inHand -=1
                if (sum > 21 and A_exists):
                    sum -=10
            return sum





        #show the cards of each player
        async def printcards(whotoprint):
            if(whotoprint == "mother"):
                await client.send_message(message.channel , "Dealer has: ")
                for card in mothercards:
                    await client.send_message(message.channel , "{} {}".format(card.rank, card.suit))
            else:
                await client.send_message(message.channel , "Player has: ")
                for card in playercards:
                    await client.send_message(message.channel , "{} {}".format(card.rank, card.suit))
            return

        #initial messages
        #hidden card for mother 
        choose_random_card("formother")
        await client.send_message(message.channel , "Let's play blackjack!")
        await client.send_message(message.channel , 'I have \n' +choose_random_card("formother"))
        await client.send_message(message.channel , 'You have \n' +choose_random_card("forplayer") + ' and ' +choose_random_card("forplayer"))
        await client.send_message(message.channel , "Type hit or stand" )


                    
        #loop to hit or stand
        while True:
            if sum_of_player_cards("player")>21:
                await client.send_message(message.channel , "Busted! I win")
                return

            choice = await client.wait_for_message(timeout = 30.0, author = message.author , check = choice_check)

            if choice is None:
                await client.send_message(message.channel , 'You gave no answer game game will now stop')
                return
            if (choice.content  == 'hit'):
                await client.send_message(message.channel , 'You grab: '  +choose_random_card("forplayer"))
                await printcards("player_")
            if (choice.content  == 'stand'):
                await client.send_message(message.channel , 'You stand with: ' +str(sum_of_player_cards("player")))
                await printcards("mother")
                break

        await client.send_message(message.channel , "Dealer's turn")
        #mother logic
        while sum_of_player_cards("mother")<17:
            await client.send_message(message.channel , 'Dealer Grabs: '  +choose_random_card("formother"))
            await printcards("mother")

        if sum_of_player_cards("mother") >=21:
            await client.send_message(message.channel , 'Dealer Busted! You Win!')
            return
        else:
            await client.send_message(message.channel , 'Dealer stands with: ' + str(sum_of_player_cards("mother")))

        if sum_of_player_cards("player") > sum_of_player_cards("mother"):
            await client.send_message(message.channel , 'You Win!!!')
        else:
            await client.send_message(message.channel , 'I Win!!!')
        return
