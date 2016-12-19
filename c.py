import discord
import random
import collections


client = discord.Client()
cards = [ 'A', '1', '2', '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K']
mothercards = []
player1_cards = []

class Deck:
    ranks=[string(n) for n in range(2,12)] + list('JQKA')
    suits= 'spathia karo kupes mpastunia'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

#a new comment
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

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
        deck=Deck();
        def choice_check(m):
            if (m == 'hit' or  m == 'stand'):
                return m;
            return m;


        await client.send_message(message.channel , "Let's play blackjack!")
        await client.send_message(message.channel , 'I have \n' +choose_random_card())

        await client.send_message(message.channel , 'Exeis \n' +choose_random_card() + ' kai ' +choose_random_card())
        await client.send_message(message.channel , 'Γράψε <<hit>> για να χτυπήσεις ή <<stand>> για να μείνεις')

        choice = await client.wait_for_message(timeout = 10.0, author = message.author , check = choice_check)


        if choice is None:
            await client.send_message(message.channel , 'Κάτι έγραψες λάθος ξαναάρχισε νέο παιχνίδι')
        if (choice.content  == 'hit'):
            await client.send_message(message.channel , 'Pare mia akomi karta')
        if (choice.content  == 'stand'):
            await client.send_message(message.channel , 'You stand')

            
            








@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print ('Hello master everything seems to be working ok')
    print('------')

client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')
