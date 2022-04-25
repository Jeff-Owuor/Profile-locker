import random
class Credentials:
    user_list = []
    password_list = ["Bully911","Champez254","Lildurk7","XotourUzi1","Emergingh20","dIvergencE666","ModuloFanForum11","Oldtraffordseat12"]
    random_password = random.choice(password_list)
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
      
    @classmethod    
    def generate_random_password(cls):
        '''
         function that returns a random password
        '''
        return cls.random_password
    
