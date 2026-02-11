FROM python:3.10-slim

LABEL authors="sajithjeewantha"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/


RUN mkdir -p /app/src/.flask_session

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.app:app"]

