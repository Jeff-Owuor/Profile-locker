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
        
    def test_random_password(self):
        '''
          test to check if the random password generated is in the password list array
        '''
        self.assertTrue(Credentials.password_list.index(self.new_user.generate_random_password())>0)
    
    def test_save_user(self):
        '''
          test to confirm we can store our object
        '''
        self.new_user.save_user()
        self.assertEqual(len(Credentials.user_list),1)
        
    def tearDown(self):
        '''
          tearDown method that does the clean up after each test has run 
        '''
        Credentials.user_list = []
        
    def test_save_users(self):
        '''
           test to confirm we can store more than one object
        '''
        self.new_user.save_user()
        test_user = Credentials("Omondi-Timon","WhatATimeToBeAlive2k")
        test_user.save_user()
        self.assertEqual(len(Credentials.user_list),2)
        
    def test_delete_users(self):
        '''
         Test to confirm we are able to remove an object from our list
        '''
        self.new_user.save_user()
        test_user = Credentials("Omondi-Timon","WhatATimeToBeAlive2k")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(Credentials.user_list),1)
        
    def test_display_users(self):
        '''
          Test to affirm that we can see all the objects in our list
        '''
        self.assertEqual(Credentials.display_users(),Credentials.user_list)
        
        
if __name__ == "__main__":
    unittest.main()