"""
This module have the functionality to request the commands
from the client to the server and has the requested commands
and also stores the commands of the client given and shows to client.
"""
import sys

async def login(reader, writer):
    """
    This function is client login function for the login
    purpose of the client and makes the client in the intractive
    way and also provides the a large facilites to the user to
    intract with his own storage and has access to edit i.e create
    , read, write file in user storage.
    """
    scommands = [
        "", "createfolder", "writefile", "readfile", "list", "changepath", "comds"
        ]
    commands = []
    response = await reader.read(100)
    msg = response.decode().strip()
    usid = input(msg)
    writer.write(usid.encode())
    response = await reader.read(100)
    msg = response.decode().strip()
    passw = input(msg)
    writer.write(passw.encode())
    response = await reader.read(10000)
    msg = response.decode().strip()
    print(msg)
    while True:
        response = await reader.read(10000)
        msg = response.decode().strip()
        print(msg)
        if msg in ["You have logged in already\nAccess Denied","Invalid Username or Password"]:
            sys.exit()
        cmdch = input("Enter your choice : ")
        commands.append(int(cmdch))
        writer.write(cmdch.encode())
        if cmdch == '1':
            data = await reader.read(100)
            msg = data.decode().strip()
            fname = input(msg)
            writer.write(fname.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            print(msg)
        elif cmdch == "2":
            data = await reader.read(100)
            msg = data.decode().strip()
            folname = input(msg)
            writer.write(folname.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            filename = input(msg)
            writer.write(filename.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            idata = input(msg)
            writer.write(idata.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            print(msg)
        elif cmdch == "3":
            data = await reader.read(100)
            msg = data.decode().strip()
            folname = input(msg)
            writer.write(folname.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            filename = input(msg)
            writer.write(filename.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            print(msg)
        elif cmdch == "4":
            data = await reader.read(100)
            msg = data.decode().strip()
            print(msg)
            writer.write("heading".encode())
            data = await reader.read(100)
            sname = data.decode().strip()
            name = list(sname.split(" "))
            # print(name)
            writer.write("file names".encode())
            data = await reader.read(100)
            ssize = data.decode().strip()
            size = list(ssize.split(" "))
            # print(size)
            writer.write("file sizes".encode())
            data = await reader.read(400)
            scr = data.decode().strip()
            cr = list(scr.split("  "))
            # print(cr)
            writer.write("created".encode())
            data = await reader.read(400)
            smod = data.decode().strip()
            mod = list(smod.split("  "))
            # print(mod)
            writer.write("modified".encode())
            for fol in range(len(name)):
                print(f"{name[fol]}  {size[fol]}   {cr[fol]}  {mod[fol]}")
            # print(msg)
        elif cmdch == '5':
            data = await reader.read(100)
            msg = data.decode().strip()
            on = input(msg)
            writer.write(on.encode())
            data = await reader.read(100)
            msg = data.decode().strip()
            print(msg)
        elif cmdch == "0":
            break
        elif cmdch == "6":
            print("The list of commands are:")
            for com in range(len(commands)):
                print(scommands[commands[com]], end="||")
            print()
        else:
            print("Wrong Command")
    response = await reader.read(100)
    msg = response.decode().strip()
    print(msg)
