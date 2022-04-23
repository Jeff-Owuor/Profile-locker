import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
      Class that defines test cases for the User class behaviour
      Args:unittest.TestCase creates test cases for the class
    '''
    def setUp(self):
        '''
          Runs before the tests
        '''
        self.new_user = Credentials("SpectreJeff");
        
    def test_init(self):
        '''
          Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"SpectreJeff")
        
    def test_save_user(self):
        '''
          Test to confirm we are storing the object
        '''
        self.new_user.save_user()
        self.assertEqual(len(Credentials.user_list),1)
    
    
if __name__ == "__main__":
    unittest.main()