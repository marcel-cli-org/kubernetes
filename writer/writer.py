import time
from datetime import datetime
import setproctitle

setproctitle.setproctitle("writer")

def write_to_file(filename):
    print("Starte das Schreiben in die Datei.")
    try:
        for _ in range(10):
            with open(filename, "a") as f:
                f.write(f"{datetime.now()}: Eine neue Zeile\n")
            time.sleep(1)  # Warte eine Sekunde statt einer Minute für das Beispiel
    except KeyboardInterrupt:
        print("Erhielt SIGINT (Strg+C), beende Prozess.")
    print("Schreiben abgeschlossen.")

def read_from_file(filename):
    print("Lese Daten aus der Datei.")
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("Inhalt der Datei:")
        print(content)
    except FileNotFoundError:
        print(f"Datei {filename} nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Lesen der Datei: {e}")

def main():
    write_to_file("/data/db.txt")
    read_from_file("/data/DB.txt")

if __name__ == "__main__":
    main()

