import tkinter as tk
from UI.customer_ui import CustomerUI
from UI.admin_ui import AdminUI
from UI.login import LoginUI


class DashboardUI(tk.Frame):

    def __init__(self, master, user):
        super().__init__(master)

        self.user = user

        tk.Label(self, text=f"Welcome, {user['name']}", font=("Arial", 16)).pack(pady=20)

        if user["role"] == "admin":
            tk.Button(self, text="Admin Panel", width=25,
                      command=lambda: master.switch_frame(AdminUI, user)).pack(pady=10)
        else:
            tk.Button(self, text="Customer Panel", width=25,
                      command=lambda: master.switch_frame(CustomerUI, user)).pack(pady=10)

        tk.Button(self, text="Logout", width=25,
                  command=lambda: master.switch_frame(LoginUI)).pack(pady=10)
