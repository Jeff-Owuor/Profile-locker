from User import User
from credentials import Credentials

def create_contact(user_name,password):
    '''
      Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user
def save_contacts(user):
    '''
       function to save a user
    '''
    user.save_user()
    
def delete_contact(user):
    '''
       function to delete a user 
    '''
    user.delete_user()
    
    
def display_contacts():
    '''
      function that returns all saved users
    '''
    return User.display_users()
