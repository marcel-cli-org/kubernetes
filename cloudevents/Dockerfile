# Verwende ein offizielles Python-Image als Basisimage
FROM python:3.9-slim

# Debugging Tools
RUN apt-get update && apt-get install -y curl wget git psmisc

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements Datei und installiere die AbhÃ¤ngigkeiten
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Exponiere Port 8080 fÃ¼r den Container
EXPOSE 8080

# Definiere den Befehl zum Starten der Anwendung
CMD ["python", "app.py"]
