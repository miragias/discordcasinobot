import discord
import random
import collections
from random import randint


client = discord.Client()
mothercards = []
playercards = []
Card = collections.namedtuple('Card', ['rank','suit'])

#Deck class
class Deck:
    ranks=[str(n) for n in range(2,11)] + list('JQKA')
    suits= '♣️ ♦️ ♥️ ♠️'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                for rank in self.ranks]

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

"""
BLACKJACK GAME

"""
    if message.content.startswith('$game'):
        deck=Deck()
        print("HI")
        print(len(deck))
        def choice_check(m):
            if (m == 'hit' or  m == 'stand'):
                return m;
            return m;

        def choose_random_card():
            randomnum = randint(1,51)
            string_to_return =  "{} {}".format(deck[randomnum].rank , deck[randomnum].suit)
            del deck[randomnum]
            print(len(deck))
            return string_to_return
    


        await client.send_message(message.channel , "Let's play blackjack!")
        await client.send_message(message.channel , 'I have \n' +choose_random_card())

        await client.send_message(message.channel , 'You have \n' +choose_random_card() + ' and ' +choose_random_card())
        await client.send_message(message.channel , "Type hit or stand" )

        choice = await client.wait_for_message(timeout = 30.0, author = message.author , check = choice_check)


        if choice is None:
            await client.send_message(message.channel , 'You typed something wrong')
            return
        if (choice.content  == 'hit'):
            await client.send_message(message.channel , 'Take another card')
        if (choice.content  == 'stand'):
            await client.send_message(message.channel , 'You stand')

            
            




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
