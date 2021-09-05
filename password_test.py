import unittest

import pyperclip 
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
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
    test case to test if the user object is initialized properly
    '''
    self.assertEqual(self.new_user.username, 'ikinoti')
    self.assertEqual(self.new_user.password, '12qwerty34')
  

  def test_save_user(self):
    '''
    test if the user objec is saved in the user list
    '''

    self.new_user.save_user()
    self.assertEqual(len(User.user_list), 1)

  def tearDown(self):
    '''
    method to clean up after each test case has run
    '''
    User.user_list = []
  
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


class TestCredentials(unittest.TestCase):
  '''
  test class to defime test case for credentials class
  '''
  def setUp(self):
    '''
    method to run before each credential test case
    '''
    self.new_credential = Credentials('LMS', 'ikinoti', '12qwerty34')

  def test_init(self):
    '''
    test case to test if the credential object is initialized properly
    '''
    self.assertEqual(self.new_credential.account, 'LMS')
    self.assertEqual(self.new_credential.username, 'ikinoti')
    self.assertEqual(self.new_credential.passwword, '12qwerty34')

  def test_cred_user(self):
    '''
    test if the credential objec is saved in the user list
    '''

    self.new_credential.save_credentials()
    self.assertEqual(len(Credentials.credentials_list), 1)
  
  def tearDown(self):
    '''
    method to clean up after each test case has run
    '''
    Credentials.credentials_list = []

  def test_save_multiple_credentials(self):
    '''
    test case to test if we can be able to save multiple credential objects in our list
    '''
    self.new_credential.save_credentials()
    new_credential1 = Credentials('Linkeld', 'igitonga', '1234')
    new_credential1.save_credentials()
    self.assertEqual(len(Credentials.credentials_list), 2)

  def test_delete_credential(self):
    '''
    test case to test if we can remove a user from our user list
    '''
    self.new_credential.save_credentials()
    new_credential1 = Credentials('Linkeld', 'igitonga', '1234')
    new_credential1.save_credentials()

    self.new_credential.delete_credential()
    self.assertEqual(len(Credentials.credentials_list), 1)

  def test_find_credential(self):
    '''
    check if we can find credential by their account and display their information
    '''
    self.new_credential.save_credentials()
    new_credential1 = Credentials('Linkeld', 'igitonga', '1234')
    new_credential1.save_credentials()

    found_credential = Credentials.find_by_account('Linkeld')
    self.assertEqual(found_credential.account, new_credential1.account)

  # def test_copy_password(self):
  #   '''
  #   Test to confirm tht we are copying the password from a found credential
  #   '''
  #   self.new_credential.save_credentials()
  #   Credentials.copy_password('12qwery34')

  #   self.assertEqual(self.new_credential.passwword, pyperclip.paste())


  def test_credential_exists(self):
    '''
    test case to check if we can return a boolean if we can or cannot find the user account
    '''

    self.new_credential.save_credentials()
    new_credential1 = Credentials('Linkeld', 'igitonga', '1234')
    new_credential1.save_credentials()

    cred_exists = Credentials.verify_credential_exists("Linkeld")

    self.assertTrue(cred_exists)

  def test_show_all_credentials(self):
    '''
    method that returns a list of all contacts saved
    '''
    self.assertEqual(Credentials.show_credentials(), Credentials.credentials_list)

if __name__ == '__main__':
  unittest.main()