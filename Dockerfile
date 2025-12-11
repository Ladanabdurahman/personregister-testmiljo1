FROM python:3.12-slim

WORKDIR /app

COPY app.py .

# Gör utskrifter synliga direkt
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]

