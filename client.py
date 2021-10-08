"""
This module will create the connection of client and connected to
server by using IPAdress and port number.And asks user to have
registration and login.
"""
import asyncio
import cregister
import clogin

async def client():
    """
    This async function has implementation for connecting the client
    to server and and sends the input to server and receives the data
    from server and shows in client.
    """
    reader, writer = await asyncio.open_connection('127.0.0.1', 8088)
    response = await reader.read(150)
    msg = response.decode().strip()
    choose = input(msg)
    writer.write(choose.encode())
    if choose == '1':
        await cregister.registration(reader, writer)

    if choose != '1':
        await clogin.login(reader, writer)

asyncio.run(client())
