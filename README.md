# Python SQLite Testdata Manager 

## Beskrivning
Detta projekt är ett enkelt Python-program som hanterar testdata i en SQLite-databas.  
Programmet kan:

- Skapa databasen `users.db` om den inte finns
- Skapa tabellen `users` med fälten `id`, `name` och `email`
- Lägga in två testpersoner: Peter Petterson och Malin Ericsson
- Visa alla användare i databasen
- Rensa alla användare
- Anonymisera alla användare

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

## Bygga och köra med Docker

1. Öppna terminalen och navigera till projektmappen.

2. Bygg och starta containern med:
docker compose up --build

3. När containern startar visas menyn:
--- MENY ---
Visa användare
Rensa användare
Anonymisera användare
Avsluta

Skriv en siffra (1–4) och tryck Enter för att välja alternativ.

4. För att stoppa containern, tryck `Ctrl + C` i terminalen och kör sedan:
docker compose down
