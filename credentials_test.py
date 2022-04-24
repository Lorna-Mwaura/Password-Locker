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

if __name__ == "__main__":
    unittest.main()