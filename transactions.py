import asyncio
import sqlite3
from client import client


# Output User Money
@asyncio.coroutine
async def TellUserMoney(message):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    if CheckIfUserInDB(name, c):
        c.execute('SELECT NAME,MONEY FROM usermoney WHERE NAME=?', (name, ))
        row1 = c.fetchone()
        await client.send_message(message.channel, 'User {} has {} marks'.format(row1[0], row1[1]))
    else:
        await client.send_message(message.channel, 'You do not exist in the database add yourself with the $addme command')
    conn.close()
    return


def CheckIfUserInDB(username, c):
    c.execute('SELECT * FROM usermoney WHERE NAME=?', (username, ))
    fetch = c.fetchall()
    if len(fetch) < 1:
        return False
    else:
        return True


@asyncio.coroutine
async def AddUserToDB(message):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    if CheckIfUserInDB(name, c):
        await client.send_message(message.channel, 'You already exist in the database')
    else:
        await client.send_message(message.channel, 'Welcome to the Greek Gaming Server hope you enjoy your stay.\nWe have added 50$ to your account for use. Don\'t forget to read the rules and announcements')
        c.execute('INSERT INTO usermoney VALUES(?, 50)', (name, ))
    conn.commit()
    conn.close()
    return


def CheckIfUserHasEnoughMoney(message, money):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    c.execute("SELECT MONEY FROM usermoney WHERE NAME=?", (name, ))
    row = c.fetchone()
    if money <= row[0]:
        return True
    return False


def ChangeUserMoney(message, amount):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    c.execute("UPDATE usermoney SET MONEY=MONEY+? WHERE NAME=?", (amount, name, ))
    conn.commit()
    conn.close()
    return

# TODO : Add or Remove X Value From User
