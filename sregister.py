"""
This module has the registration function for registering the
user in the file.And make accessable to  server to
check the credentials for the login.
"""
async def registration(reader, writer):
    """
    This function has the functionality to register the user
    credentials to the file. And also check the same user is
    registered or not.If registered application halts by
    showing the message.
    """
    msg = "********Registration Form********\nEnter your name :"
    writer.write(msg.encode())
    print("Waiting for name")
    response = await reader.read(100)
    # getting name
    name = response.decode().strip()
    msg = "Create a User Name : "
    writer.write(msg.encode())
    print("Waiting for User Name")
    # getting User Name
    response = await reader.read(100)
    usid = response.decode().strip()
    msg = "Enter your Password :"
    writer.write(msg.encode())
    print("Waiting for Password")
    # getting password
    response = await reader.read(100)
    password = response.decode().strip()
    confirm = False
    p = "E:\\BTH\\DV1614\\Assignments\\Assignment 3\\root\\admin\\Registration.txt"
    # checking the user registered before or not
    with open(p, 'r') as fread:
        for line in fread:
            if usid and password in line:
                confirm = True
                break
    # if not registered make user register
    if not confirm:
        with open(p, 'a') as file:
            file.write(usid + ':')
            file.write(password + ', \n')
        msg = f"{name} is Registered Succcessfully..:-)"
        writer.write(msg.encode())
        print("Registration Done")
    else:
        msg = "Request Denied\nYou are already Registered"
        writer.write(msg.encode())
        print("Denied\n User already Registered")
