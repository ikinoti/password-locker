class User:
  '''
  class that generate new instance of user
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

  