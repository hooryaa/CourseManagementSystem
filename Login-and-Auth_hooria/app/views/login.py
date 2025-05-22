import tkinter as tk
from tkinter import messagebox
from app.services.auth import authenticate

def login():
    username = entry_username.get()
    password = entry_password.get()
    role = authenticate(username, password)
    if role:
        messagebox.showinfo("Login Success", f"Logged in as {role}")
    else:
        messagebox.showerror("Error", "Invalid credentials")

root = tk.Tk()
root.title("Login")
tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()
tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()
tk.Button(root, text="Login", command=login).pack()
root.mainloop()