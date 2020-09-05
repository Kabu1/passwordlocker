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