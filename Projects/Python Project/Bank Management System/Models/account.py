class Account:
    def __init__(self, account_no, user_id, balance, account_type, status):
        self.account_no = account_no
        self.user_id = user_id
        self.balance = balance
        self.account_type = account_type
        self.status = status

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance")
        self.balance -= amount
