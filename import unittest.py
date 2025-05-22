import unittest
from unittest.mock import patch, MagicMock
from main import StudentService, AssignmentService

class TestStudentService(unittest.TestCase):

    @patch('main.get_db_connection')
    def test_enroll_student_success(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db.return_value = mock_conn

        result = StudentService.enroll_student("John Doe", "john@example.com", "Math")
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once()

    @patch('main.get_db_connection', side_effect=Exception("DB Error"))
    def test_enroll_student_failure(self, mock_db):
        result = StudentService.enroll_student("John Doe", "john@example.com", "Math")
        self.assertFalse(result)

class TestAssignmentService(unittest.TestCase):

    @patch('main.get_db_connection')
    def test_upload_assignment_success(self, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db.return_value = mock_conn

        result = AssignmentService.upload_assignment("1", "Assignment 1", "/path/to/file.pdf")
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once()

    @patch('main.get_db_connection', side_effect=Exception("DB Error"))
    def test_upload_assignment_failure(self, mock_db):
        result = AssignmentService.upload_assignment("1", "Assignment 1", "/path/to/file.pdf")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
