from flask import Flask, request, render_template_string
from cloudevents.http import from_http
import signal
import sys

app = Flask(__name__)

# Globale Liste zur Speicherung der Cloudevents
events = []

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

@app.route('/', methods=['GET'])
def show_events():
    # HTML Template zur Anzeige der Cloudevents mit Bootstrap
    html_template = '''
    <!doctype html>
    <html lang="de">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <title>Cloudevents</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1 class="mb-4">Empfangene Cloudevents</h1>
          <ul class="list-group">
            {% for event in events %}
              <li class="list-group-item">
                <h5 class="mb-1">ID: {{ event.id }}</h5>
                <p class="mb-1"><strong>Source:</strong> {{ event.source }}</p>
                <p class="mb-1"><strong>Type:</strong> {{ event.type }}</p>
                <p class="mb-1"><strong>Time:</strong> {{ event.time }}</p>
                <p class="mb-1"><strong>Data:</strong> {{ event.data }}</p>
              </li>
            {% endfor %}
          </ul>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      </body>
    </html>
    '''
    return render_template_string(html_template, events=events)

@app.route('/', methods=['POST'])
def receive_event():
    event = from_http(request.headers, request.get_data())
    print(f"Received CloudEvent:")
    print(f"ID: {event['id']}")
    print(f"Source: {event['source']}")
    print(f"Type: {event['type']}")
    print(f"Time: {event['time']}")
    print(f"Data: {event.data}")
    
    # Neuen Event zuoberst zur Liste hinzufügen
    events.insert(0, {
        'id': event['id'],
        'source': event['source'],
        'type': event['type'],
        'time': event['time'],
        'data': event.data
    })
    
    sys.stdout.flush()
    return 'Event received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
