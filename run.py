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


