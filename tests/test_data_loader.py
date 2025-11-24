import pytest
from gravity_listener.data_loader import load_data

def test_dummy_data_generation():
    """
    Checks that the data loader returns valid arrays when no file is provided.
    """
    # Call the function without a filepath
    t, signal = load_data()
    
    # Assertions: Checks that must be true for the test to pass
    assert len(t) > 0, "Time array should not be empty"
    assert len(signal) > 0, "Signal array should not be empty"
    assert len(t) == len(signal), "Time and signal arrays must have the same length"
