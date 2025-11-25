import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt

st.title("🌊 Gravity Listener: Hör dem Universum zu")

st.write("""
Willkommen im Gravitationswellen-Detektor. 
Klicke unten auf den Button, um das Universum nach Signalen von kollidierenden schwarzen Löchern zu scannen.
""")

# Button, um die Analyse zu starten
if st.button("📡 Scan starten"):
    with st.spinner("Horche ins All..."):
        try:
            # Hier nutzen wir die 'requests' Bibliothek!
            response = requests.get("http://127.0.0.1:8000/analyze")
            data = response.json()
            
            # Daten aus der API holen
            frequencies = np.array(data["frequencies"])
            times = np.array(data["times"])
            spectrogram = np.array(data["spectrogram"])

            st.success("Signal entdeckt!")
            
            # Das Spektrogramm zeichnen
            fig, ax = plt.subplots(figsize=(10, 4))
            c = ax.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), shading='gouraud', cmap='inferno')
            ax.set_ylabel('Frequenz [Hz]')
            ax.set_xlabel('Zeit [s]')
            ax.set_title('Spektrogramm des Gravitationswellen-Events')
            fig.colorbar(c, ax=ax, label='Intensität [dB]')
            
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Fehler bei der Verbindung zur API: {e}")
