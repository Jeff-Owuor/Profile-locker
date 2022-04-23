class Credentials:
    
    user_list = []
    def __init__(self,user_name):
        self.user_name = user_name
        
    def save_user(self):
        '''
          saves a user object to the user_list
        '''
        Credentials.user_list.append(self)
        