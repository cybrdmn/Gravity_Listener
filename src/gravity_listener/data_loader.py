import numpy as np
import pandas as pd
import os

def generate_dummy_wave(duration=2, rate=4096):
    """
    Generates a dummy gravitational wave signal (sine wave + noise)
    for testing our pipeline before we have real data.
    """
    t = np.linspace(0, duration, int(duration * rate))
    
    # Simulate a 'chirp' (frequency increases over time like a black hole merger)
    freq = np.linspace(50, 500, len(t))
    signal = 0.5 * np.sin(2 * np.pi * freq * t)
    
    # Add some random universe noise
    noise = np.random.normal(0, 0.3, len(t))
    
    return t, signal + noise

def load_data(filepath=None):
    """
    Tries to load data from a file. If None or not found,
    generates dummy data so we can keep working.
    """
    if filepath is None or not os.path.exists(filepath):
        print("⚠️  No file found. Generating dummy gravity wave data...")
        return generate_dummy_wave()
    
    # If we had a real CSV, we would load it here:
    # return pd.read_csv(filepath)
    print(f"Loading data from {filepath}...")
    return pd.read_csv(filepath)
