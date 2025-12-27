from database import get_connection

class BankService:

    def create_account(self, user_id, account_type):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO accounts (user_id, account_type, balance) VALUES (%s, %s, 0)",
            (user_id, account_type)
        )

        conn.commit()
        cursor.close()
        conn.close()

    def get_account(self, account_no):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM accounts WHERE account_no=%s AND status='active'",
            (account_no,)
        )

        acc = cursor.fetchone()

        cursor.close()
        conn.close()

        return acc

    def deposit(self, account_no, amount):
        if amount <= 0:
            raise Exception("Invalid amount")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_no=%s AND status='active'",
            (amount, account_no)
        )

        cursor.execute(
            "INSERT INTO transactions (to_account, amount, transaction_type) VALUES (%s, %s, 'deposit')",
            (account_no, amount)
        )

        conn.commit()
        cursor.close()
        conn.close()

    def withdraw(self, account_no, amount):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=%s AND status='active'",
            (account_no,)
        )

        balance = cursor.fetchone()

        if not balance or balance[0] < amount:
            conn.close()
            raise Exception("Insufficient balance")

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_no=%s",
            (amount, account_no)
        )

        cursor.execute(
            "INSERT INTO transactions (from_account, amount, transaction_type) VALUES (%s, %s, 'withdraw')",
            (account_no, amount)
        )

        conn.commit()
        cursor.close()
        conn.close()

    def transfer(self, from_acc, to_acc, amount):
        if amount <= 0:
            raise Exception("Invalid amount")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT balance FROM accounts WHERE account_no=%s AND status='active'",
                (from_acc,)
            )
            balance = cursor.fetchone()[0]

            if balance < amount:
                raise Exception("Insufficient funds")

            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE account_no=%s",
                (amount, from_acc)
            )

            cursor.execute(
                "UPDATE accounts SET balance = balance + %s WHERE account_no=%s",
                (amount, to_acc)
            )

            cursor.execute(
                """INSERT INTO transactions 
                (from_account, to_account, amount, transaction_type)
                VALUES (%s, %s, %s, 'transfer')""",
                (from_acc, to_acc, amount)
            )

            conn.commit()

        except:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()

    def transaction_history(self, account_no):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM transactions
            WHERE from_account=%s OR to_account=%s
            ORDER BY date DESC
            """,
            (account_no, account_no)
        )

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data
    
    def get_user_accounts(self, user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM accounts WHERE user_id = %s AND status='active'",
            (user_id,)
        )

        accounts = cursor.fetchall()

        cursor.close()
        conn.close()

        return accounts

