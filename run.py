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
    user.save_user()
def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user
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
    credential.save_credential()
def delete_credential(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credential()
def find_by_acc_name(acc_name):
    '''
    Function to check if a credential exists
    '''
    return Credential.find_by_acc_name(acc_name)


def display_all_credentials(user_name):
    '''
    function to display credentials saved by a user
    '''
    return Credential.display_all_credentials(user_name)

def copy_credential(acc_name):
    '''
    function to copy a credential details to the clipboard
    '''
    return Credential.copy_credential(acc_name)
def main():
    print("Hello there, welcome to your Password Locker 😜")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes to navigate : cc -create a new account, li-Log In, ex-Exit")
        short_code = input('Enter a choice: ').lower()

        if short_code == 'ex':
            break
        elif short_code == 'cc':
            print("To create a new account")
            print("-"*10)
            print("First name ....")
            first_name = input()

            print("Last name ....")
            last_name = input ()

            print("password ....")
            password = input()

            save_user(create_user(first_name, last_name, password))
            print(f'Congratulations 🎉, New Account has been created for: {first_name} {last_name} using password: {password}')

        elif short_code == 'li':
            print("-"*10)
            print('To login, enter you account details:')
            print("First name ....")
            first_name = input()
            print("Password ....")
            password = input()
            user_exists = verify_user(first_name, password)
            if user_exists == first_name:
                print(f'Welcome back 😍 {first_name}. please choose an option to continue')

                while True:
                    print('Use these codes to navigate: nc -create a credential, dc-dipslay credentials, cp-copy credential, ex-exit')
                    short_code == input('Enter your choice: ').lower()

if __name__ == '__main__':
	main()