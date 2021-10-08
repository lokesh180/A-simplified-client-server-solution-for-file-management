"""
This is the SERVER program with asyncio.
---------------------------------------
This program is the main heart of the application.Server code is designed
to run forever and the server will stop when we give a command of CTRL+C.
This pragram has the main program, which initiate the application.
Here we have the functions for choosing the login and register option.
After selceting the option user has the oppurtinity to acess his directories.
"""
import asyncio
import signal
import sregister
import slogin

# signal to stop server when clicked CTRL+C
signal.signal(signal.SIGINT, signal.SIG_DFL)

# async function of server code to choose the option Registration or Login
async def choose_option(reader, writer):
    """
    This function will provide user an opportunity to choose the
    Registration or Login function, which the code is divided in few modules.
    Based on the command given by the user the program will call the function
    and run the function.
    >>> choice = 1
    """
    welcomemsg = """Hello User you have two choice\nChoose Registration or Login
    1. Registration
    2. Login (If you hav Registered)
    Enter your choice :"""
    writer.write(welcomemsg.encode())
    response = await reader.read(150)
    choice = response.decode().strip()
    print(f"User choosed the {choice} option")
    if choice == '1':
        # calling the registration function
        await sregister.registration(reader, writer)
    else:
        # calling the login function
        await slogin.login(reader, writer)

async def main():
    """
    This is used for initiation of the server and makes the server
    running forever untill press CTRL+C.
    The client with the same ipadress and port number will
    has acess to connect the server.
    """
    server = await asyncio.start_server(
        choose_option, '127.0.0.1', 8088)

    # showing address
    addr = server.sockets[0].getsockname()
    print(f'The SERVER is Started and serving on {addr}')
    print("Waiting for the Clients....:-)")

    # makes server to run forever
    async with server:
        await server.serve_forever()

asyncio.run(main())
