from casinogames import BlackJack, GuessGame
<<<<<<< HEAD
#from transactions import TellUserMoney
from multiprocessing import Process
import discord
import asyncio

client = None

#TODO(JohnMir): Clean this up
def run_bot():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('Bot initialized properly')
        print('------')


    @client.event
    async def on_message(message):
        if message.author == client.user:
                return
        if message.content.startswith('$bj'):
                await BlackJack(client , message)
        if message.content.startswith('$guess'):
                await GuessGame(client , message)
        if message.content.startswith('$moneyleft'):
                await TellUserMoney(message)

    async def get_server_data():
        while True:
            await asyncio.sleep(10)
            #Get info here
            print('TESTING DELAY')

    loop = client.loop
    loop.create_task(get_server_data())
    client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')

if __name__ == '__main__':
    p = Process(target=run_bot, args=())
    p.start()
    p.join()


=======
from transactions import TellUserMoney, AddUserToDB
from roles import addRole, removeRole


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

    if message.content.startswith('$bj'):
            await BlackJack(message)

    if message.content.startswith('$guess'):
            await GuessGame(message)

    if message.content.startswith('$money'):
            await TellUserMoney(message)

    if message.content.startswith('$register'):
            await AddUserToDB(message)

    if message.content.startswith('$addrole'):
            await addRole(message)

    if message.content.startswith('$removerole'):
            await removeRole(message)


client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')
>>>>>>> b9e2afbcd493016bcdae21618b7927fbd2e57281
