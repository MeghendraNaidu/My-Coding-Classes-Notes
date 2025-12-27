import tkinter as tk
from tkinter import messagebox
from Services.auth_service import AuthService


class LoginUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)


        tk.Label(self, text="BANK LOGIN", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.auth = AuthService()
        self.pass_entry = tk.Entry(self, show="*", width=30)
        self.pass_entry.pack(pady=5)

        tk.Button(self, text="Login", width=15, command=self.login_user).pack(pady=20)
        
        # tk.Button(self, text="New User? Register Here",
        #   width=20,
        #   command=lambda: master.switch_frame(RegisterUI)).pack(pady=10)
        
        tk.Button(self, text="New User? Register Here",
              width=20,
              command=self.go_to_register).pack(pady=10)
        
    def go_to_register(self):
        from UI.register import RegisterUI
        self.master.switch_frame(RegisterUI)


    def login_user(self):
        from UI.dashboard import DashboardUI
        from UI.admin_ui import AdminUI 
        
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Email and Password required")
            return

        user = self.auth.login(email, password)

        if not user:
            messagebox.showerror("Error", "Invalid credentials")
            return

        messagebox.showinfo("Success", "Login successful")

        # ✅ Correct role routing + pass user object
        if user["role"] == "admin":
            self.master.switch_frame(AdminUI, user)
        else:
            self.master.switch_frame(DashboardUI, user)
