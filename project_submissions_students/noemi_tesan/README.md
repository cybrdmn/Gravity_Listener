# 🌌 Gravity Listener

**Gravity Listener** ist eine interaktive Full-Stack AI-Applikation zur Analyse von Gravitationswellen.
Das Projekt visualisiert Signale von kollidierenden schwarzen Löchern ("Chirps") als Spektrogramme und macht sie **hörbar**. Es nutzt echte wissenschaftliche Daten (z.B. LIGO/Virgo) und simuliert astrophysikalische Ereignisse mittels "Software Injection".

---

## ✨ Features

* **🔭 Echte Daten:** Verarbeitet reale Signale (z.B. G2Net Kaggle Challenge).
* **🎲 Random Sampler:** Wählt bei jedem Scan einen zufälligen Sektor des Universums (3-Sekunden-Clip).
* **🎰 Signal Injection:** Um die Detektion zu testen, wird mit einer **30% Wahrscheinlichkeit** ein künstliches Signal ("Chirp") in das echte Hintergrundrauschen injiziert.
* **🎧 Audio-Feedback:** Hör dir das Rauschen des Universums (und die versteckten Signale) an.
* **🐳 Containerized:** Vollständig isolierte Umgebung mit Docker.

---

## 🛠️ Setup & Installation

Dieses Projekt nutzt Python 3.10.6 und verwaltet Abhängigkeiten über eine virtuelle Umgebung.

### 1. Voraussetzungen
Stelle sicher, dass `pyenv`, `pyenv-virtualenv` und `Docker` installiert sind.

### 2. Daten herunterladen 💾
Da echte wissenschaftliche Daten groß sind, sind sie nicht im Repository enthalten.
1. Lade dir einen Gravitationswellen-Datensatz herunter (z.B. [G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection/data)).
2. Platziere die `.csv` Datei im Ordner `data/`.
3. Die App erkennt automatisch die Datei.

### 3. Lokale Installation (Ohne Docker)
Navigiere in den Projektordner:

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

### Mit Docker (Empfohlen) 🐳
Startet Backend und Frontend in einem isolierten Container.

```bash
# Image bauen
docker build -t gravity_listener .

# Container starten (API auf 8000, Frontend auf 8501)
docker run -p 8000:8000 -p 8501:8501 gravity_listener
```
Öffne dann **http://localhost:8501** im Browser.

### Wie man testet
1. Drücke auf **"Scan starten"**.
2. Meistens hörst du nur **statisches Rauschen** (Realität).
3. Drücke so lange weiter, bis du den **"Jackpot"** triffst (30% Chance).
4. Dann hörst du einen **"Whooop"-Sound** und siehst die gelbe Kurve im Spektrogramm.

---

## 🤖 Automatisierung

Für eine effiziente Entwicklung nutzen wir Shell-Skripte.

```bash
# Installiert alles, formatiert Code und führt Tests aus
./autotest.sh
```

---

## 👥 Credits & Tech Stack
Dieses Projekt wurde im Rahmen des AI-Projektkurses erstellt.

* **Author:** Noemi Tesan
* **Datenquelle:** [Kaggle G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection)
* **Tech Stack:** FastAPI, Streamlit, SciPy, Matplotlib, Docker

> "Listen to the universe." 🌌
