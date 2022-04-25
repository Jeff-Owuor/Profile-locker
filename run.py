#!/usr/bin/env python3.9

from User import User
from credentials import Credentials

def create_user(user_name,phone,email,password):
    '''
      Function to create a new user
    '''
    new_user = User(user_name,phone,email,password)
    return new_user

def create_credential(account,password):
    '''
     Function to create credential
    '''
    
    new_credential = Credentials(account,password)
    return new_credential;
def save_users(user):
    '''
       function to save a user
    '''
    user.save_credential()
    
def delete_users(user):
    '''
       function to delete a user 
    '''
    user.delete_credential()
    
    
def display_users():
    '''
      function that returns all saved users
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to password locker")
    print("Use these short codes : ca - create a new account,lg - login to account")
    short_code = input().lower()
    if short_code == "ca":
        print("New User")
        print("-"*10)
        print("Enter preferred user name ...")
        user_name = input()
            
        print("Phone number ...")
        p_number = input()
            
        print("Email address ...")
        e_address = input()
            
        print("Would you like a suggested password?(Y/N)")
        random_password = input()
        if random_password == "Y":
            passkey = Credentials.generate_random_password()
            print("Password")
            print("*"*8)
        else:
            print("Enter your password")
            passkey = input() 
            
        save_users(create_user(user_name,p_number,e_address,passkey));
        print("\n")
        print(f"New User  {user_name} created")
        print("\n")
        
    elif short_code == "lg":
        print("Please enter your user name and your password")
        print("User name:")
        userName = input()
        print("Enter your password:")
        passWord = input()
        print("It's good to have you back " + userName + " :)")
    while True:
        print("Use the following short codes for your credentials")
        print("cc - create credential, del - delete account,dc - display credential, ex - exit your account")
        short_code = input().lower()
        if short_code == "cc":
            print("New credential")
            print("-"*10)
            print("Enter account")
            account = input()
            print("Would you like a generated password?(Y/N)")
            random_generated_password = input()
            if random_generated_password == "Y":
                credential_password  = Credentials.generate_random_password()
                print("Password")
                print("*"*8)
            else:
                print("Enter your password")
                credential_password  = input() 
            save_users(create_credential(account,credential_password))
        elif short_code == "del":
            delete_users()   
        elif short_code == 'dc':
            if display_users():
                print("Here is a list of all your accounts")
                print("\n")
                for user in display_users():
                    print(f"{user.user_name} <----> {user.password}")
                    print('\n')
            else:
                print('\n')
                print("You do not seem to have any credentials saved yet")
                print('\n')
            
        elif short_code == "ex":
            print("see you soon.....")
            break
        else:
            print("I really didn't get that. Please use the short codes")

    
if __name__ ==  '__main__':
    main()