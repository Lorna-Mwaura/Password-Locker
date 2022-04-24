import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """setup method that runs before each test case"""
        self.user = User("lorna","mwaura","lorna-mwaura","password")
        User.user_accounts = []
    
    def test_user_created(self):
        """Method that test if the constructor works"""
        self.assertEqual(self.user.first_name, "lorna")
        self.assertEqual(self.user.last_name, "mwaura")
        self.assertEqual(self.user.username, "lorna-mwaura")
        self.assertEqual(self.user.password, "password")

    def test_user_saved(self):
        """Test the dave user method"""
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)


if __name__ == "__main__":
    unittest.main()