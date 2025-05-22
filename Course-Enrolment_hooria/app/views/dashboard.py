import tkinter as tk
import mysql.connector

def create_course():
    title = entry_title.get()
    description = entry_desc.get()
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="course_management"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (title, description) VALUES (%s, %s)", (title, description))
    conn.commit()
    cursor.close()
    conn.close()
    tk.messagebox.showinfo("Success", "Course Created")

def enroll_student():
    student_id = int(entry_student_id.get())
    course_id = int(entry_course_id.get())
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="course_management"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)", (student_id, course_id))
    conn.commit()
    cursor.close()
    conn.close()
    tk.messagebox.showinfo("Success", "Student Enrolled")

root = tk.Tk()
root.title("Dashboard")
# Course creation form
tk.Label(root, text="Course Title").pack()
entry_title = tk.Entry(root)
entry_title.pack()
tk.Label(root, text="Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()
tk.Button(root, text="Create Course", command=create_course).pack()

# Student enrollment form
tk.Label(root, text="Student ID").pack()
entry_student_id = tk.Entry(root)
entry_student_id.pack()
tk.Label(root, text="Course ID").pack()
entry_course_id = tk.Entry(root)
entry_course_id.pack()
tk.Button(root, text="Enroll Student", command=enroll_student).pack()

root.mainloop()