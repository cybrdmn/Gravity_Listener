# 🌌 Gravity Listener

**Gravity Listener** is an interactive full-stack AI application for analyzing gravitational waves.
The project visualizes signals from colliding black holes ("chirps") as spectrograms and makes them **audible**. It leverages real scientific data (e.g., LIGO/Virgo) and simulates astrophysical events via "software injection".

---

## ✨ Features

* **🔭 Real Data:** Processes actual signal data (e.g., G2Net Kaggle Challenge).
* **🎲 Random Sampler:** Automatically selects a random 3-second sector of the universe for every scan – every analysis is unique.
* **🎰 Signal Injection:** To test detection capabilities, there is a **30% probability** of an artificial signal ("chirp") being injected into the background noise.
* **🎧 Audio Feedback:** Listen to the cosmic noise (and hidden signals) directly in your browser.
* **🐳 Containerized:** Fully isolated environment using Docker.
* **🎨 Sci-Fi UI:** Immersive dark-mode dashboard built with Streamlit.

---

## 🛠️ Setup & Installation

This project uses Python 3.10.6 and manages dependencies via a virtual environment.

### 1. Prerequisites
Ensure that `pyenv`, `pyenv-virtualenv`, and `Docker` are installed.

### 2. Download Data 💾
Since scientific datasets are large, they are not included in the repository.
1. Download a gravitational wave dataset (e.g., [G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection/data)).
2. Place the `.csv` file inside the `data/` folder.
3. The app automatically detects the file. (If no file is found, it falls back to a full simulation).

### 3. Local Installation (Without Docker)
Navigate to the project folder:

```bash
# Create and activate environment
pyenv virtualenv 3.10.6 gravity_env
pyenv activate gravity_env

# Install dependencies
pip install -r requirements.txt

# Install project as a local package
pip install -e .
```

---

## 🚀 Usage

### Option A: Using Docker (Recommended) 🐳
Starts both Backend and Frontend in an isolated container.

```bash
# Build the image
docker build -t gravity_listener .

# Start the container (API on 8000, Frontend on 8501)
docker run -p 8000:8000 -p 8501:8501 gravity_listener
```
Then open **http://localhost:8501** in your browser.

### Option B: Manual Start
If you are developing locally without Docker:

1. **Start API:**
   ```bash
   uvicorn gravity_listener.main:app --reload
   ```
2. **Start Frontend (in a new terminal):**
   ```bash
   streamlit run src/gravity_listener/frontend.py
   ```

### 🧪 How to Test (Live Demo)
1. Click **"Start Scan"**.
2. Most of the time, you will hear **static noise** (this is physical reality).
3. Keep scanning until you hit the **"Jackpot"** (30% chance).
4. You will hear a distinct **"Whooop"** sound and see a bright yellow curve in the spectrogram.

---

## 🤖 Automation & CI/CD

For efficient development, we use shell scripts to simulate a CI/CD pipeline.

```bash
# Installs dependencies, formats code, and runs tests
./autotest.sh
```

---

## 👥 Credits & Tech Stack
Created as part of the AI Project Course.

* **Author:** Noemi Tesan
* **Data Source:** [Kaggle G2Net Gravitational Wave Detection](https://www.kaggle.com/c/g2net-gravitational-wave-detection)
* **Tech Stack:** FastAPI, Streamlit, SciPy, Matplotlib, Docker

> "Listen to the universe." 🌌
