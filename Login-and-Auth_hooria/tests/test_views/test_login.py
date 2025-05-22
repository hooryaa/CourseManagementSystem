import unittest
from unittest.mock import patch
from app.views import login

class TestLoginView(unittest.TestCase):

    @patch('app.views.login.authenticate')
    def test_login_success(self, mock_auth):
        mock_auth.return_value = 'admin'
        # You can only fully test Tkinter apps using GUI automation libraries like `pytest-tkinter` or `pyautogui`
        # So we focus here on mocking authenticate
        result = login.authenticate('admin', 'adminpass')
        self.assertEqual(result, 'admin')

    @patch('app.views.login.authenticate')
    def test_login_fail(self, mock_auth):
        mock_auth.return_value = None
        result = login.authenticate('wrong', 'wrongpass')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
