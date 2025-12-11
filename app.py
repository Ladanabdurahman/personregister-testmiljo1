import sqlite3  
import os  

DB_NAME = os.getenv("DATABASE_PATH", "users.db")  # Databasfil

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
    print("\nAlla användare har raderats.")

    conn.close()

def anonymize_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Anonymisera användare
    cur.execute("UPDATE users SET name = 'Anonym', email = 'anonym@none'")
    conn.commit()
    print("\nAlla användare har anonymiserats.")

    conn.close()

def main():
    setup_database()  # Initiera databas

    while True:
        print("\n--- MENY ---")
        print("1. Visa användare")
        print("2. Rensa användare (radera testdata)")
        print("3. Anonymisera användare (GDPR-anonymisering)")
        print("4. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            show_users()
        elif choice == "2":
            clear_users()
        elif choice == "3":
            anonymize_users()
        elif choice == "4":
            print("Avslutar.")
            break
        else:
            print("Fel val. Försök igen.")

if __name__ == "__main__":
    main()
