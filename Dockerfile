FROM python:3.12-slim

WORKDIR /app

COPY app.py /app/

RUN mkdir -p /data

CMD ["python", "app.py"]
