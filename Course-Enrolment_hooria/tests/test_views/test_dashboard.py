import unittest
from unittest.mock import patch, MagicMock
from app.views import dashboard

class TestDashboard(unittest.TestCase):

    @patch('app.views.dashboard.mysql.connector.connect')
    def test_create_course(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Simulate course creation
        dashboard.entry_title = MagicMock()
        dashboard.entry_title.get.return_value = 'Math'
        dashboard.entry_desc = MagicMock()
        dashboard.entry_desc.get.return_value = 'Algebra basics'

        dashboard.create_course()
        mock_cursor.execute.assert_called_once()

    @patch('app.views.dashboard.mysql.connector.connect')
    def test_enroll_student(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        dashboard.entry_student_id = MagicMock()
        dashboard.entry_student_id.get.return_value = '1'
        dashboard.entry_course_id = MagicMock()
        dashboard.entry_course_id.get.return_value = '2'

        dashboard.enroll_student()
        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()
