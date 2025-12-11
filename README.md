# Python SQLite GDPR Personregister

## Beskrivning
Detta projekt är ett enkelt Python-program som simulerar ett personregister med GDPR-funktioner, lagrat i en SQLite-databas.  
Programmet kan:

- Skapa databasen `users.db` om den inte finns
- Skapa tabellen `users` med fälten `id`, `name` och `email`
- Lägga in två testpersoner: Peter Petterson och Malin Ericsson
- Visa alla användare i databasen
- Rensa alla användare (ta bort testdata)
- Anonymisera alla användare (GDPR-anonymisering)

Programmet körs via en terminalbaserad meny inuti en Docker-container.

## Förutsättningar
För att köra projektet behövs:

- Docker installerat
- Docker Compose installerat
- Grundläggande kunskap om terminalkommandon

## Filstruktur
app.py
Dockerfile
docker-compose.yml
.gitignore
README.md
data/ # Här lagras SQLite-databasen users.db

## GDPR-åtgärd i projektet

| Funktion               | GDPR-Artikel| Beskrivning |
|------------------------|-------------|-------------|
| anonymize_users()      | Art. 4(5)   | Ersätter namn och e-post med generiska värden så att personer inte längre kan identifieras                              |

**Effekt:** Efter anonymisering går det inte längre att koppla en post till en faktisk individ, vilket uppfyller GDPR:s definition av anonymiserad data.

## Bygga och köra med Docker

1. Öppna terminalen och navigera till projektmappen.

2. Bygg och starta containern med:
```bash
docker compose up --build

# När containern startar visas menyn
--- MENY ---
1. Visa användare
2. Rensa användare (radera testdata)
3. Anonymisera användare (GDPR-anonymisering)
4. Avsluta

#Skriv en siffra (1–4) och tryck Enter för att välja alternativ

#För att stoppa containern, tryck Ctrl + C i terminalen och kör sedan
docker compose down
