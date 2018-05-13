from casinogames import blackjack, guess_game
from transactions import tell_user_money, add_user_to_db
from roles import add_role,remove_role

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
                await blackjack(client , message)
        if message.content.startswith('$guess'):
                await guess_game(client , message)
        if message.content.startswith('$moneyleft'):
                await tell_user_money(client , message)
        if message.content.startswith('$register'):
            await add_user_to_db(client , message)
        if message.content.startswith('$addrole'):
                await add_role(client , message)
        if message.content.startswith('$removerole'):
                await remove_role(client , message)

    async def get_server_data():
        while True:
            await asyncio.sleep(10)
            #Get info here
            print('TESTING DELAY')

    loop = client.loop
    loop.create_task(get_server_data())
    client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')

#TODO(JohnMir): Flask subproccess here
def do_something():
        while True:
                pass

if __name__ == '__main__':
    p = Process(target=run_bot, args=())
    p.start()
    d = Process(target=do_something, args=())
    d.start()
    p.join()


