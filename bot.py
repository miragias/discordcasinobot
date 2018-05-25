from casinogames import blackjack, guess_game
from transactions import tell_user_money, add_user_to_db
from roles import add_role,remove_role
from serverinfoscrapper import get_server_data
from webserver import do_something

from multiprocessing import Process , Queue
import discord
import asyncio

client = None

#TODO(JohnMir): Clean this up
def run_bot(q):
        client = discord.Client()

        @client.event
        async def on_ready():
                #Check Correct Initialization
                print('Logged in as')
                print(client.user.name)
                print(client.user.id)
                print('Bot initialized properly')
                print('------')
                #Add bot tasks here after initialization is complete
                loop = client.loop
                #q.put("TEST")
                loop.create_task(get_server_data(client , q))

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


        client.run('MTg3NjYwNDA4MDIxMDU3NTM3.CuKrag.9X9myjLSYD2J9IX6ANWal4ZqPNM')


if __name__ == '__main__':
        q = Queue()
        p = Process(target=run_bot, args=(q , ))
        p.start()
        #print(q.get())
        d = Process(target=do_something, args=(q , ))
        d.start()
        p.join()


