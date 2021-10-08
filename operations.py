"""
This module has the Operations class which operates the commands.
----------------------------------------------------------------
This class has the functions to each commands, which were given to
server from client
"""
import os
import time


class Operations:
    """
    This class has the operations to the each commands
    The functions includes in this are:
    create_folder(name):Creates the folder with that name
    --------
    write_file(folnam,filename,data):
    takes the folname or take the(.) for the same directory and
    file name and data the data written in the file and saved
    with the given name.
    --------
    read_file(folname,filename):
    takes foldername and file name as the input parameters
    and the print the matter in the file
    --------
    list_of():
    shows all the directories,Files and folder in user root.
    --------
    change_path(folname):
    takes the folder name and changes the path.
    """
    def __init__(self, usid):
        self.usid = usid
        self.confirm = False
        self.confirms = False
        self.data = ''
        self.files = 0
        self.size = 0
        self.created = 0
        self.modified = 0
        self.oname = 0
        self.filename = 0
        self.fname = 0
        self.pathread = 0
        self.ver = 0
        self.fname = 0
        self.foname = 0
        self.pathwrite = 0
        self.pathread = 0
        self.input = 0
        self.confirmed = 0
        self.fol = 0
        self.path = 0
        self.p = f"E:\\BTH\\DV1614\\Assignments\\Assignment 3\\root\\{self.usid}\\"
        try:
            os.makedirs(self.p)
        except Exception:
            print("User Exists")

    def create_folder(self, name):
        """
        create_folder(name):Creates the folder with that name and return
        true or false.
        """
        self.fname = name
        self.foname = os.path.join(self.p, self.fname)
        try:
            os.makedirs(self.foname)
            self.confirm = True
        except FileExistsError:
            print("File Exists")
        finally:
            return self.confirm

    def write_file(self, fname, name, inputd):
        """
        takes the folname or take the(.) for the same directory and
        file name and data the data written in the file and saved
        with the given name and also confirms the file is written or not.
        """
        self.filename = name
        if fname != ".":
            self.fname = f"{fname}\\"
            self.pathwrite = os.path.join(self.p, self.fname)
        else:
            self.pathwrite = self.p
        self.input = inputd
        try:
            self.path = os.path.join(self.pathwrite, self.filename)
            with open(self.path, 'w') as file:
                file.write(self.input)
                self.confirms = True
        except Exception as error:
            print(error)
        finally:
            return self.confirms

    def read_file(self, fname, name):
        """
        Takes foldername and file name as the input parameters
        and the print the matter in the file and returns the strings to
        the client from server.
        """
        self.filename = name
        if fname != ".":
            self.fname = f"{fname}\\"
            self.pathread = os.path.join(self.p, self.fname)
        else:
            self.pathread = self.p
        try:
            self.path = os.path.join(self.pathread, self.filename)
            with open(self.path, 'r') as read:
                self.data = read.readlines()
        except Exception as error:
            return error
        finally:
            send = " ".join(self.data)
            return send

    def list_of(self):
        """
        This function shows all the directories,Files and folder in user root.
        and returns the list of names,sizes,created date and time and modified
        date and time.
        """
        self.files = os.listdir(self.p)
        self.size = [0] * len(self.files)
        self.created = [0] * len(self.files)
        self.modified = [0] * len(self.files)
        total_size = 0
        iteration = 0
        for file in self.files:
            self.fol = os.path.join(self.p, file)
            self.modified[iteration] = time.ctime(os.path.getmtime(f"{self.fol}"))
            self.created[iteration] = time.ctime(os.path.getctime(f"{self.fol}"))
            for path, dirs, files in os.walk(self.fol):
                for fol in files:
                    fpath = os.path.join(path, fol)
                    total_size += os.path.getsize(fpath)
            self.size[iteration] = total_size
            iteration += 1
        return self.files, self.size, self.created, self.modified

    def change_folname(self, name):
        """
        This function changes the path of the control
        to the folder and also changes the control to the
        root folder.
        """
        self.oname = f"{name}\\"
        self.ver = os.path.join(self.p, self.oname)
        try:
            os.chdir(self.ver)
            self.confirmed = True
        except Exception as error:
            return error
        finally:
            return self.confirmed

#u = Operations("lokl20")
#u.list_of()