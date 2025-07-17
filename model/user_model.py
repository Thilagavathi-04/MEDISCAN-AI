import sqlite3

DB_NAME = "hospital.db"

class UserModel:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @staticmethod
    def register_user(username, password, role):
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           (username, password, role))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def validate_user(username, password):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT role FROM users WHERE LOWER(TRIM(username)) = ? AND password = ?",
            (username.strip().lower(), password)
        )
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None