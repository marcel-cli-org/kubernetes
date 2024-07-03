# Verwende das offizielle Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install setproctitle

# Kopiere das Python-Skript in das Arbeitsverzeichnis
COPY non_terminating_script.py .

# Führe das Python-Skript aus, wenn der Container gestartet wird
CMD ["python", "non_terminating_script.py"]
