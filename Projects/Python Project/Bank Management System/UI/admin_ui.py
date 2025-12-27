import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.ttk as ttk
from database import get_connection
from UI.login import LoginUI


class AdminUI(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.master = master
        self.user = user
        self.db = get_connection()

        tk.Label(self, text=f"Welcome {user['name']} (ADMIN)", font=("Arial", 16, "bold")).pack(pady=10)

        # Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tabs
        self.accounts_tab = tk.Frame(self.notebook)
        self.transactions_tab = tk.Frame(self.notebook)

        self.notebook.add(self.accounts_tab, text="Accounts")
        self.notebook.add(self.transactions_tab, text="Transactions")
        
        self.setup_accounts_tab()
        self.setup_transactions_tab()

        self.audit_tab = tk.Frame(self.notebook)
        self.notebook.add(self.audit_tab, text="Audit Log")
        self.setup_audit_tab()
        
    # ------------------ ACCOUNTS TAB ------------------
    def setup_accounts_tab(self):

        # Buttons
        btn_frame = tk.Frame(self.accounts_tab)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Create Account", width=18,
                  command=self.create_account).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(btn_frame, text="Delete Account", width=18,
                  command=self.delete_account).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(btn_frame, text="Deposit", width=18,
                  command=self.deposit_btn).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(btn_frame, text="Withdraw", width=18,
                  command=self.withdraw_btn).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(btn_frame, text="Refresh", width=18,
                  command=self.load_accounts).grid(row=2, column=0, columnspan=2, pady=5)
        # Add Logout button inside Accounts tab
        tk.Button(btn_frame, text="Logout", bg="red", fg="white", width=18,
                  command=lambda: self.master.switch_frame(LoginUI)).grid(row=3, column=0, columnspan=2, pady=10)

        
        tk.Button(self.transactions_tab, text="Generate Statement", command=self.generate_statement).pack(pady=5)


        # Table
        self.accounts_tree = ttk.Treeview(self.accounts_tab, columns=("Account No", "User ID", "Balance"))
        self.accounts_tree.column("#0", width=0, stretch=tk.NO)

        for col in ("Account No", "User ID", "Balance"):
            self.accounts_tree.column(col, anchor=tk.CENTER, width=150)
            self.accounts_tree.heading(col, text=col, anchor=tk.CENTER)

        self.accounts_tree.pack(fill=tk.BOTH, expand=True)

        self.load_accounts()

    def load_accounts(self):
        for item in self.accounts_tree.get_children():
            self.accounts_tree.delete(item)

        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT account_no, user_id, balance FROM accounts ORDER BY account_no")
        for row in cursor.fetchall():
            self.accounts_tree.insert('', tk.END,
                                      values=(row['account_no'], row['user_id'], float(row['balance'])))

    # ------------------ CREATE ACCOUNT ------------------
    def create_account(self):
        top = tk.Toplevel(self)
        top.title("Create Account")

        tk.Label(top, text="User ID").pack(pady=5)
        user_id_entry = tk.Entry(top)
        user_id_entry.pack()

        tk.Label(top, text="Initial Balance").pack(pady=5)
        balance_entry = tk.Entry(top)
        balance_entry.pack()

        def save():
            user_id = user_id_entry.get()
            balance = balance_entry.get()

            if not user_id.isdigit():
                messagebox.showerror("Error", "User ID must be a number")
                return

            try:
                balance = float(balance)
                if balance < 0:
                    raise ValueError
            except:
                messagebox.showerror("Error", "Invalid balance")
                return

            try:
                cursor = self.db.cursor()
                cursor.execute(
                    "INSERT INTO accounts (user_id, balance) VALUES (%s, %s)",
                    (user_id, balance)
                )
                self.db.commit()
                messagebox.showinfo("Success", "Account created")
                top.destroy()
                self.load_accounts()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(top, text="Create", command=save).pack(pady=10)

    # ------------------ DEPOSIT ------------------
    def deposit_btn(self):
        acc = simpledialog.askinteger("Deposit", "Enter account number:")
        amt = simpledialog.askfloat("Deposit", "Enter amount:")

        if not acc or not amt or amt <= 0:
            return

        cursor = self.db.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc,))
        row = cursor.fetchone()

        if not row:
            messagebox.showerror("Error", "Account not found")
            return

        new_balance = float(row[0]) + amt
        cursor.execute("UPDATE accounts SET balance=%s WHERE account_no=%s", (new_balance, acc))
        self.db.commit()

        messagebox.showinfo("Success", f"Deposited ₹{amt}")
        self.load_accounts()

    # ------------------ WITHDRAW ------------------
    def withdraw_btn(self):
        acc = simpledialog.askinteger("Withdraw", "Enter account number:")
        amt = simpledialog.askfloat("Withdraw", "Enter amount:")

        if not acc or not amt or amt <= 0:
            return

        cursor = self.db.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc,))
        row = cursor.fetchone()

        if not row:
            messagebox.showerror("Error", "Account not found")
            return

        if amt > float(row[0]):
            messagebox.showerror("Error", "Insufficient balance")
            return

        new_balance = float(row[0]) - amt
        cursor.execute("UPDATE accounts SET balance=%s WHERE account_no=%s", (new_balance, acc))
        self.db.commit()

        messagebox.showinfo("Success", f"Withdrawn ₹{amt}")
        self.load_accounts()

    # ------------------ DELETE ------------------
    def delete_account(self):
        acc = simpledialog.askinteger("Delete", "Enter account number:")
        if not acc:
            return

        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc,))
        row = cursor.fetchone()

        if not row:
            messagebox.showerror("Error", "Account not found")
            return

        if float(row["balance"]) != 0:
            messagebox.showerror("Error", "Balance must be zero")
            return

        cursor.execute("DELETE FROM transactions WHERE from_account=%s OR to_account=%s", (acc, acc))
        cursor.execute("DELETE FROM accounts WHERE account_no=%s", (acc,))
        self.db.commit()

        messagebox.showinfo("Success", "Account deleted")
        self.load_accounts()

    # ------------------ TRANSACTION TAB ------------------
    def setup_transactions_tab(self):

        self.txn_tree = ttk.Treeview(self.transactions_tab, columns=(
            "ID", "From", "To", "Type", "Amount", "Date"))

        self.txn_tree.column("#0", width=0, stretch=tk.NO)

        for col in ("ID", "From", "To", "Type", "Amount", "Date"):
            self.txn_tree.column(col, anchor=tk.CENTER, width=140)
            self.txn_tree.heading(col, text=col)

        self.txn_tree.pack(fill=tk.BOTH, expand=True)

        self.load_transactions()

    def load_transactions(self):
        for item in self.txn_tree.get_children():
            self.txn_tree.delete(item)

        cursor = self.db.cursor(dictionary=True)
        cursor.execute("""
            SELECT transaction_id, from_account, to_account,
                   transaction_type, amount, date
            FROM transactions
            ORDER BY date DESC
        """)

        for row in cursor.fetchall():
            self.txn_tree.insert('', tk.END, values=(
                row['transaction_id'],
                row['from_account'],
                row['to_account'],
                row['transaction_type'],
                float(row['amount']),
                row['date']
            ))
            
    def log_action(self, action, target=""):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO admin_actions (admin_name, action, target) VALUES (%s,%s,%s)",
            (self.user["name"], action, target)
        )
        self.db.commit()
        
    def setup_audit_tab(self):
        self.audit_tree = ttk.Treeview(self.audit_tab)

        self.audit_tree['columns'] = ("ID", "Admin", "Action", "Target", "Date")
        self.audit_tree.column("#0", width=0, stretch=tk.NO)

        for col in self.audit_tree['columns']:
            self.audit_tree.heading(col, text=col)
            self.audit_tree.column(col, anchor=tk.CENTER, width=150)

        self.audit_tree.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.audit_tab, text="Refresh", command=self.load_audit).pack(pady=5)

        self.load_audit()
        
    def load_audit(self):
        for i in self.audit_tree.get_children():
            self.audit_tree.delete(i)

        cursor = self.db.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, admin_name, action, target, created_at
            FROM admin_actions
            ORDER BY created_at DESC
        """)

        for row in cursor.fetchall():
            self.audit_tree.insert('', tk.END, values=(
                row["id"],
                row["admin_name"],
                row["action"],
                row["target"],
                row["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            ))
            
    def generate_statement(self):
        acc_no = simpledialog.askinteger("Statement", "Enter Account Number:")
        if not acc_no:
            return

        cursor = self.db.cursor(dictionary=True)
        cursor.execute("""
            SELECT transaction_id, from_account, to_account, transaction_type, amount, date
            FROM transactions
            WHERE from_account = %s OR to_account = %s
            ORDER BY date DESC
        """, (acc_no, acc_no))

        data = cursor.fetchall()

        if not data:
            messagebox.showinfo("No Data", "No transactions for this account")
            return

        win = tk.Toplevel(self)
        win.title(f"Statement - Account {acc_no}")
        win.geometry("800x400")

        tree = ttk.Treeview(win)
        tree["columns"] = ("ID","From","To","Type","Amount","Date")
        tree.column("#0", width=0, stretch=tk.NO)

        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER, width=130)

        tree.pack(fill=tk.BOTH, expand=True)

        for row in data:
            tree.insert('', tk.END, values=(
                row["transaction_id"],
                row["from_account"],
                row["to_account"],
                row["transaction_type"],
                row["amount"],
                row["date"].strftime("%Y-%m-%d %H:%M:%S")
            ))





