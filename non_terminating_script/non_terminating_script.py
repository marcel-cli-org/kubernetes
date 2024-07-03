import signal
import time
import os
import setproctitle

# Setzen des Prozessnamens
setproctitle.setproctitle("non_terminating_script")

# Signalhandler, der nichts tut
def ignore_signals(signum, frame):
    print(f"Erhielt Signal {signum}, aber werde es ignorieren!")

# Registriere den Signalhandler für alle Signale, die der Prozess ignorieren kann
for sig in dir(signal):
    if sig.startswith("SIG") and not sig.startswith("SIG_"):
        try:
            signum = getattr(signal, sig)
            signal.signal(signum, ignore_signals)
        except (OSError, RuntimeError, ValueError):
            # Einige Signale können nicht abgefangen werden, daher diese ignorieren
            pass

print("Starte Endlosschleife. Senden Sie Signale, um zu testen.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Erhielt SIGINT (Strg+C), beende Prozess.")
    
