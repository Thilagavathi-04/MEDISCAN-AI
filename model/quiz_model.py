import sqlite3

DB = "hospital.db"

class QuizModel:

    @staticmethod
    def save_score(username, score, quiz_type="static"):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO intern_scores (intern_username, score, quiz_type)
                VALUES (?, ?, ?)
            """, (username, score, quiz_type))
            conn.commit()

    @staticmethod
    def get_scores(username):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT score, taken_at
                FROM intern_scores
                WHERE intern_username = ?
                ORDER BY taken_at DESC
            """, (username,))
            return cursor.fetchall()
