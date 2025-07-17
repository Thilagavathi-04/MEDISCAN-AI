import sqlite3

def create_tables():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_username TEXT,
            image_path TEXT,
            ocr_text TEXT,
            ai_summary TEXT
        )
    """)

    cursor.execute("PRAGMA table_info(reports)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'doctor_comment' not in columns:
        print("Adding missing 'doctor_comment' column to reports table...")
        cursor.execute("ALTER TABLE reports ADD COLUMN doctor_comment TEXT")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctor_comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_id INTEGER,
            doctor_username TEXT,
            comment TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS intern_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intern_username TEXT,
            score INTEGER,
            taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("PRAGMA table_info(intern_scores)")
    score_columns = [col[1] for col in cursor.fetchall()]
    if 'quiz_type' not in score_columns:
        print("Adding missing 'quiz_type' column to intern_scores table...")
        cursor.execute("ALTER TABLE intern_scores ADD COLUMN quiz_type TEXT DEFAULT 'static'")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()