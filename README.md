# 🎓 Course Management System (Tkinter + MySQL)

A modular Python desktop application for managing courses and user access using **Tkinter** for the GUI and **MySQL** as the backend database. Designed with clean architecture, role-based authentication, and unit test coverage, this system enables seamless login, course creation, and student enrollment.

---

## 🧱 Project Structure
<pre lang="markdown">
```
CourseManagementSystem/
│
├── app/ # Application logic
│ ├── models/ # Data models
│ │ ├── user.py # User model with role handling
│ │ ├── course.py # Course model
│ │ └── enrollment.py # Enrollment model
│ │
│ ├── services/ # Business logic
│ │ └── auth.py # Authentication service
│ │
│ ├── views/ # Tkinter GUI views
│ │ ├── login.py # Login screen
│ │ └── dashboard.py # Dashboard for managing courses and enrollments
│
├── tests/ # Unit tests
│ ├── test_views/
│ │ ├── test_login.py
│ │ └── test_dashboard.py
│ └── test_services/
│ └── test_auth.py
│
├── sql/
│ └── course_management.sql # MySQL schema and seed data
│
└── README.md # Project documentation
```
</pre>    


---

## 👤 Responsibilities

### ✅ Hooria - Login & Authentication & Course & Enrollment

- Developed secure login form (`views/login.py`)
- Implemented role-based authentication logic (`services/auth.py`)
- Built user model for DB interaction (`models/user.py`)
- Added unit tests for login flow and auth logic
- Created dashboard UI for managing courses (`views/dashboard.py`)
- Defined data models for Course and Enrollment
- Established DB structure for many-to-one relations (students → courses)
- Wrote unit tests for dashboard features and model interactions

---

## 🛠️ Technologies Used

- Python 3.11  
- Tkinter – for GUI development  
- MySQL – for database storage  
- unittest – for testing  
- mysql-connector-python – for DB connectivity  

---

## 🗄️ Database Schema

SQL setup file (`sql/course_management.sql`) includes:

- `users` table with roles (`admin`, `teacher`, `student`)
- `courses` table for class offerings
- `enrollments` linking users to courses

### Sample schema:

```sql
CREATE DATABASE IF NOT EXISTS course_management;

USE course_management;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin', 'teacher', 'student') NOT NULL
);

CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    description TEXT
);

CREATE TABLE IF NOT EXISTS enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin');
