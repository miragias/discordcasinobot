import asyncio

#TODO(JohnMir): Make this welp be input from console when app starts as input parameters
#TODO(JohnMir): Take into account users joining or leaving the server while bot is running
async def get_server_data(client , queue):
    members = None
    queue.put("HEY")
    for server in client.servers:
        if str(server) == "welp":
            for member in server.members:
                print(member)
            members = server.members
    while True:
        await asyncio.sleep(6)
        print('TESTING DELAY')

