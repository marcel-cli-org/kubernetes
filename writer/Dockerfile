# Verwende das offizielle Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere das Python-Skript in das Arbeitsverzeichnis
COPY writer.py .

# Install any needed packages specified in requirements.txt
RUN pip install setproctitle 

# Erstelle das Verzeichnis /data, falls es nicht existiert
RUN mkdir -p /data

# Definiere ein Volume fÃ¼r das Verzeichnis /data
VOLUME ["/data"]

USER 1001:100

# FÃ¼hre das Python-Skript aus, wenn der Container gestartet wird
CMD ["python", "writer.py"]
