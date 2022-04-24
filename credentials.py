import string
import random

class Credentials:
    user_passwords = []


    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def save_platform_credentials(self):
        """method that appends credentials to the credentials list"""
        Credentials.user_passwords.append(self)

    def delete_platform_credentials(self):
        """removes credentials from the user passwords array"""
        Credentials.user_passwords.remove(self)
