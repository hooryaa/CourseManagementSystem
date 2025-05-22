import tkinter as tk
from tkinter import messagebox, simpledialog

courses = {}
students = {}

def add_course():
    cid = simpledialog.askstring("Input", "Enter Course ID:")
    title = simpledialog.askstring("Input", "Enter Course Title:")
    instructor = simpledialog.askstring("Input", "Enter Instructor Name:")
    if cid and title and instructor:
        courses[cid] = {"title": title, "instructor": instructor, "students": []}
        messagebox.showinfo("Success", f"Course '{title}' added successfully.")

def add_student():
    sid = simpledialog.askstring("Input", "Enter Student ID:")
    name = simpledialog.askstring("Input", "Enter Student Name:")
    if sid and name:
        students[sid] = {"name": name, "progress": {}}
        messagebox.showinfo("Success", f"Student '{name}' added successfully.")

def enroll_student():
    sid = simpledialog.askstring("Input", "Enter Student ID:")
    cid = simpledialog.askstring("Input", "Enter Course ID:")
    if sid in students and cid in courses:
        courses[cid]["students"].append(students[sid]["name"])
        messagebox.showinfo("Success", f"{students[sid]['name']} enrolled in {courses[cid]['title']}")
    else:
        messagebox.showerror("Error", "Invalid Student or Course ID")

def update_progress():
    sid = simpledialog.askstring("Input", "Enter Student ID:")
    cid = simpledialog.askstring("Input", "Enter Course ID:")
    progress = simpledialog.askinteger("Input", "Enter Progress (%)")
    if sid in students and cid in courses:
        students[sid]["progress"][cid] = progress
        messagebox.showinfo("Success", "Progress updated.")
    else:
        messagebox.showerror("Error", "Student or Course not found.")

def show_students():
    cid = simpledialog.askstring("Input", "Enter Course ID:")
    if cid in courses:
        names = "\n".join(courses[cid]["students"])
        messagebox.showinfo("Students", f"Students in {courses[cid]['title']}:\n{names}")
    else:
        messagebox.showerror("Error", "Course not found.")

def show_progress():
    sid = simpledialog.askstring("Input", "Enter Student ID:")
    if sid in students:
        data = students[sid]["progress"]
        msg = "\n".join([f"Course {cid}: {p}%" for cid, p in data.items()])
        messagebox.showinfo("Progress", msg or "No progress yet.")
    else:
        messagebox.showerror("Error", "Student not found.")

# Main UI window
root = tk.Tk()
root.title("Course Management System")
root.geometry("300x400")

tk.Button(root, text="Add Course", command=add_course).pack(pady=10)
tk.Button(root, text="Add Student", command=add_student).pack(pady=10)
tk.Button(root, text="Enroll Student", command=enroll_student).pack(pady=10)
tk.Button(root, text="Update Progress", command=update_progress).pack(pady=10)
tk.Button(root, text="Show Course Students", command=show_students).pack(pady=10)
tk.Button(root, text="Show Student Progress", command=show_progress).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
