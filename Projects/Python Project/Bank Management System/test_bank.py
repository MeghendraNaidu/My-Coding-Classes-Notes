from Services.auth_service import AuthService
from Services.bank_service import BankService

auth = AuthService()
bank = BankService()

print("\n===== REGISTER USERS =====")

# Register Admin
auth.register_user("Admin User", "admin@mail.com", "admin123", role="admin")

# Register Customer
auth.register_user("Test User", "test@mail.com", "1234", role="customer")

print("\n===== LOGIN TEST =====")

# Login as Admin
admin = auth.login("admin@mail.com", "admin123")
print("Admin:", admin)

# Login as Customer
user = auth.login("test@mail.com", "1234")
print("Customer:", user)

if not user:
    print("Login failed. Fix your auth_service before doing anything else.")
    exit()

print("\n===== CREATE ACCOUNTS =====")

# Create account for customer
bank.create_account(user["user_id"], "savings")

# (Optional) second account to test transfer properly
bank.create_account(user["user_id"], "current")

print("\n===== DEPOSIT =====")

# Get account numbers from database or assume order
account_1 = 1
account_2 = 2

bank.deposit(account_1, 10000)

print("\n===== WITHDRAW =====")

bank.withdraw(account_1, 2500)

print("\n===== TRANSFER =====")

# Do NOT transfer to same account
bank.transfer(account_1, account_2, 2000)

print("\n===== TRANSACTION HISTORY =====")

history = bank.transaction_history(account_1)

for h in history:
    print(h)
