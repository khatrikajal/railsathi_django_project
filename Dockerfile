# Use official Python image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system packages (like nc)
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean


WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
