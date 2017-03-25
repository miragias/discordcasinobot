import discord
import asyncio
from client import client
from casinogames import BlackJack,GuessGame


"""
DISCORD BOT STARTUP SCREEN
"""


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot initialized properly')
    print('------')

#Start bot function depending on user command
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$bj'):
		await BlackJack(message)

	if message.content.startswith('$guess'):
		await GuessGame(message)



client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')

