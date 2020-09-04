import unittest #importing unittest module
from user import User #importing the user class
from credentials import Credentials #importing the credentials class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class 

    Args: 
        unittest.TestCase: helps in creating test cases
    '''
        def setUp(self):
            '''
            Set up method that runs before each test case is conducted.
            '''
            self.new_user = User("Test","User","Pass@2020")