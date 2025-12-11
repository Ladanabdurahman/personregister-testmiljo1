# Basbild med Python 3.12
FROM python:3.12-slim

# Sätt arbetskatalog i containern
WORKDIR /app

# Kopiera in appen
COPY app.py .

# Installera eventuella beroenden (om du har fler paket kan du lägga till requirements.txt)
# RUN pip install --no-cache-dir -r requirements.txt

# Gör utskrifter synliga direkt
ENV PYTHONUNBUFFERED=1

# Starta appen
CMD ["python", "app.py"]
