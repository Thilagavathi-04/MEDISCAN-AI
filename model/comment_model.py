import sqlite3

DB = "hospital.db"

class CommentModel:

    @staticmethod
    def add_comment(report_id, doctor_username, comment):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO doctor_comments (report_id, doctor_username, comment)
                VALUES (?, ?, ?)
            """, (report_id, doctor_username, comment))
            conn.commit()

    @staticmethod
    def get_comments_for_report(report_id):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT doctor_username, comment FROM doctor_comments
                WHERE report_id = ?
            """, (report_id,))
            return cursor.fetchall()