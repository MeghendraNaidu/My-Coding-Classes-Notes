import tkinter as tk
from tkinter import messagebox
import mysql.connector



conn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "1234", 
    port = "3306", 
    database = "practice", 
    autocommit = False
)

cur = conn.cursor()

def user_details():
    try:
        username = usname.get()
        password = uspass.get()
        
        query = "select * from User_details where username = %s and password = %s"
        cur.execute(query, (username, password))
        result = cur.fetchone()
        
        if result:
            messagebox.showinfo("Login Successful")
        else:
            messagebox.showerror("Failed", "Invalid Username or Password")
            
    except mysql.connector.Error as err:
        messagebox.showerror("Query Error", f"Something went wrong:\n{err}")
        
            
            
root = tk.Tk()

root.title("Check User Details")
root.geometry("500x500")

tk.Label(root, text = "Welcome To Login Page", font = ("Times New Roman", 20)).pack()

frame = tk.Frame(root, bd = 5, height = 200, width = 200)
frame.pack(pady = 30)

tk.Label(frame, text = "Username : ", font = ("Times New Roman", 16)).grid(row = 0, column = 0, pady = 5, padx = 10)
usname = tk.Entry(frame)
usname.grid(row = 0, column = 1, pady = 5, padx = 10)

tk.Label(frame, text = "Password : ", font = ("Times New Roman", 16)).grid(row = 1, column = 0, pady = 5, padx = 10)
uspass = tk.Entry(frame, show = "@")
uspass.grid(row = 1, column = 1, pady = 5, padx = 10)

frame1 = tk.Frame(root, bd = 5, height = 200, width = 200)
frame1.pack(pady = 30)

tk.Button(frame1, text = "Check", command = user_details).grid(row = 0, column = 0, pady = 10,  padx = 10)


root.mainloop()