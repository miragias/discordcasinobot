import asyncio
import sqlite3

# Output User Money
@asyncio.coroutine
async def tell_user_money(client , message):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    if check_if_user_in_db(name, c):
        c.execute('SELECT NAME,MONEY FROM usermoney WHERE NAME=?', (name, ))
        row1 = c.fetchone()
        await client.send_message(message.channel, 'User {} has {} marks'.format(row1[0], row1[1]))
    else:
        await client.send_message(message.channel, 'You do not exist in the database add yourself with the $addme command')
    conn.close()
    return


def check_if_user_in_db(username, c):
    c.execute('SELECT * FROM usermoney WHERE NAME=?', (username, ))
    fetch = c.fetchall()
    if len(fetch) < 1:
        return False
    else:
        return True


@asyncio.coroutine
async def add_user_to_db(client , message):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    if check_if_user_in_db(name, c):
        await client.send_message(message.channel, 'You already exist in the database')
    else:
        await client.send_message(message.channel, 'Welcome to the Greek Gaming Server hope you enjoy your stay.\nWe have added 50$ to your account for use. Don\'t forget to read the rules and announcements')
        c.execute('INSERT INTO usermoney VALUES(?, 50)', (name, ))
    conn.commit()
    conn.close()
    return


def check_if_user_has_enough_money(message, money):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    c.execute("SELECT MONEY FROM usermoney WHERE NAME=?", (name, ))
    row = c.fetchone()
    if money <= row[0]:
        return True
    return False


def change_user_money(message, amount):
    conn = sqlite3.connect('money.db')
    c = conn.cursor()
    name = str(message.author.display_name)
    c.execute("UPDATE usermoney SET MONEY=MONEY+? WHERE NAME=?", (amount, name, ))
    conn.commit()
    conn.close()
    return

# TODO : Add or Remove X Value From User
