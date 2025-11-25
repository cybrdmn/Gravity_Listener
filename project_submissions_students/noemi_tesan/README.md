# 🌌 Gravity Listener

**Gravity Listener** ist eine Full-Stack AI-Applikation, die Gravitationswellen-Daten analysiert und visualisiert. 
Das Projekt simuliert Signale von kollidierenden schwarzen Löchern ("Chirps"), verarbeitet diese mithilfe von `scipy` zu Spektrogrammen und stellt die Ergebnisse über eine **FastAPI**-Schnittstelle bereit. Ein interaktives **Streamlit**-Frontend ermöglicht es Nutzern, diese kosmischen Ereignisse "sichtbar" zu machen.

---

## 🛠️ Setup & Installation

Dieses Projekt nutzt Python 3.10.6 und verwaltet Abhängigkeiten über eine virtuelle Umgebung.

### 1. Voraussetzungen
Stelle sicher, dass `pyenv` und `pyenv-virtualenv` installiert sind.

### 2. Installation
Navigiere in den Projektordner und richte die Umgebung ein:

```bash
# Umgebung erstellen und aktivieren
pyenv virtualenv 3.10.6 gravity_env
pyenv activate gravity_env

# Abhängigkeiten installieren
pip install -r requirements.txt

# Das Projekt als lokales Package installieren
pip install -e .
```

---

## 🚀 Verwendung

### API starten
Die API berechnet die Spektrogramme im Hintergrund.
```bash
uvicorn gravity_listener.main:app --reload
```

### Frontend starten
Das Dashboard visualisiert die Daten.
```bash
streamlit run src/gravity_listener/frontend.py
```

---

## 🐳 Docker (Containerisierung)

Das Projekt ist vollständig containerisiert. Du kannst die gesamte App (API + Frontend) mit einem einzigen Befehl starten, ohne Python lokal installieren zu müssen.

### Image bauen
```bash
docker build -t gravity_listener .
```

### Container starten
Startet die API auf Port 8000 und das Frontend auf Port 8501.
```bash
docker run -p 8000:8000 -p 8501:8501 gravity_listener
```

---

## 🤖 Automatisierung & Tests

Für eine effiziente Entwicklung nutzen wir `make` und Shell-Skripte.

### Makefile Befehle
* `make install`: Installiert alle Abhängigkeiten und das Package.
* `make test`: Führt die Test-Suite (Pytest) aus.
* `make clean`: Entfernt temporäre Dateien.

### CI/CD Simulation
Das `autotest.sh` Skript simuliert eine Pipeline, die Installation, Formatierung und Tests automatisch durchführt.
```bash
./autotest.sh
```

---

## 🏗️ Projektstruktur

```
├── data/                   # (Optional) Lokale Datensätze
├── src/                    # Quellcode
│   ├── gravity_listener/   # Haupt-Package
│   │   ├── __init__.py
│   │   ├── data_loader.py  # Lädt oder generiert Signale
│   │   ├── processing.py   # Berechnet Spektrogramme
│   │   ├── main.py         # FastAPI Backend
│   │   └── frontend.py     # Streamlit Dashboard
├── tests/                  # Automatisierte Tests
├── Dockerfile              # Container-Konfiguration
├── Makefile                # Befehls-Shortcuts
├── autotest.sh             # CI/CD Skript
├── requirements.txt        # Projekt-Abhängigkeiten
├── setup.py                # Package-Konfiguration
└── README.md               # Projektdokumentation
```

## 👥 Credits
Erstellt von **Noemi Tesan** im Rahmen des AI-Projektkurses.
