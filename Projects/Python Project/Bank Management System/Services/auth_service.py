from database import get_connection
import hashlib

class AuthService:

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, name, email, password, role="customer"):
        conn = get_connection()
        cursor = conn.cursor()

        password_hash = self.hash_password(password)

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, %s)",
                (name, email, password_hash, role)
            )
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def login(self, email, password):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        password_hash = self.hash_password(password)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password_hash=%s",
            (email, password_hash)
        )

        user = cursor.fetchone()
        cursor.close()
        conn.close()

        return user
