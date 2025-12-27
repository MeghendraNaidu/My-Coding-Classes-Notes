import tkinter as tk
from tkinter import messagebox, simpledialog
from Services.bank_service import BankService
from UI.login import LoginUI


class CustomerUI(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)

        self.master = master
        self.user = user
        self.bank = BankService()

        # Title
        tk.Label(self, text=f"Welcome, {user['name']}", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="View My Accounts", width=30, command=self.view_accounts).pack(pady=2)
        tk.Button(btn_frame, text="Deposit", width=30, command=self.deposit_ui).pack(pady=2)
        tk.Button(btn_frame, text="Withdraw", width=30, command=self.withdraw_ui).pack(pady=2)
        tk.Button(btn_frame, text="Transfer", width=30, command=self.transfer_ui).pack(pady=2)
        tk.Button(btn_frame, text="Transaction History", width=30, command=self.history_ui).pack(pady=2)
        tk.Button(btn_frame, text="Logout", width=30, bg="red", fg="white", command=lambda: master.switch_frame(LoginUI)).pack(pady=10)

        # Output Text box
        self.output = tk.Text(self, height=15, width=80)
        self.output.pack(pady=10)

    def view_accounts(self):
        self.output.delete("1.0", tk.END)
        accounts = self.bank.get_user_accounts(self.user["user_id"])
        if not accounts:
            self.output.insert(tk.END, "No accounts found.\n")
            return
        for acc in accounts:
            self.output.insert(tk.END,
                f"Account No: {acc['account_no']} | Type: {acc['account_type']} | "
                f"Balance: ₹{acc['balance']} | Status: {acc['status']}\n"
            )

    def deposit_ui(self):
        try:
            acc_no = simpledialog.askinteger("Deposit", "Enter account number:")
            amount = simpledialog.askfloat("Deposit", "Enter amount:")
            if not acc_no or not amount:
                return
            self.bank.deposit(acc_no, amount)
            messagebox.showinfo("Success", "Deposit successful")
            self.view_accounts()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def withdraw_ui(self):
        try:
            acc_no = simpledialog.askinteger("Withdraw", "Enter account number:")
            amount = simpledialog.askfloat("Withdraw", "Enter amount:")
            if not acc_no or not amount:
                return
            self.bank.withdraw(acc_no, amount)
            messagebox.showinfo("Success", "Withdraw successful")
            self.view_accounts()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transfer_ui(self):
        try:
            from_acc = simpledialog.askinteger("Transfer", "From Account Number:")
            to_acc = simpledialog.askinteger("Transfer", "To Account Number:")
            amount = simpledialog.askfloat("Transfer", "Enter amount:")
            if not from_acc or not to_acc or not amount:
                return
            if from_acc == to_acc:
                raise Exception("Cannot transfer to same account")
            self.bank.transfer(from_acc, to_acc, amount)
            messagebox.showinfo("Success", "Transfer successful")
            self.view_accounts()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def history_ui(self):
        self.output.delete("1.0", tk.END)
        acc_no = simpledialog.askinteger("History", "Enter Account Number:")
        if not acc_no:
            return
        history = self.bank.transaction_history(acc_no)
        if not history:
            self.output.insert(tk.END, "No transactions found.\n")
            return
        for txn in history:
            self.output.insert(tk.END,
                f"ID:{txn['transaction_id']} | From:{txn['from_account']} | "
                f"To:{txn['to_account']} | Amount:₹{txn['amount']} | "
                f"Type:{txn['transaction_type']} | Date:{txn['date']}\n"
            )
