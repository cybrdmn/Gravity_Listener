import numpy as np
import pandas as pd
import os
import random

def generate_dummy_wave(duration=2, rate=4096):
    """Generiert Dummy-Daten (Fallback)."""
    t = np.linspace(0, duration, int(duration * rate))
    freq = np.linspace(50, 500, len(t))
    signal = 0.5 * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, 0.3, len(t))
    return t, signal + noise

def load_data(filepath=None):
    """
    Lädt echte Daten. Wenn die Datei zu lang ist,
    wird ein ZUFÄLLIGER Ausschnitt von 3 Sekunden gewählt.
    """
    if filepath and os.path.exists(filepath):
        print(f"📂 Lade echte Daten von: {filepath}")
        try:
            # CSV laden
            df = pd.read_csv(filepath)
            
            # Signal extrahieren (nur numerische Werte, alles in ein Array)
            signal = df.select_dtypes(include=[np.number]).values.flatten()
            
            # Maximale Länge: 3 Sekunden bei 4096 Hz
            max_samples = 4096 * 3
            
            if len(signal) > max_samples:
                # Zufälligen Startpunkt wählen
                max_start_index = len(signal) - max_samples
                start_index = random.randint(0, max_start_index)
                
                print(f"✂️ Schneide zufälligen Clip von Index {start_index} bis {start_index + max_samples}")
                signal = signal[start_index : start_index + max_samples]
            
            # Zeitachse passend zum (geschnittenen) Signal erstellen
            t = np.linspace(0, len(signal)/4096, len(signal))
                
            return t, signal

        except Exception as e:
            print(f"⚠️ Fehler beim Laden der Datei: {e}")
            print("Verwende stattdessen Simulation...")
    
    # Fallback
    if filepath:
        print(f"⚠️ Datei nicht gefunden: {filepath}")
        
    return generate_dummy_wave()
