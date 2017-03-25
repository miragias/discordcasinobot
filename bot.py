from client import client
from casinogames import BlackJack, GuessGame
from transactions import TellUserMoney


# Bot Startup Text
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot initialized properly')
    print('------')


# Start bot function depending on user command
@client.event
async def on_message(message):
    if message.author == client.user:
            return

    print(message.author.display_name)
    if message.content.startswith('$bj'):
            await BlackJack(message)

    if message.content.startswith('$guess'):
            await GuessGame(message)

    if message.content.startswith('$moneyleft'):
            await TellUserMoney(message)

client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')
