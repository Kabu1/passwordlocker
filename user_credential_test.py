import unittest #importing unittest module
from user import User #importing the user class
from credentials import Credential


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
    def test__init(self):
        '''
        Test to check if the initialization of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name,"Test")
        self.assertEqual(self.new_user.last_name,"User")
        self.assertEqual(self.new_user.password,"Pass@2020")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the contact list
        '''
        self.new_user.save_user()#saving the new contact
        self.assertEqual(len(User.user_list),1)
if __name__ == '__main__':
    unittest.main()