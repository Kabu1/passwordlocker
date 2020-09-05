import unittest #importing unittest module
from user import User #importing the user class
from credentials import Credential
import pyperclip


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
        self.new_user = User("Test","User","Pass2020")
    def test__init(self):
        '''
        Test to check if the initialization of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name,"Test")
        self.assertEqual(self.new_user.last_name,"User")
        self.assertEqual(self.new_user.password,"Pass2020")
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
        self.new_credential = Credential("Jack","Facebook","testuser2020@yahoo.com","Pass2020")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credentials_list = []

    def test__init(self):
        '''
        test to check if initialization is properly done
        '''
        self.assertEqual(self.new_credential.user_name, 'Jack')
        self.assertEqual(self.new_credential.acc_name,'Facebook')
        self.assertEqual(self.new_credential.email,'testuser2020@yahoo.com')
        self.assertEqual(self.new_credential.acc_password,'Pass2020')

    def test_save_credential(self):
        '''
        test case to test if the object is saved into the contact list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
    
    def test_save_multiple_credential(self):
        '''
        Test to check if the new credential info is saved into the credential list
        '''
        self.new_credential.save_credential()
        twitter = Credential("Jane","Twitter","janejane@yahoo.com","Pass2019")
        twitter.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
    def test_delete_credential(self):
        '''
        test to check whether we can remove a credential from the list
        '''
        self.new_credential.save_credential()
        twitter_credential = Credential("Jane","Twitter","manejane@yahoo.com","Pass2019")
        twitter_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
    def test_display_all_credentials(self):
        '''
        test to check if display is done correctly
        '''
        self.new_credential.save_credential()
        twitter_credential = Credential("Jane","Twitter","Janejane@yahoo.com","Pass2019")
        twitter_credential.save_credential()
        gmail = Credential('mary','Gmail','maryjon@yahoo.com','pswd200')
        gmail.save_credential()
        self.assertEqual(len(Credential.display_all_credentials(gmail.user_name)),2)

    def test_find_by_acc_name(self):
        '''
        test to find credentials using the account name
        '''
        self.new_credential.save_credential()
        twitter_credential = Credential("Jane","Twitter","Janejane@yahoo.com","Pass2019")
        twitter_credential.save_credential()
        credential_exists = Credential.find_by_acc_name("Twitter")
        self.assertTrue(credential_exists)
    
    def test_copy_credential(self):
        '''
        Test to check if copy credential method works
        '''
        self.new_credential.save_credential()
        twitter_credential = Credential("Jane","Twitter","Janejane@yahoo.com","Pass2019")
        twitter_credential.save_credential()
        find_credential = None
        for credential in Credential.credentials_list:
            find_credential = Credential.find_by_acc_name(credential.acc_name)
            return pyperclip.copy(find_credential.acc_password)
        Credential.copy_credential(self.new_credential.acc_name)
        self.assertEqual("Pass2019",pyperclip.paste())
        print(pyperclip.paste())
        

if __name__ == '__main__':
    unittest.main()