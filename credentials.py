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
    