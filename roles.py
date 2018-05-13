import asyncio
roleList = ['ow', 'lol', 'csgo']

@asyncio.coroutine
async def add_role(client , message):
    # Get Available Roles From Server
    print("addrole happened")
    availableServerRoles = message.server.roles
    rolemessage = str(message.content)
    roles = rolemessage.split()
    roles.remove('$addrole')
    for role in availableServerRoles:
        if role.name in roleList and role.name in roles:
            await client.add_roles(message.author, role)
    return

@asyncio.coroutine
async def remove_role(client , message):
    # Get Available Roles From Server
    rolemessage = str(message.content)
    roles = rolemessage.split()
    roles.remove('$removerole')
    for role in message.author.roles:
        if role.name in roles:
            await client.remove_roles(message.author, role)
    return
