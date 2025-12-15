# Python SQLite GDPR Personregister – Dataanonymisering (Art. 4(5))

## Beskrivning
Detta projekt är ett Python-program som simulerar ett personregister med **GDPR-fokus på Dataanonymisering**.  
Programmet använder en SQLite-databas (`users.db`) och kan:

- Skapa databasen om den inte finns
- Skapa tabellen `users` med fälten `id`, `name` och `email`
- Lägga in två testpersoner: **Peter Petterson** och **Malin Ericsson**
- Visa alla användare i databasen
- Anonymisera alla användare enligt **Art. 4(5) – Dataanonymisering**
- Rensa all testdata (GDPR-åtgärd)

Programmet körs automatiskt i en Docker-container och initierar databasen vid start.

## GDPR-åtgärd
| Funktion          | GDPR-Artikel | Beskrivning |
|------------------|--------------|-------------|
| `anonymize_users()` | Art. 4(5)   | Ersätter namn och e-post med generiska värden så att personer inte längre kan identifieras |
| `clear_users()`     | Art. 4(5)   | Raderar all testdata för att säkerställa dataskydd |

---

## Körning och testning

### 1. Bygg och starta containern
```bash
docker compose up --build

# När containern startar initieras databasen automatiskt och användarna visas

Databasen initierades med testanvändare.
--- Användare i databasen ---
ID: 1, Namn: Peter Petterson, Email: peter@test.com
ID: 2, Namn: Malin Ericsson, Email: malin@test.com
Containern körs. Tryck Ctrl+C för att avsluta.

# Testa GDPR-funktioner i nytt terminalfönster

# Anonymisera användare:
docker exec gdpr_app python -c "import app; app.anonymize_users(); app.show_users()"

# Rensa testdata:
docker exec gdpr_app python -c "import app; app.clear_users(); app.show_users()"

# Återställ testdata:
docker exec gdpr_app python -c "import app; app.setup_database(); app.show_users()"

# Stoppa containern
docker compose down

# Filstruktur
app.py              # Python-programmet med GDPR-funktioner
Dockerfile          # Instruktioner för att bygga Docker-image
docker-compose.yml  # Konfiguration för att köra containern
.gitignore          # Ignorerar temporära filer
README.md           # Dokumentation
data/               # Här lagras SQLite-databasen users.db

## CI/CD med GitHub Actions

Projektet använder **GitHub Actions** för att automatiskt testa koden vid varje commit och pull request.  
Workflow-filen finns i `.github/workflows/build-test.yml`.

### Vad som testas
- Att Python och SQLite kan importeras korrekt
- Att `app.py` kompilerar utan fel

### Workflow-fil
```yaml
name: Build and Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    
    - name: Test imports and syntax
      run: |
        python -c "import sqlite3, os; print('All imports successful')"
        python -m py_compile app.py
        echo "Code compilation successful"
