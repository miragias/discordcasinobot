import discord

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    #Check if user input number
    def check_msg(m):
        return m.content.isdigit()
    #Check if user input name
    def check_msg_user(m):
        return m


    #Admin function to add money to a user
    if message.content.startswith('$addmoney'):
        admin_check = False #Check if user putting the command is admin
        user_check = False #Check if user exists to add money to him
        amount_check = False #Check if amount is a number

        command = await client.wait_for_message(timeout=30.0, author=message.author)

        #Check if user who invokes the command is admin
        for role in message.author.roles: 
            if str(role) == "admin":
                admin_check = True
        if not admin_check:
                await client.send_message(message.channel , 'You are not admin')
                return
        command_txt = command.content.split()
        for word in command_txt:
            print(word)
    
    
        

