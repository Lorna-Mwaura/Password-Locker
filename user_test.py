import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """setup method that runs before each test case"""
        self.user = User("lorna","mwaura","lorna-mwaura", "password")
        User.user_accounts = []
    
    def test_user_created(self):
        """Method that tests if the constructor works"""
        self.assertEqual(self.user.first_name, "lorna")
        self.assertEqual(self.user.last_name, "mwaura")
        self.assertEqual(self.user.username, "lorna-mwaura")
        self.assertEqual(self.user.password, "password")
    
    def test_user_saved(self):
        """tests the save user method"""
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)
    
    def test_user_delete(self):
        """tests the delete user method"""
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)
        self.user.delete_user()
        self.assertEqual(len(User.display_user_accounts()), 0)

    def test_login(self):
        """test if login method works"""
        self.user.save_user()
        self.assertEqual(User.login(
            self.user.username, self.user.password), True)

    def test_find_user(self):
        """test search-user method using the username"""
        self.user.save_user()
        self.assertEqual(User.find_user(self.user.username), self.user)

    def test_display_user_accounts(self):
        """test if show all accounts method shows all accounts"""
        self.user.save_user()
        self.assertEqual(User.display_user_accounts(), User.user_accounts)

if __name__ == "__main__":
    unittest.main()
