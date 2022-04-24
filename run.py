#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

def create_user(first_name,last_name,username,password):
    return User(first_name,last_name,username,password)