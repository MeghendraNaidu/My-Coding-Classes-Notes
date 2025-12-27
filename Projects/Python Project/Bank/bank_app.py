# bank_app.py
import bcrypt
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, simpledialog
from decimal import Decimal
import random
import string
import threading

# ---------- CONFIG ----------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'bank_system',
    'autocommit': True
}
# ----------------------------

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ---------- Utilities ----------
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, pw_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), pw_hash)

def generate_account_no():
    return ''.join(random.choices(string.digits, k=12))

# ---------- Data Access Layer ----------
class DB:
    def __init__(self):
        self.conn = get_db_connection()

    def fetchone(self, query, params):
        cur = self.conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        cur.close()
        return row

    def fetchall(self, query, params):
        cur = self.conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        return rows

    def execute(self, query, params):
        cur = self.conn.cursor()
        cur.execute(query, params)
        lastid = cur.lastrowid
        cur.close()
        return lastid

    def commit(self):
        self.conn.commit()

# ---------- Models ----------
class User:
    def __init__(self, db: DB, id=None, username=None, password_hash=None, full_name=None):
        self.db = db
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.full_name = full_name

    @classmethod
    def register(cls, db: DB, username: str, password: str, full_name: str = None):
        # check exists
        exists = db.fetchone("SELECT id FROM users WHERE username=%s", (username,))
        if exists:
            raise ValueError("Username already taken.")
        pw_hash = hash_password(password)
        db.execute("INSERT INTO users (username, password_hash, full_name) VALUES (%s,%s,%s)",
                   (username, pw_hash, full_name))
        db.commit()
        row = db.fetchone("SELECT id, username, password_hash, full_name FROM users WHERE username=%s", (username,))
        return cls(db, id=row[0], username=row[1], password_hash=row[2], full_name=row[3])

    @classmethod
    def login(cls, db: DB, username: str, password: str):
        row = db.fetchone("SELECT id, username, password_hash, full_name FROM users WHERE username=%s", (username,))
        if not row:
            return None
        uid, uname, pw_hash, full = row
        if verify_password(password, pw_hash.encode('utf-8') if isinstance(pw_hash, str) else pw_hash):
            return cls(db, id=uid, username=uname, password_hash=pw_hash, full_name=full)
        return None

