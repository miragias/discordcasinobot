import asyncio
import sqlite3
from client import client


@asyncio.coroutine
async def TellUserMoney(message):
    # Test Output for money
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    print(name)
    c.execute('SELECT NAME,MONEY FROM usermoney WHERE NAME=?', (name, ))
    row1 = c.fetchone()
    print(row1)
    await client.send_message(message.channel, 'User {} has {} marks'.format(row1[0], row1[1]))
    conn.close()
    return

# TODO : Check if user is in database
# TODO : Add or Remove X Value From User
# TODO : Add user to database IF he wants to and is not already in
