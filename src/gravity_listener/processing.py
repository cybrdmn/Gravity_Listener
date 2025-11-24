import numpy as np
from scipy import signal

def compute_spectrogram(wave_data, sample_rate=4096):
    """
    Computes the spectrogram of a gravitational wave.
    
    Args:
        wave_data (np.array): The 1D array of the signal.
        sample_rate (int): Number of samples per second (Hz).
        
    Returns:
        f: Array of sample frequencies.
        t: Array of segment times.
        Sxx: Spectrogram of x (Power Spectral Density).
    """
    # Use Scipy to compute the math behind the heat map
    f, t, Sxx = signal.spectrogram(wave_data, sample_rate)
    return f, t, Sxx
