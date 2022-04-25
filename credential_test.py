import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
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
        
    def test_random_password(self):
        '''
          test to check if the random password generated is in the password list array
        '''
        self.assertTrue(Credentials.password_list.index(self.new_user.generate_random_password())>0)
    
   
        
if __name__ == "__main__":
    unittest.main()