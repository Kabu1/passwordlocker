import string
import pyperclip
import random

class Credential:
    '''
    class to create users credentials i.e generate passwords and save their information
    '''
    credentials_list = []

    def __init__(self, user_name, acc_name, email, acc_password):
        '''
        defining the properties of object credential
        '''
        self.user_name = user_name
        self.acc_name = acc_name
        self.email = email
        self.acc_password = acc_password

    def save_credential(self):
        '''
        Function to save a newly created user instance
        '''
        Credential.credentials_list.append(self)
    def delete_credential(self):
        '''
        Function to delete a saved credential from the credential_list
        '''
        Credential.credentials_list.remove(self)
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
		Function to generate an 8 character password for a credential
		'''
        gen_pass=" ".join(random.choise(char)for i in range(size))
        return gen_pass
    @classmethod
    def display_all_credentials(cls,user_name):
        '''
        class method to display the lists of credentials saved 
        '''
        credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                credentials_list.append(credential)
        return credentials_list
    @classmethod
    def find_by_acc_name(cls, acc_name):
        '''
        method that returns a credential that matches the acc_name.
        '''
        for credential in cls.credentials_list:
            if credential.acc_name == acc_name:
                return credential
    @classmethod
    def copy_credential(cls,acc_name):
        '''
        class method that copies credential info after site name is entered
        '''
        find_credential = Credential.find_by_acc_name(acc_name)
        return pyperclip.copy(find_credential.acc_password)
