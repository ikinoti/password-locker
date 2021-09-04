#!/usr/bin/env python3.8

from password import User, Credentials

print('Hello, What is your name')
name = input('Enter you Name: ')
print("\n")

print(f"Hey {name}, Welcome to Password locker App")
print("\n")

def create_newUser(username, password):
  '''
  Method to create a new user
  '''
  new_user = User(username, password)
  return new_user

def save_user(user):
  '''
  method to save user created by create newUser method
  '''
  user.save_user()

def show_user():
  '''
  function to show existing user
  '''
  return User.show_user()

def user_login(username, password):
  '''
  function to check if our user exist in our list and then login in that user
  '''

  confirm_user = Credentials.check_valid_login(username, password)
  return confirm_user

def register_new_credential(account, username, password):
  '''
  function to register a new credetial of a given account
  '''
  new_credential = Credentials(account, username, password)
  return new_credential

def save_credentials(credentials):
  '''
  function to user credential in the credential list
  '''
  credentials.save_credentials


