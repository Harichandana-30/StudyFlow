import sqlite3

def create_database():
    conn = sqlite3.connect("studyflow.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        subject TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()


def add_task(task, subject):
    conn = sqlite3.connect("studyflow.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (task, subject)
    VALUES (?, ?)
    """, (task, subject))

    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect("studyflow.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks