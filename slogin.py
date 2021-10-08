"""
This slogin module has the logic of login for user
--------------------------------------------------
The function in the module will plays a vital role in the
excecution has the implemention of all commands, which are given
by the user.
"""
import fileinput
import operations

async def login(reader, writer):
    """
    This function has the implentation of all the commands like
    create folder, Write file, Read file, List of Directories,
    Change folder name.And acces the operations in the operations
    module.
    """
    logmsg = """*********-Login Form-***********\nEnter UserID   : """
    writer.write(logmsg.encode())
    print("Waiting for the User Name")
    response = await reader.read(100)
    UserID = response.decode().strip()
    passmsg = "Enter Password : "
    writer.write(passmsg.encode())
    print("Waiting for password")
    response = await reader.read(100)
    passw = response.decode().strip()
    fp = "E:\\BTH\\DV1614\\Assignments\\Assignment 3\\root\\admin\\Registration.txt"
    c = 0
    b = True
    # checking the user is in logged state or not
    with open(fp, 'r') as p:
        for line in p:
            if UserID in line:
                if passw in line:
                    c = 1
                    if "logged" in line:
                        msg = "You have logged in already\nAccess Denied"
                        writer.write(msg.encode())
                        print("Denied")
                        b = False
                        break
    # adding the logged word in th registration file to check wheater user
    # logged or not
    if b:
        for line in fileinput.FileInput(fp, inplace=1):
            if UserID in line:
                if passw in line:
                    line = line.rstrip()
                    line = line.replace(line, line + "logged\n")
            print(line, end='')
    if c != 1:
        msg = "Invalid Username or Password"
        writer.write(msg.encode())
        print(msg)
    elif c == 1 and b:
        try:
            print("Granted")
            msg = "Login Access Granted..:-)\nWelcome"
            writer.write(msg.encode())
            long = """\nCommand are:
            1.Create_Folder(name)
            2.Write_File
            3.Read_File
            4.List_of_directories
            5.Change_path(folname)
            6.Commands List
            0.LogOut"""
            user = operations.Operations(UserID)
            while True:
                writer.write(long.encode())
                print("Waiting for Command")
                response = await reader.read(100)
                command = response.decode().strip()
                # command for the create folder
                if command == '1':
                    msg = "Enter folder name : "
                    writer.write(msg.encode())
                    print("Waiting for folder name")
                    data = await reader.read(100)
                    fname = data.decode().strip()
                    c = user.create_folder(fname)
                    if c:
                        msg = "File has been Created!"
                        print(msg)
                        writer.write(msg.encode())
                    else:
                        msg = "File Exists Already"
                        print(msg)
                        writer.write(msg.encode())
                # command for the file creation
                elif command == '2':
                    mdf = "Enter folder name/to write in same directory give(.):"
                    writer.write(mdf.encode())
                    print("Waiting for folder name/(.)")
                    data = await reader.read(50)
                    folname = data.decode().strip()
                    msg = "Enter file name : "
                    writer.write(msg.encode())
                    print("Waiting for file name")
                    data = await reader.read(50)
                    filename = data.decode().strip()
                    msg = "Enter the data : "
                    writer.write(msg.encode())
                    print("Waiting for Data to be written in file")
                    data = await reader.read(50)
                    idata = data.decode().strip()
                    val = user.write_file(folname, filename, idata)
                    if val:
                        msg = "File Created"
                    else:
                        msg = "File exists"
                    print(msg)
                    writer.write(msg.encode())
                # command for the file read
                elif command == '3':
                    msg = "Enter folder name/to read in same directory give(.): "
                    writer.write(msg.encode())
                    print("Waiting for folder name")
                    data = await reader.read(100)
                    folname = data.decode().strip()
                    msg = "Enter file name : "
                    writer.write(msg.encode())
                    print("Waiting for file name")
                    data = await reader.read(100)
                    filename = data.decode().strip()
                    kin = str(user.read_file(folname, filename))
                    writer.write(kin.encode())
                # command for the list of files/folders
                elif command == '4':
                    lname, lsize, lcr, lmod = user.list_of()
                    msg = "Name      Size         Created           Modified"
                    writer.write(msg.encode())
                    data = await reader.read(100)
                    msg = data.decode().strip()
                    print(msg+"Reached")
                    sname = str(" ".join(lname))
                    writer.write(sname.encode())
                    data = await reader.read(100)
                    msg = data.decode().strip()
                    print(msg+"Reached")
                    ssize = str(" ".join(map(str, lsize)))
                    writer.write(ssize.encode())
                    data = await reader.read(100)
                    msg = data.decode().strip()
                    print(msg+"Reached")
                    scr = str("  ".join(map(str, lcr)))
                    writer.write(scr.encode())
                    data = await reader.read(100)
                    msg = data.decode().strip()
                    print(msg+"Reached")
                    smod = str("  ".join(map(str, lmod)))
                    writer.write(smod.encode())
                    data = await reader.read(100)
                    msg = data.decode().strip()
                    print(msg+"Reached")
                # command for the change folder path
                elif command == '5':
                    msg = "Enter Folder name : "
                    writer .write(msg.encode())
                    print("Waiting for folder name")
                    data = await reader.read(100)
                    oname = data.decode().strip()
                    nap = user.change_folname(oname)
                    if nap:
                        msg = "Path Changed Successfully"
                    else:
                        msg = "NO file Exists"
                    print(msg)
                    writer.write(msg.encode())
                # logging out
                elif command == '0':
                    break
                elif command == "6":
                    print("Commands Printed")
                else:
                    print("Wrong Command")

        except Exception as error:
            print(error)

        finally:
            # logic to remove the logged word in file.
            for line in fileinput.FileInput(fp, inplace=1):
                if UserID in line:
                    if passw in line:
                        line = line.rstrip()
                        line = line.replace(line, f"{UserID}:{passw},\n")
                print(line, end='')
            print("Logged Out")
            msg = "Log Out Successfull"
            writer.write(msg.encode())
