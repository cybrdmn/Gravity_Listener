from fastapi import FastAPI
from gravity_listener.data_loader import load_data
from gravity_listener.processing import compute_spectrogram
import numpy as np

# Initialize the API
app = FastAPI(title="Gravity Listener API", version="0.1")

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "Gravity Listener API is online and listening! 🌌"}

@app.get("/analyze")
def analyze_wave():
    """
    Loads the dummy gravity wave, computes the spectrogram, 
    and returns the raw data arrays so the frontend can plot them.
    """
    # 1. Get the raw signal
    t, signal = load_data()
    
    # 2. Process it into a spectrogram
    # (We use a smaller sample_rate here just to keep the JSON size manageable for the demo)
    f, t_spec, Sxx = compute_spectrogram(signal, sample_rate=1024)
    
    # 3. Return as JSON (Web APIs can't send Numpy arrays, so we convert to lists)
    return {
        "frequencies": f.tolist(),
        "times": t_spec.tolist(),
        "spectrogram": Sxx.tolist()
    }
