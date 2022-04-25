from credentials import User
from credentials import Credentials

def create_contact(user_name,password):
    '''
      Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user
def save_contacts(credentials):
    '''
       function to save credentials
    '''
    credentials.save_contact()
    
