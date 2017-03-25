import asyncio
import sqlite3
from client import client


@asyncio.coroutine
async def TellUserMoney(message):
    # Test Output for money
    await client.send_message(message.channel, 'Trying to add money')
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    c.execute('SELECT NAME,MONEY FROM usermoney')
    row1 = c.fetchone()
    await client.send_message(message.channel, 'connected successfuly user {} has {} marks'.format(row1[0], row1[1]))
    conn.close()
    return
