import numpy as np

def is_silent(audio_np, threshold=500):
    rms = np.sqrt(np.mean(audio_np**2))
    return rms < threshold
