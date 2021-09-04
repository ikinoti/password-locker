import unittest 
from password import User

class TestClass(unittest.TestCase):
  '''
  test case for the classes behaviours
  '''
  def setUp(self):
    '''
    method to run before each test case
    '''
    self.new_user = User('ikinoti', '12qwerty34')

  def test_init(self):
    '''
    test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.username, 'ikinoti')
    self.assertEqual(self.new_user.password, '12qwerty34')
  
  def tearDown(self):
    '''
    method to clean up after each test case has run
    '''
    User.user_list = []

  def test_save_user_details(self):
    '''
    test if the user objec is saved in the user list
    '''

    self.new_user.save_user()
    self.assertEqual(len(User.user_list), 1)
  
  def test_save_multiple_user(self):
    '''
    test case to test if we can be able to save multiple user objects in our list
    '''
    self.new_user.save_user()
    new_user1 = User('igitonga', '1234')
    new_user1.save_user()
    self.assertEqual(len(User.user_list), 2)

if __name__ == '__main__':
  unittest.main()