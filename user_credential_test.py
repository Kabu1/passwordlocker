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


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviors.
    '''
    def setUp(self):
        '''
        Function to create credentials before each test
        '''
        self.new_credential = Credential("Test","Twitter","testuser2020@yahoo.com","Pass@2020")
    def test__init(self):
        '''
        test to check if initialization is properly done
        '''
        self.assertEqual(self.new_credential.user_name, 'Test')
        self.assertEqual(self.new_credential.acc_name,'Twitter')
        self.assertEqual(self.new_credential.email,'testuser2020@yahoo.com')
        self.assertEqual(self.new_credential.acc_password,'Pass@2020')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credential list
        '''
        self.new_credential.save_credentials()
        facebook = Credential("Jane","Facebook","janejane@yahoo.com","Password@2019")
        facebook.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
    
if __name__ == '__main__':
    unittest.main()