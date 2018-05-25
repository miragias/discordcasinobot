from casinogames import blackjack, guess_game
from transactions import tell_user_money, add_user_to_db
from roles import add_role,remove_role
from serverinfoscrapper import get_server_data
from webserver import do_something

from multiprocessing import Process , Pipe
import discord
import asyncio

client = None

#TODO(JohnMir): Make config file for options:
"""
1)Server
2)Wait time between intervals to send data
"""
#TODO(JohnMir): Clean this up
def run_bot(pipe):
        output_p , input_p = pipe
        output_p.close()
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
                loop.create_task(get_server_data(client , input_p))

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
        output_p , input_p = Pipe()
        p = Process(target=run_bot, args=((output_p , input_p),))
        p.start()
        d = Process(target=do_something, args=((output_p , input_p),))
        d.start()
        p.join()


