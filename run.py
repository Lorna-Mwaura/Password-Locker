#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(first_name, last_name, username, password):
    """Function to create a new user"""
    return User(first_name, last_name, username, password)

def show_options():
    print("Please choose an option to continue: ")
    print("1. Create Account\n2. Login\n3. Display Accounts\n4. Exit")

def create_account_option():
    print("Please provide the following details to create an account")
    print('*' * 70)

    print("Enter your first name .....")
    first_name = input()
    print("Enter your last name .....")
    last_name = input()
    print("Enter your username .....")
    username = input()
    print("Enter password .....")
    user_password = input()

    user = create_user(first_name, last_name, username, user_password)

    user.save_user()

    return user

def user_login():
    print("Enter your details to login")
    print("Enter your username .....")
    username = input()
    print("Enter password .....")
    user_password = input()

    return User.login(username, user_password)
