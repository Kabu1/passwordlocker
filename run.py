#!/usr/bin/env python3.8
from user import User
from credentials import Credential
import pyperclip

def create_user(first_name,last_name,password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name,last_name,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user account
    '''
    user.save_user(user)
def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass
def create_credential(user_name,acc_name, email, acc_password):
    '''
    function to create a new credential
    '''
    new_credential = Credential(user_name, acc_name, email, acc_password)
    return new_credential
def save_credential(credential):
    '''
    function to save a newly created credential
    '''
    Credential.save_credential(credential)
