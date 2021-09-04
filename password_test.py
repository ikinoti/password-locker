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

  def test_delete_user(self):
    '''
    test case to test if we can remove a user from our user list
    '''
    self.new_user.save_user()
    new_user1 = User('igitonga', '1234')
    new_user1.save_user()

    self.new_user.delete_user()
    self.assertEqual(len(User.user_list), 1)

  def test_find_user_by_username(self):
    '''
    check if we can find user by their username and display their information
    '''
    self.new_user.save_user()
    new_user1 = User('shiku', '1998')
    new_user1.save_user()

    found_user = User.find_by_username('shiku')
    self.assertEqual(found_user.username, new_user1.username)

  def test_user_exists(self):
    '''
    test case to check if we can return a boolean if we cannot find the contact
    '''

    self.new_user.save_user()
    new_user1 = User('shiku', '1998')
    new_user1.save_user()

    user_exists = User.user_exist("shiku")

    self.assertTrue(user_exists)

if __name__ == '__main__':
  unittest.main()