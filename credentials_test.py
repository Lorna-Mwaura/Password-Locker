import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        """setup method that runs before each test case"""
        self.platform = Credentials("github", "lorna-mwaura", "123456")
        Credentials.user_passwords = []

    def test_platform_created(self):
        """Method testing the constructor"""
        self.assertEqual(self.platform.platform, "github")
        self.assertEqual(self.platform.username, "lorna-mwaura")
        self.assertEqual(self.platform.password, "123456")

    def test_save_platform_credentials(self):
        """tests credentials save method if it appends to the list"""
        self.assertEqual(len(Credentials.user_passwords), 0)
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 1)

    def test_delete_platform_credentials(self):
        """tests if the delete credentials method removes from the list"""
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 1)
        self.platform.delete_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 0)

if __name__ == "__main__":
    unittest.main()