class Account:
    def __init__(self, db: DB, id, user_id, account_no, balance, account_type):
        self.db = db
        self.id = id
        self.user_id = user_id
        self.account_no = account_no
        self.balance = Decimal(balance)
        self.account_type = account_type

    @classmethod
    def create_for_user(cls, db: DB, user_id: int, account_type='savings'):
        acct_no = generate_account_no()
        db.execute("INSERT INTO accounts (user_id, account_no, balance, account_type) VALUES (%s,%s,%s,%s)",
                   (user_id, acct_no, Decimal('0.00'), account_type))
        db.commit()
        row = db.fetchone("SELECT id, user_id, account_no, balance, account_type FROM accounts WHERE account_no=%s", (acct_no,))
        return cls(db, *row)

    @classmethod
    def get_by_user(cls, db: DB, user_id: int):
        rows = db.fetchall("SELECT id, user_id, account_no, balance, account_type FROM accounts WHERE user_id=%s", (user_id,))
        return [cls(db, *r) for r in rows]

    @classmethod
    def get_by_account_no(cls, db: DB, acct_no: str):
        row = db.fetchone("SELECT id, user_id, account_no, balance, account_type FROM accounts WHERE account_no=%s", (acct_no,))
        if not row:
            return None
        return cls(db, *row)

    def deposit(self, amount: Decimal, note=None):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        new_balance = self.balance + Decimal(amount)
        self.db.execute("UPDATE accounts SET balance=%s WHERE id=%s", (str(new_balance), self.id))
        self.db.execute("INSERT INTO transactions (account_id, type, amount, note) VALUES (%s,%s,%s,%s)",
                        (self.id, 'deposit', str(amount), note))
        self.db.commit()
        self.balance = new_balance

    def withdraw(self, amount: Decimal, note=None):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.balance < Decimal(amount):
            raise ValueError("Insufficient balance.")
        new_balance = self.balance - Decimal(amount)
        self.db.execute("UPDATE accounts SET balance=%s WHERE id=%s", (str(new_balance), self.id))
        self.db.execute("INSERT INTO transactions (account_id, type, amount, note) VALUES (%s,%s,%s,%s)",
                        (self.id, 'withdraw', str(amount), note))
        self.db.commit()
        self.balance = new_balance

    def transfer_to(self, target_account_no: str, amount: Decimal, note=None):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.balance < Decimal(amount):
            raise ValueError("Insufficient balance.")
        target = Account.get_by_account_no(self.db, target_account_no)
        if not target:
            raise ValueError("Target account not found.")

        # Simple transactional approach - note: for production use DB transactions
        new_balance_self = self.balance - Decimal(amount)
        new_balance_target = target.balance + Decimal(amount)

        # Update balances
        self.db.execute("UPDATE accounts SET balance=%s WHERE id=%s", (str(new_balance_self), self.id))
        self.db.execute("UPDATE accounts SET balance=%s WHERE id=%s", (str(new_balance_target), target.id))

        # Insert transaction records
        self.db.execute("INSERT INTO transactions (account_id, type, amount, note, related_account) VALUES (%s,%s,%s,%s,%s)",
                        (self.id, 'transfer_out', str(amount), note, target.account_no))
        self.db.execute("INSERT INTO transactions (account_id, type, amount, note, related_account) VALUES (%s,%s,%s,%s,%s)",
                        (target.id, 'transfer_in', str(amount), note, self.account_no))
        self.db.commit()

        self.balance = new_balance_self
        target.balance = new_balance_target

    def transactions(self, limit=50):
        rows = self.db.fetchall("SELECT id, type, amount, note, created_at, related_account FROM transactions WHERE account_id=%s ORDER BY created_at DESC LIMIT %s",
                                (self.id, limit))
        return rows

