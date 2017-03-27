from client import client

roleList = ['ow', 'lol', 'csgo']

# TODO: CHECK WHY THEY DO NOT ACCEPT 2 PARWAMETERS


@client.event
async def addRole(message):
    # Get Available Roles From Server
    availableServerRoles = message.server.roles
    rolemessage = str(message.content)
    roles = rolemessage.split()
    roles.remove('$addrole')
    for role in availableServerRoles:
        if role.name in roleList and role.name in roles:
            print(role.name)
            await client.add_roles(message.author, role)
    return


@client.event
async def removeRole(message):
    # Get Available Roles From Server
    rolemessage = str(message.content)
    roles = rolemessage.split()
    roles.remove('$removerole')
    for role in message.author.roles:
        if role.name in roles:
            await client.remove_roles(message.author, role)
    return
