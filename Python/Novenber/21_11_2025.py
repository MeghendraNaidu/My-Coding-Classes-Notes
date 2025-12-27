import tkinter as tk
import csv
from tkinter import filedialog, messagebox
import mysql.connector


conn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "1234", 
    database = "practice", 
    autocommit = False
)

print(conn.is_connected())
cursor = conn.cursor()



def upload_csv_function():
    filename = filedialog.askopenfilename(filetypes = [("CSV FILES", "*.csv")])
    
    with open(filename, "r") as f:
        data = csv.reader(f)
        next(data)
        
        for row in data:
            # Insert into database
            cursor.execute(
                '''INSERT INTO STUDENTS (NAME , AGE, CLASS, GRADE) 
                    VALUES (%s, %s, %s, %s)
                ''', (row)
            )
        conn.commit()
        
    messagebox.showinfo("Success", "Data has Been Inserted Into DataBase")
    
def show_data_grid():
    data_grid.configure(state = tk.NORMAL)
    data_grid.delete("1.0", tk.END)
    cursor.execute('SELECT * FROM STUDENTS')
    # print(cursor.fetchall())
    
    for row in cursor.fetchall():
        data_grid.insert(tk.END, f'ID: {row[0]}, NAME: {row[1]}, AGE: {row[2]}, CLASS: {row[3]}, GRADE: {row[4]}\n')
    
    data_grid.configure(state = tk.DISABLED)
        
def add():
    name = name_entry.get()
    age = age_entry.get()
    class_ = class_entry.get()
    grade = grade_entry.get()
    
    if name and age and class_ and grade:
        cursor.execute(
            '''INSERT INTO STUDENTS (NAME, AGE, CLASS, GRADE)
            VALUES (%s, %s, %s, %s)
            ''', (name, age, class_, grade)
        )
        conn.commit()
        messagebox.showinfo("info", "Data Has Been Inserted Successfully")
        show_data_grid()
    else:
        messagebox.showwarning("warning", "Please Enter Valid Details")    
    

def update():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    class_ = class_entry.get()
    grade = grade_entry.get()
    
    if id and name and age and class_ and grade:
        cursor.execute(
            '''UPDATE  STUDENTS SET  NAME = %s, AGE = %s, CLASS = %s, GRADE = %s 
            WHERE ID = %s 
            ''', (name, age, class_, grade, id)
        )
        conn.commit()
        messagebox.showinfo("Info", "Data Has Been Updated")
        show_data_grid()
    else:
        messagebox.showwarning("Warning", "Please Enter a Valid ID to Update Data")

def delete():
    id = id_entry.get()
    
    if id:
        cursor.execute(
            '''DELETE FROM STUDENTS WHERE ID = %s''', (id, )
        )
        conn.commit()
        messagebox.showinfo("Info", "Data Has Been Deleted")
        show_data_grid()
    else:
        messagebox.showwarning("Warning", "Please Enter a Valid ID to Delete Data")

root = tk.Tk()
root.geometry("500x500")



tk.Button(root, text = "Upload CSV", command = upload_csv_function).pack(pady = 20)

data_grid = tk.Text(root, width = 55, height =15)
data_grid.pack()

actions_frame = tk.Frame(root)
actions_frame.pack(pady = 25)

id_label = tk.Label(actions_frame, text = "ID")
id_label.grid(row = 0, column = 0)
id_entry = tk.Entry(actions_frame, width = 5)
id_entry.grid(row = 0, column = 1)

name_label = tk.Label(actions_frame, text = "NAME")
name_label.grid(row = 0, column = 2)
name_entry = tk.Entry(actions_frame, width = 9)
name_entry.grid(row = 0, column = 3)

age_label = tk.Label(actions_frame, text = "AGE")
age_label.grid(row = 0, column = 4)
age_entry = tk.Entry(actions_frame, width = 5)
age_entry.grid(row = 0, column = 5)

class_label = tk.Label(actions_frame, text = "CLASS")
class_label.grid(row = 0, column = 6)
class_entry = tk.Entry(actions_frame, width = 5)
class_entry.grid(row = 0, column = 7)

grade_label = tk.Label(actions_frame, text = "GRADE")
grade_label.grid(row = 0, column = 8)
grade_entry = tk.Entry(actions_frame, width = 5)
grade_entry.grid(row = 0, column = 9)

tk.Button(actions_frame, text = "ADD", command = add).grid(row = 1, column = 2, pady = 25)
tk.Button(actions_frame, text = "UPDATE", command = update).grid(row = 1, column = 4, pady = 25)
tk.Button(actions_frame, text = "DELETE", command = delete).grid(row = 1, column = 7, pady = 25)



show_data_grid()



root.mainloop()