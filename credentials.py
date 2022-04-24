import string
import random

class Credentials:
    user_passwords = []

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password
