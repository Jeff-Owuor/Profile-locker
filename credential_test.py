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
        self.new_user = Credentials("SpectreJeff","Random33!");
        
    def test_init(self):
        '''
          Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"SpectreJeff")
        self.assertEqual(self.new_user.password,"Random33!")
        
    def test_save_user(self):
        '''
          Test to confirm we are storing the object
        '''
        self.new_user.save_user()
        self.assertEqual(len(Credentials.user_list),1)
        
    def tearDown(self):
        '''
           Method that runs after every test to clean up
        '''
        Credentials.user_list = []
    
    
if __name__ == "__main__":
    unittest.main()