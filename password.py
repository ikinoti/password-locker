class User:
  '''
  class that generate user objects
  '''
  user_list = []

  def __init__(self, username, password):
    '''
    method that helps us define properties for our objects
    '''
    self.username = username
    self.password = password
    
  def save_user(self):
    '''
    save user object into user_list
    '''
    User.user_list.append(self)

  @classmethod
  def show_user(cls):
    '''
    method to show user saved in the list'''
    return cls.user_list

  def delete_user(self):
    '''
    method to delete saved contact from the user list
    '''
    User.user_list.remove(self)


class Credentials:
  '''
  class that generate credentials objects
  '''
  credentials_list = []
  def __init__(self, account, username, password):
    '''
    method that helps us define properties for our credential objects
    '''
    self.account = account
    self.username = username
    self.passwword = password
  
  def save_credentials(self):
    '''
    method to save credential object into credential_list
    '''
    Credentials.credentials_list.append(self)

  def delete_credential(self):
    '''
    method to delete saved contact from the user list
    '''
    Credentials.credentials_list.remove(self)


  # @classmethod
  # def find_by_username(cls, username):
  #   '''
  #   method that take a username and returns a user object that matches that number
  #   '''
  #   for user in cls.user_list:
  #     if user.username == username:
  #       return user

  # @classmethod
  # def user_exist(cls, username):
  #   '''
  #   method to check if user acc exist in the user list
  #   '''
  #   for user in cls.user_list:
  #     if user.username == username:
  #       return True
  #   return False