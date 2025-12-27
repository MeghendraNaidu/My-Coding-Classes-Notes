import tkinter as tk
from tkinter import messagebox
from database import get_connection
from Services.auth_service import AuthService

class RegisterUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#1f1f1f")

        self.master = master
        self.db = get_connection()

        tk.Label(self, text="USER REGISTRATION", font=("Arial", 20, "bold"),
                 bg="#1f1f1f", fg="white").pack(pady=20)

        # NAME
        tk.Label(self, text="Full Name", bg="#1f1f1f", fg="white").pack(pady=5)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.pack(pady=5)

        # EMAIL
        tk.Label(self, text="Email", bg="#1f1f1f", fg="white").pack(pady=5)
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.pack(pady=5)

        # PASSWORD
        tk.Label(self, text="Password", bg="#1f1f1f", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.password_entry.pack(pady=5)

        # BUTTONS
        tk.Button(self, text="Register", width=20, height=2,
                  command=self.register_user).pack(pady=15)

        # tk.Button(self, text="Go to Login", width=20, height=2,
        #           command=lambda: master.switch_frame(LoginUI)).pack()
        
        tk.Button(self, text="Go to Login", width=20, height=2,
            command=self.go_to_login).pack()

    def go_to_login(self):
        from UI.login import LoginUI
        self.master.switch_frame(LoginUI)

    def register_user(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password_hash = self.password_entry.get().strip()

        # ------- VALIDATION (NO MERCY) -------
        if not name or not email or not password_hash:
            messagebox.showerror("Error", "All fields are required")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email format")
            return

        if len(password_hash) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        
        auth = AuthService()

        try:
            cursor = self.db.cursor()

            # Check if email exists
            cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Email already registered")
                return
            

            # Save user
            # cursor.execute(
            #     "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
            #     (name, email, password_hash)
            # )
            success = auth.register_user(name, email, password_hash)

            self.db.commit()

            messagebox.showinfo("Success", "Registration successful! Now login.")
            from UI.login import LoginUI

            self.master.switch_frame(LoginUI)

        except Exception as e:
            messagebox.showerror("Error", str(e))
