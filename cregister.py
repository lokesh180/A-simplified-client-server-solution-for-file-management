"""
This module has the client registration function, which
is implemented with asyncio.
"""

async def registration(reader, writer):
    """
    This function provides the user to register in the
    application.
    The parameters included are:
    name - name of user
    Userid - Username of user
    Password - Password of user
    """
    for _ in range(3):
        response = await reader.read(100)
        msg = response.decode().strip()
        something = input(msg)
        writer.write(something.encode())
    response = await reader.read(100)
    finalmsg = response.decode().strip()
    print(finalmsg)
    print("----Pls Login now by clicking login after running client----")