# ---------- GUI ----------
class BankApp:
    def __init__(self, root):
        self.db = DB()
        self.root = root
        self.root.title("Bank Management System")
        self.current_user = None
        self.current_accounts = []

        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack()

        self.show_login_screen()

    def clear(self):
        for w in self.main_frame.winfo_children():
            w.destroy()

    def show_login_screen(self):
        self.clear()
        tk.Label(self.main_frame, text="Login", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(self.main_frame, text="Username").grid(row=1, column=0, sticky='e')
        tk.Label(self.main_frame, text="Password").grid(row=2, column=0, sticky='e')

        self.username_var = tk.Entry(self.main_frame)
        self.password_var = tk.Entry(self.main_frame, show='*')
        self.username_var.grid(row=1, column=1)
        self.password_var.grid(row=2, column=1)

        tk.Button(self.main_frame, text="Login", command=self.login).grid(row=3, column=0, pady=10)
        tk.Button(self.main_frame, text="Register", command=self.show_register_screen).grid(row=3, column=1, pady=10)

    def show_register_screen(self):
        self.clear()
        tk.Label(self.main_frame, text="Register", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(self.main_frame, text="Username").grid(row=1, column=0, sticky='e')
        tk.Label(self.main_frame, text="Password").grid(row=2, column=0, sticky='e')
        tk.Label(self.main_frame, text="Full name").grid(row=3, column=0, sticky='e')

        self.reg_username = tk.Entry(self.main_frame)
        self.reg_password = tk.Entry(self.main_frame, show='*')
        self.reg_fullname = tk.Entry(self.main_frame)
        self.reg_username.grid(row=1, column=1)
        self.reg_password.grid(row=2, column=1)
        self.reg_fullname.grid(row=3, column=1)

        tk.Button(self.main_frame, text="Create", command=self.register).grid(row=4, column=0, pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_login_screen).grid(row=4, column=1, pady=10)

    def register(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        fullname = self.reg_fullname.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "Username and password required.")
            return
        try:
            user = User.register(self.db, username, password, fullname)
            messagebox.showinfo("Success", f"User {user.username} registered. Please login.")
            self.show_login_screen()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        user = User.login(self.db, username, password)
        if not user:
            messagebox.showerror("Error", "Invalid credentials.")
            return
        self.current_user = user
        self.load_accounts()
        self.show_dashboard()

    def load_accounts(self):
        self.current_accounts = Account.get_by_user(self.db, self.current_user.id)

    def show_dashboard(self):
        self.clear()
        tk.Label(self.main_frame, text=f"Welcome, {self.current_user.full_name or self.current_user.username}", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=5)
        tk.Button(self.main_frame, text="Create Account", command=self.create_account_dialog).grid(row=1, column=0, pady=5)
        tk.Button(self.main_frame, text="Logout", command=self.logout).grid(row=1, column=2, pady=5)

        self.accounts_frame = tk.Frame(self.main_frame)
        self.accounts_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.render_accounts()

    def render_accounts(self):
        for w in self.accounts_frame.winfo_children():
            w.destroy()
        for idx, acct in enumerate(self.current_accounts):
            frame = tk.LabelFrame(self.accounts_frame, text=f"Account: {acct.account_no}", padx=6, pady=6)
            frame.grid(row=idx, column=0, padx=5, pady=5, sticky='w')
            tk.Label(frame, text=f"Type: {acct.account_type}").grid(row=0, column=0, sticky='w')
            tk.Label(frame, text=f"Balance: {acct.balance}").grid(row=1, column=0, sticky='w')
            tk.Button(frame, text="Deposit", command=lambda a=acct: self.deposit_dialog(a)).grid(row=0, column=1)
            tk.Button(frame, text="Withdraw", command=lambda a=acct: self.withdraw_dialog(a)).grid(row=1, column=1)
            tk.Button(frame, text="Transfer", command=lambda a=acct: self.transfer_dialog(a)).grid(row=2, column=1)
            tk.Button(frame, text="History", command=lambda a=acct: self.show_history(a)).grid(row=3, column=1)

    def create_account_dialog(self):
        acct_type = simpledialog.askstring("Account Type", "Enter account type (savings/current):", initialvalue="savings")
        if not acct_type:
            return
        try:
            acct = Account.create_for_user(self.db, self.current_user.id, acct_type)
            self.load_accounts()
            self.render_accounts()
            messagebox.showinfo("Created", f"Created account {acct.account_no}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def deposit_dialog(self, account: Account):
        amt = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amt is None:
            return
        try:
            account.deposit(Decimal(str(amt)))
            self.load_accounts()
            self.render_accounts()
            messagebox.showinfo("Success", "Deposit completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def withdraw_dialog(self, account: Account):
        amt = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amt is None:
            return
        try:
            account.withdraw(Decimal(str(amt)))
            self.load_accounts()
            self.render_accounts()
            messagebox.showinfo("Success", "Withdrawal completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transfer_dialog(self, account: Account):
        target = simpledialog.askstring("Transfer", "Enter target account number:")
        if not target:
            return
        amt = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
        if amt is None:
            return
        try:
            account.transfer_to(target, Decimal(str(amt)))
            self.load_accounts()
            self.render_accounts()
            messagebox.showinfo("Success", "Transfer completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_history(self, account: Account):
        trans = account.transactions(limit=100)
        txt = ""
        for t in trans:
            tid, ttype, amount, note, created_at, related = t
            txt += f"{created_at} | {ttype} | {amount} | {note or ''} | related: {related or ''}\n"
        top = tk.Toplevel(self.root)
        top.title(f"History {account.account_no}")
        tk.Text(top, width=80, height=20).pack()
        tk.Text(top).insert('1.0', txt)
        # simpler way: use messagebox for short or create Text widget properly

    def logout(self):
        self.current_user = None
        self.current_accounts = []
        self.show_login_screen()

def run_app():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
