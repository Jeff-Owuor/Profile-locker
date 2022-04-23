import unittest
from User import User

class TestUser(unittest.TestCase):
    '''
      Class that defines test cases for the User class behaviour
      Args:unittest.TestCase creates test cases for the class
    '''
    def setUp(self):
        self.new_user = User("SpectreJeff");
        
    def test_init(self):
        '''
          Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"SpectreJeff")
        
    def save_user(self):
        '''
          Test to save a user 
        '''
        self.save_user_name();
        self.assertEqual(len(User.users_list),1)
    
    
if __name__ == "__main__":
    unittest.main()