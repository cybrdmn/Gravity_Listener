import pytest
import numpy as np
from gravity_listener.processing import compute_spectrogram

def test_spectrogram_output():
    """
    Verifies that the spectrogram function returns the correct shapes.
    """
    # 1. Create a dummy signal (1 second of random noise at 4096 Hz)
    dummy_wave = np.random.normal(0, 1, 4096)
    
    # 2. Run the function
    f, t, Sxx = compute_spectrogram(dummy_wave, sample_rate=4096)
    
    # 3. Basic Assertions: Ensure nothing is None
    assert f is not None, "Frequencies array should not be None"
    assert t is not None, "Time array should not be None"
    assert Sxx is not None, "Spectrogram matrix should not be None"
    
    # 4. Shape Assertions: The matrix Sxx must match (frequencies x time steps)
    # Sxx.shape[0] corresponds to frequency bins
    # Sxx.shape[1] corresponds to time segments
    assert Sxx.shape[0] == len(f), "Spectrogram height must match frequency array length"
    assert Sxx.shape[1] == len(t), "Spectrogram width must match time array length"
