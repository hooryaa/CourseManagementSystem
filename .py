import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class CourseManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Course Management System")
        self.root.geometry("500x400")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.create_enrollment_ui()
        self.create_assignment_ui()
        self.create_progress_ui()

    def create_enrollment_ui(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Student Enrollment')

        ttk.Label(frame, text="Name:").pack(pady=5)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.pack(pady=5)

        ttk.Label(frame, text="Email:").pack(pady=5)
        self.email_entry = ttk.Entry(frame)
        self.email_entry.pack(pady=5)

        ttk.Label(frame, text="Course:").pack(pady=5)
        self.course_entry = ttk.Entry(frame)
        self.course_entry.pack(pady=5)

        ttk.Button(frame, text="Enroll", command=self.enroll_student).pack(pady=10)

    def enroll_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        course = self.course_entry.get()
        if name and email and course:
            messagebox.showinfo("Success", f"{name} enrolled in {course}!")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def create_assignment_ui(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Assignment Upload')

        ttk.Label(frame, text="Assignment Title:").pack(pady=5)
        self.assignment_title = ttk.Entry(frame)
        self.assignment_title.pack(pady=5)

        ttk.Button(frame, text="Choose File", command=self.upload_file).pack(pady=10)
        self.file_label = ttk.Label(frame, text="No file chosen")
        self.file_label.pack(pady=5)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=f"Selected: {file_path.split('/')[-1]}")
            messagebox.showinfo("Uploaded", f"File uploaded successfully!")

    def create_progress_ui(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Progress Tracking')

        ttk.Label(frame, text="Course Progress:").pack(pady=10)
        self.progress = ttk.Progressbar(frame, length=300, value=60, mode='determinate')
        self.progress.pack(pady=10)

        ttk.Label(frame, text="60% Completed").pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = CourseManagementApp(root)
    root.mainloop()
