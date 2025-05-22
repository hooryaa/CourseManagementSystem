import tkinter as tk
from tkinter import messagebox
from app.services.auth import login_user

def login_window():
    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        role = var_role.get()
        if login_user(username, password, role):
            messagebox.showinfo("Success", f"Logged in as {role}")
        else:
            messagebox.showerror("Error", "Invalid credentials")

    window = tk.Tk()
    window.title("Login")

    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Label(window, text="Role").pack()
    var_role = tk.StringVar(window)
    var_role.set("Admin")
    tk.OptionMenu(window, var_role, "Admin", "Teacher", "Student").pack()

    tk.Button(window, text="Login", command=handle_login).pack()

    window.mainloop()

if __name__ == "__main__":
    login_window()
