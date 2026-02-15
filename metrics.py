import numpy as np


def dominant_frequency(freqs, magnitude):
    return freqs[np.argmax(magnitude)]


def band_energy(freqs, magnitude_db, low, high):
    mask = (freqs >= low) & (freqs <= high)

    # Converter de dB para linear
    magnitude_linear = 10 ** (magnitude_db / 20)

    return np.sum(magnitude_linear[mask])


def low_end_score(kick_energy, bass_energy):
    ratio = bass_energy / (kick_energy + 1e-10)

    if ratio < 0.8:
        return 90
    elif ratio < 1.2:
        return 75
    elif ratio < 1.5:
        return 60
    else:
        return 40
