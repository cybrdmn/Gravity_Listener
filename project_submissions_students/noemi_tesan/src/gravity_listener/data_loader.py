import numpy as np
import pandas as pd
import os

def generate_dummy_wave(duration=2, rate=4096):
    """Generiert Dummy-Daten (Fallback)."""
    t = np.linspace(0, duration, int(duration * rate))
    freq = np.linspace(50, 500, len(t))
    signal = 0.5 * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, 0.3, len(t))
    return t, signal + noise

def load_data(filepath=None):
    """
    Lädt echte Daten aus einer CSV, falls vorhanden.
    Sonst generiert es Dummy-Daten.
    """
    if filepath and os.path.exists(filepath):
        print(f"📂 Lade echte Daten von: {filepath}")
        try:
            # Lade die CSV (wir nehmen an, das Signal ist in der ersten Spalte oder flach)
            df = pd.read_csv(filepath)
            
            # Nimm nur die numerischen Werte (flachklopfen zu einem Array)
            # Falls deine CSV Header hat, wird das hier automatisch gehandhabt
            signal = df.select_dtypes(include=[np.number]).values.flatten()
            
            # Wir basteln eine Zeitachse dazu (Rate 4096 Hz geschätzt)
            t = np.linspace(0, len(signal)/4096, len(signal))
            
            # Nimm nur die ersten 2-3 Sekunden, damit das Frontend nicht explodiert
            max_samples = 4096 * 3
            if len(signal) > max_samples:
                signal = signal[:max_samples]
                t = t[:max_samples]
                
            return t, signal
        except Exception as e:
            print(f"⚠️ Fehler beim Laden der Datei: {e}")
            print("Verwende stattdessen Simulation...")
    
    # Fallback
    if filepath:
        print(f"⚠️ Datei nicht gefunden: {filepath}")
        
    return generate_dummy_wave()
