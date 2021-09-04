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

if __name__ == '__main__':
  unittest.main()