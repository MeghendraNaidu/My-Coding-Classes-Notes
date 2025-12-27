import tkinter as tk
from UI.login import LoginUI
from database import get_connection


class BankApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Bank Management System")
        self.geometry("600x400")
        self.resizable(False, False)

        self.db = get_connection()
        self.switch_frame(LoginUI)


    def switch_frame(self, frame_class, *args):
        new_frame = frame_class(self, *args)
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()

        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
    
