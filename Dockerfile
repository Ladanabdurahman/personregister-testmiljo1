FROM python:3.12-slim

WORKDIR /app

COPY app.py .

# Skapa data-mappen för SQLite
RUN mkdir -p /data

# Gör utskrifter synliga direkt
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
