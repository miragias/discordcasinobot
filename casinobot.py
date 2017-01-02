import discord
import random
import collections
from random import randint


client = discord.Client()
mothercards = []
playercards = []
Card = collections.namedtuple('Card', ['rank','suit'])

#pull_check
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
        #initialize deck
        deck=Deck()
        print(len(deck))

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
    
        #show the cards of each player
        async def printcards(whotoprint):
            if(whotoprint == "mother"):
                await client.send_message(message.channel , "Mother has:")
                for card in mothercards:
                    await client.send_message(message.channel , "{} {}".format(card.rank, card.suit))
            else:
                await client.send_message(message.channel , "Player has:")
                for card in playercards:
                    await client.send_message(message.channel , "{} {}".format(card.rank, card.suit))
            return

        #initial messages
        await client.send_message(message.channel , "Let's play blackjack!")
        await client.send_message(message.channel , 'I have \n' +choose_random_card("formother"))
        await client.send_message(message.channel , 'You have \n' +choose_random_card("forplayer") + ' and ' +choose_random_card("forplayer"))
        await client.send_message(message.channel , "Type hit or stand" )


        while True:
            choice = await client.wait_for_message(timeout = 30.0, author = message.author , check = choice_check)

            if choice is None:
                await client.send_message(message.channel , 'You gave no answer game game will now stop')
                return
            if (choice.content  == 'hit'):
                await client.send_message(message.channel , 'You grab '  +choose_random_card("forplayer"))
            if (choice.content  == 'stand'):
                await client.send_message(message.channel , 'You stand')
                await printcards("mother")
                await printcards("player_")
                break

            


"""
DISCORD BOT SETTINGS
"""
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print ('Bot working properly')
    print('------')

client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')
