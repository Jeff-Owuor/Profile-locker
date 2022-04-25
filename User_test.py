import unittest

from credentials import User

class TestUsers(unittest.TestCase):
    '''
      Class that defines test cases for the User class behaviour
      Args:unittest.TestCase creates test cases for the class
    '''
    def setUp(self):
        '''
          Runs before the tests
        '''
        self.new_user = User("SpectreJeff","Random33!");
        
    def test_init(self):
        '''
          Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"SpectreJeff")
        self.assertEqual(self.new_user.password,"Random33!")
        
    def test_save_user(self):
        '''
          test to confirm we can store our object
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
        '''
          tearDown method that does the clean up after each test has run 
        '''
        User.user_list = []
        
    def test_save_users(self):
        '''
           test to confirm we can store more than one object
        '''
        self.new_user.save_user()
        test_user = User("Omondi-Timon","WhatATimeToBeAlive2k")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
        
        