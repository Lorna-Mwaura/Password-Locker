class User:

    
    def __init__(self, first_name, last_name, username, password):
        """user constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    user_accounts = []

    def save_user(self):
        """Append user to the user accounts lists"""
        User.user_accounts.append(self)

