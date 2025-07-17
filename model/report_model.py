import sqlite3

DB = "hospital.db"

class ReportModel:
    @staticmethod
    def save_report(patient_username, image_path, ocr_text, ai_summary):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reports (patient_username, image_path, ocr_text, ai_summary)
                VALUES (?, ?, ?, ?)
            """, (patient_username, image_path, ocr_text, ai_summary))
            conn.commit()

    @staticmethod
    def get_reports_by_patient(username):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, image_path, ocr_text, ai_summary, doctor_comment
                FROM reports
                WHERE patient_username = ?
            """, (username,))
            return cursor.fetchall()

    @staticmethod
    def get_report_by_id(report_id):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, patient_username, image_path, ocr_text, ai_summary, doctor_comment
                FROM reports
                WHERE id = ?
            """, (report_id,))
            return cursor.fetchone()

    @staticmethod
    def add_doctor_comment(report_id, comment, doctor_username="Unknown"):
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE reports
                SET doctor_comment = ?
                WHERE id = ?
            """, (comment, report_id))

            cursor.execute("""
                INSERT INTO doctor_comments (report_id, doctor_username, comment)
                VALUES (?, ?, ?)
            """, (report_id, doctor_username, comment))

            conn.commit()

    @staticmethod
    def get_all_reports():
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reports")
            return cursor.fetchall()
