#!/usr/bin/env python3.8

from password import User, Credentials

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
  credentials.save_credentials()

def show_account_info():
  '''
  function to display user account information
  '''
  return Credentials.show_credentials()

def delete_credential(credentials):
  '''
  function to delete a credential from cred list
  '''
  credentials.delete_credential()

def search_credential(account):
  '''
  function to search for a credential if it exist
  '''
  return Credentials.find_by_account(account)

def verify_credentials(account):
  '''
  function fo verify if a credential exist in our list
  '''

  return Credentials.verify_credential_exists(account)

def generate_random_password():
  '''
  function to generate a random password

  '''
  passwordLength = int(input('\nEnter the length of password: '))
  random_password = Credentials.passwordGenerator(passwordLength)
  return random_password

def copy_password(account):
  '''
  a function to copy a password using pyperclip
  '''

  return Credentials.copy_password(account)

def main():
  print("#"*30)
  print("\n")

  print('Hello, What is your name')
  name = input('Enter you Name: ')
  print("\n")

  print(f"Hey {name}, Welcome to Password locker App. \n Enter one of the following code to proceed. \n CU --> Create New User \n LG --> If you already have an account \n")
  print("\n")
  print("Short code")
  short_code = input('').lower()
  if short_code == 'cu':
    print('Register')
    print("#"*20)
    username = input('Enter your Username: ')
    while True:
      print(" Choose between computer generated password or your own password. \n OP --> To use your own password \n CP --> To use computer generated password" )
      print('Password Option')
      print("_"*30)
      password_option = input().lower()
      print("_"*30)
      if password_option == 'op':
        password = input("Key in your password: ")
        break
      elif password_option == 'cp':
        password = generate_random_password()
        break
      else:
        print("Invalid password option. Try again")
    save_user(create_newUser(username, password))
    print("#"*50)
    print(f"Greating {username}, you have successfully created your account and your password is: {password}")
    print("#"*50)
  elif short_code == 'lg':
    print("#"*50)
    username = input('Enter your username: ')
    password = input("Key in your password: ")
    sign_in = user_login(username, password)
    if user_login == sign_in:
      print(f"Greating {username}. Welcome to Password locker Manager")
      print("\n")
  
  while True:
    print("Choose one of the short codes: \n CC --> CREATE A NEW CREDENTIAL \n SC --> SHOW CREDENTIALS \n SRC --> SEARCH FOR A CREDENTIAL \n GP --> GENERATE A RANDOM PASSWORD \n DL --> DELETE A CREDENTIAL \n EX --> EXIT THE APP \n")

    print('Short Code: ')
    short_code = input().lower()
    if short_code == 'cc':
      print("Create a new credential")
      print('#'*20)
      print('Enter your account name: ')
      account = input()
      print('enter your username for the account: ')
      username = input()
      while True:
        print("Choose between computer generated password or your own password. \n OP --> To use your own password \n CP --> To use computer generated password" )
        print('Password Option')
        password_option = input().lower()
        print("____")
        if password_option == 'op':
          password = input("Key in your password: ")
          break
        elif password_option == 'cp':
          password = generate_random_password()
          break
        else:
          print("*"*30)
          print("Invalid password option. Try again")
          print("*"*30)

      save_credentials(register_new_credential(account, username, password))
      print("\n")
      print(f"Credential for {account} - user name: {username} - Password : {password} created successfully")
      print("\n")
    elif short_code == 'sc':
      if show_account_info():
        print('You saved accounts are: ')
        print("#"*30)
        for account in show_account_info():
          print("*"*30)
          print(f"Account: {account.account} \n User name: {username}\n Password: {password} ")
          print("*"*30)
        print("#" * 30)
      else:
        print("*"*30)
        print("The is no saved credentials in your list")
        print("*"*30)

    elif short_code == 'src':
      print("Enter account name to search")
      search_acc = input().lower()
      if search_credential(search_acc):
        find_credential = search_credential(search_acc)
        print("*"*30)
        print(f'Account Registed: {find_credential.account}')
        print(f"Account username: {find_credential.username}")
        print(f"Account Password: {find_credential.password} ")
        print("*"*30)
        print("#"*30)
      
      else:
        print("*"*30)
        print("No Credential exist with that username. ")
        print("*"*30)
        print("\n")

    elif short_code == "dl":
      print("Key in Account name you wish to delete")
      acc_name = input().lower()
      if search_credential(acc_name):
        find_credential = search_credential(acc_name)
        print("#"*30)
        find_credential.delete_credential()
        print("\n")
        print(f"{find_credential.account} successfully deleted")
        print("\n")
      else:
        print("*"*30)
        print("The credential you want to delete doesnot exist")
        print("*"*30)
    elif short_code == 'gp':
      password = generate_random_password()
      print(f"{password} has been generated. you can proceed to use it to your account")
    elif short_code == "ex":
      print("Thank you for trusting us with your data.")
      break
    else:
      print("*"*30)
      print("Wrong short code. TRY again with the one given in the menu")
      print("*"*30)
  else:
    print("*"*30)
    print("Enter a valid input to continue")
    print("*"*30)

if __name__ == "__main__":
  main()