import unittest
from unittest.mock import patch
from app.services.auth import authenticate

class TestAuth(unittest.TestCase):

    @patch('app.services.auth.mysql.connector.connect')
    def test_authenticate_valid_user(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = ['student']

        role = authenticate('validuser', 'validpass')
        self.assertEqual(role, 'student')

    @patch('app.services.auth.mysql.connector.connect')
    def test_authenticate_invalid_user(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        role = authenticate('wronguser', 'wrongpass')
        self.assertIsNone(role)

if __name__ == '__main__':
    unittest.main()
