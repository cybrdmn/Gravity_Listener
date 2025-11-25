# 🌌 Gravity Listener

**Gravity Listener** ist eine Full-Stack AI-Applikation, die Gravitationswellen-Daten analysiert und visualisiert. 
Das Projekt nutzt **echte Signaldaten** (z.B. aus der G2Net Kaggle Challenge), verarbeitet diese mithilfe von `scipy` zu Spektrogrammen und stellt die Ergebnisse über eine **FastAPI**-Schnittstelle bereit. Ein interaktives **Streamlit**-Frontend ermöglicht es Nutzern, diese kosmischen Ereignisse "sichtbar" zu machen.

---

## 🛠️ Setup & Installation

Dieses Projekt nutzt Python 3.10.6 und verwaltet Abhängigkeiten über eine virtuelle Umgebung.

### 1. Voraussetzungen
Stelle sicher, dass `pyenv` und `pyenv-virtualenv` installiert sind.

### 2. Daten herunterladen 💾
Da echte wissenschaftliche Daten groß sind, sind sie nicht im Repository enthalten.
1. Lade dir einen Gravitationswellen-Datensatz herunter (z.B. [G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection/data)).
2. Platziere die `.csv` Datei im Ordner `data/`.
3. Die App erkennt automatisch die Datei und lädt sie. (Falls keine Datei gefunden wird, startet eine Simulation).

### 3. Installation
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

Das Projekt ist vollständig containerisiert. 

**Wichtig:** Damit der Container auf deine lokalen Daten zugreifen kann, muss der Data-Ordner gemounted werden oder im Image gebaut sein (hier: im Build integriert).

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

### CI/CD Simulation
Das `autotest.sh` Skript simuliert eine Pipeline, die Installation, Formatierung und Tests automatisch durchführt.
```bash
./autotest.sh
```

---

## 👥 Credits & Datenquellen
* **Code & Umsetzung:** Noemi Tesan
* **Datenquelle:** [Kaggle G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection)
* **Tools:** FastAPI, Streamlit, SciPy, Docker
