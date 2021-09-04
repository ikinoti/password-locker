import random
import string
import pyperclip

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

  @classmethod
  def check_valid_login(cls, username, password):
    '''
    method to check where user is in our user_list
    '''
    userL = ""
    for userN in User.user_list:
      if(userN.username == username and userN.password == password):
        userL == userN.ussername
    return userL


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


  @classmethod
  def find_by_account(cls, account):
    '''
    method that take a account and returns a credential object that matches that number
    '''
    for cred in cls.credentials_list:
      if cred.account == account:
        return cred

  @classmethod
  def copy_password(cls, account):
    found_credentials = Credentials.find_by_account(account)
    pyperclip.copy(found_credentials.password)

  @classmethod
  def credential_exists(cls, account):
    '''
    method to check if user acc exist in the user list
    '''
    for cred in cls.credentials_list:
      if cred.account == account:
        return True
    return False

  @classmethod
  def show_credentials(cls):
    '''
    method that returns the credential list
    '''

    return cls.credentials_list

  def passwordGenerator():
    '''
    method to generate a random password

    '''
    print("We are glad to generate a strong password for you")

    passwordLength = int(input('\nEnter the length of password: '))

    all = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.sample(all, passwordLength))

    return(password)
