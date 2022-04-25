#!/usr/bin/env python3.9

from User import User
from credentials import Credentials

def create_user(user_name,phone,email,password):
    '''
      Function to create a new user
    '''
    new_user = User(user_name,phone,email,password)
    return new_user
def save_users(user):
    '''
       function to save a user
    '''
    user.save_user()
    
def delete_users(user):
    '''
       function to delete a user 
    '''
    user.delete_user()
    
    
def display_users():
    '''
      function that returns all saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print("\n")
    while True:
        print("Use these short codes : ca - create a new account, du - display user, ex - exit the contact list")
        short_code = input().lower()
        if short_code == 'ca':
            print("New User")
            print("-"*10)
            print("First name ...")
            user_name = input()
            
            print("Phone number ...")
            p_number = input()
            
            print("Email address ...")
            e_address = input()
            
            print("Last name ...")
            password = input()
            
            
            save_users(create_user(user_name,p_number,e_address,password));
            print("\n")
            print(f"New User  {user_name} created")
            print("\n")
            
        elif short_code == 'du':
            if display_users():
                print("Here is a list of all your accounts")
                print("\n")
                for user in display_users():
                    print(f"{user.user_name} ..... {user.password}")
                    print('\n')
            else:
                print('\n')
                print("You do not seem to have any account saved yet")
                print('\n')
            
        elif short_code == "ex":
            print("Bye .....")
            break
        else:
            print("I really didn't get that. Please use the short codes")

    
