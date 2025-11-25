from fastapi import FastAPI
from gravity_listener.data_loader import load_data
from gravity_listener.processing import compute_spectrogram
import numpy as np
import os

app = FastAPI(title="Gravity Listener API", version="0.2")

@app.get("/")
def read_root():
    return {"message": "Gravity Listener API is online! 🌌"}

@app.get("/analyze")
def analyze_wave():
    # HIER DEN DATEINAMEN ANPASSEN!
    # 👇👇👇
    csv_filename = "data/60k_submission.csv" 
    
    # Prüfen, ob wir im Docker sind oder lokal
    if not os.path.exists(csv_filename):
        # Falls kein Data-Ordner da ist, lass Data Loader den Fallback machen
        print("Keine CSV gefunden, nutze Simulation.")
        t, signal = load_data(filepath=None)
    else:
        t, signal = load_data(filepath=csv_filename)
    
    # Spektrogramm berechnen
    f, t_spec, Sxx = compute_spectrogram(signal, sample_rate=4096)
    
    return {
        "frequencies": f.tolist(),
        "times": t_spec.tolist(),
        "spectrogram": Sxx.tolist()
    }
