 Student Enrollment – Overview
✅ Description
Student enrollment is the process of assigning students to courses. Only authenticated users with the student role can view available courses and request enrollment. Admins or instructors can approve/reject enrollments.

📁 Location
Copy
Edit
app/
├── models/
│   └── enrollment.py
├── views/
│   └── dashboard.py
🧠 Responsibilities by IQRA IQBAL
Students can:

View available courses

Enroll in selected courses

Instructors/Admins can:

View enrolled students

Approve or remove students from a course

📊 MySQL Table: enrollments
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    progress INT DEFAULT 0,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
📈 Progress Tracking – Overview
✅ Description
Tracks how far a student has progressed through a course. It’s updated manually by the instructor or automatically when students complete lessons/quizzes.

🧠 Responsibilities
Students can:

View their own progress per course

Instructors/Admins can:

Update progress percentage (0–100%)

🧩 Table Column in enrollments
progress INT DEFAULT 0 → Percentage of course completed by student

🧩 Models: enrollment.py
python
Copy
Edit
# app/models/enrollment.py

class Enrollment:
    def __init__(self, db):
        self.db = db

    def enroll_student(self, user_id, course_id):
        cursor = self.db.cursor()
        query = """
        INSERT INTO enrollments (user_id, course_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, course_id))
        self.db.commit()

    def get_enrollments_by_user(self, user_id):
        cursor = self.db.cursor(dictionary=True)
        query = """
        SELECT e.id, c.name AS course_name, e.progress, e.status
        FROM enrollments e
        JOIN courses c ON e.course_id = c.id
        WHERE e.user_id = %s
        """
        cursor.execute(query, (user_id,))
        return cursor.fetchall()

    def update_progress(self, enrollment_id, progress):
        cursor = self.db.cursor()
        query = """
        UPDATE enrollments SET progress = %s
        WHERE id = %s
        """
        cursor.execute(query, (progress, enrollment_id))
        self.db.commit()
✅ Sample DDL for Related Tables
🧑 users table
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('student', 'instructor', 'admin') NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
📚 courses table
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_by INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);
