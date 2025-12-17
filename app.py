import sqlite3
import os

# Databasfil (hämtas från miljövariabel eller standard "users.db")
DB_NAME = os.getenv("DATABASE_PATH", "users.db")

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Skapa tabell om den inte finns
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    # Lägg till testanvändare om tabellen är tom
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Peter Petterson", "peter@test.com"))
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Malin Ericsson", "malin@test.com"))
        print("Databasen initierades med testanvändare.")
    else:
        print("Databasen innehåller redan användare.")

    conn.commit()
    conn.close()

def show_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    print("\n--- Användare i databasen ---")
    if not rows:
        print("Inga användare hittades.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Namn: {row[1]}, Email: {row[2]}")

    conn.close()

def clear_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("\nAlla användare har raderats (GDPR).")

def anonymize_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = 'Anonym', email = 'anonym@none'")
    conn.commit()
    conn.close()
    print("\nAlla användare har anonymiserats (GDPR).")

def run_all():
    print("\n--- Kör GDPR-sekvens ---")

    # 1. Rensa testdata
    clear_users()
    show_users()

    # 2. Återställ testdata
    setup_database()
    show_users()

    # 3. Anonymisera testdata
    anonymize_users()
    show_users()

    print("\n--- GDPR-sekvens klar ---")

if __name__ == "__main__":
    # Kör hela GDPR-sekvensen automatiskt när du trycker på play
    run_all()

    print("\nProgrammet kördes klart.")

