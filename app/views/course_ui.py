import tkinter as tk
from tkinter import messagebox, ttk

courses = []

def add_course():
    title = title_entry.get()
    desc = desc_entry.get()
    teacher = teacher_entry.get()
    if title and desc and teacher:
        courses.append((title, desc, teacher))
        tree.insert('', 'end', values=(title, desc, teacher))
        messagebox.showinfo("Success", "Course added.")
    else:
        messagebox.showerror("Error", "All fields required.")

root = tk.Tk()
root.title("Course Management")

tk.Label(root, text="Title").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Description").grid(row=1, column=0)
desc_entry = tk.Entry(root)
desc_entry.grid(row=1, column=1)

tk.Label(root, text="Teacher ID").grid(row=2, column=0)
teacher_entry = tk.Entry(root)
teacher_entry.grid(row=2, column=1)

tk.Button(root, text="Add Course", command=add_course).grid(row=3, column=1)

tree = ttk.Treeview(root, columns=("Title", "Description", "Teacher ID"), show="headings")
tree.heading("Title", text="Title")
tree.heading("Description", text="Description")
tree.heading("Teacher ID", text="Teacher ID")
tree.grid(row=4, column=0, columnspan=2)

root.mainloop()
