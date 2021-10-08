"""
This module is of testing the operations in the server
module and the test is done with the unittest module.
"""
import unittest
import operations

class TestOperations(unittest.TestCase):
    """
    In this class the testcase was taken to test the server code
    (operations) commands, which gives from server to client.
    There are four functions in the sense of four different testcases
    Ofcourse the methods was passed the test without any fail.
    """
    def test1_all_functions(self):
        """
        In this 1st test case the userid is lokesh90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = operations.Operations("lokesh90")

        createfol = opera.create_folder("cats")
        self.assertEqual(createfol, True)

        writefil = opera.write_file("cats", "snoopy", "Snoopy is good cat")
        self.assertEqual(writefil, True)

        readfil = opera.read_file("cats", "snoopy")
        self.assertEqual(readfil, "Snoopy is good cat")

        change = opera.change_folname("cats")
        self.assertEqual(change, True)

    def test2_all_functions(self):
        """
        In this 2nd test case the userid is suresh90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = operations.Operations("suresh90")

        createfol = opera.create_folder("dogs")
        self.assertEqual(createfol, True)

        writefil = opera.write_file("dogs", "tommy", "tommy is good dog")
        self.assertEqual(writefil, True)

        readfil = opera.read_file("dogs", "tommy")
        self.assertEqual(readfil, "tommy is good dog")

        change = opera.change_folname("dogs")
        self.assertEqual(change, True)

    def test3_all_functions(self):
        """
        In this 3rd test case the userid is naresh90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = operations.Operations("naresh90")

        createfol = opera.create_folder("monkey")
        self.assertEqual(createfol, True)

        writefil = opera.write_file("monkey", "cuty", "cuty is good monkey")
        self.assertEqual(writefil, True)

        readfil = opera.read_file("monkey", "cuty")
        self.assertEqual(readfil, "cuty is good monkey")

        change = opera.change_folname("monkey")
        self.assertEqual(change, True)

    def test4_all_functions(self):
        """
        In this 4th test case the userid is nibbesh90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = operations.Operations("nibbesh90")

        createfol = opera.create_folder("nibbi")
        self.assertEqual(createfol, True)

        writefil = opera.write_file("nibbi", "boy", "my name is good boy")
        self.assertEqual(writefil, True)

        readfil = opera.read_file("nibbi", "boy")
        self.assertEqual(readfil, "my name is good boy")

        change = opera.change_folname("nibbi")
        self.assertEqual(change, True)

if __name__ == "__main__":
    unittest.main()
