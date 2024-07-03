from flask import Flask, request
from cloudevents.http import from_http
import signal
import sys

app = Flask(__name__)

# Signalbehandlungsfunktionen
def handle_sigterm(signum, frame):
    print("SIGTERM erhalten, Skript wird beendet...")
    cleanup()
    sys.exit(0)

def handle_sigint(signum, frame):
    print("SIGINT erhalten, Skript wird beendet...")
    cleanup()
    sys.exit(0)

# Cleanup-Funktion, die beim Beenden ausgeführt wird
def cleanup():
    print("Aufräumen vor dem Beenden...")
    # Fügen Sie hier Ihre Aufräumarbeiten hinzu
    print("Aufräumarbeiten abgeschlossen.")

# Registrieren der Signalhandler
signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigint)

@app.route('/', methods=['POST'])
def receive_event():
    event = from_http(request.headers, request.get_data())
    print(f"Received CloudEvent:")
    print(f"ID: {event['id']}")
    print(f"Source: {event['source']}")
    print(f"Type: {event['type']}")
    print(f"Time: {event['time']}")
    print(f"Data: {event.data}")
    sys.stdout.flush()
    return 'Event received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
