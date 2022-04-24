#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(first_name, last_name, username, password):
    """Function to create a new user"""
    return User(first_name, last_name, username, password)

def show_options():
    print("Please choose an option to continue: ")
    print("1. Create Account\n2. Login\n3. Display Accounts\n4. Exit")


if __name__ == '__main__':

    main()