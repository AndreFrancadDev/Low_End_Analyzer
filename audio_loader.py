import numpy as np
import soundfile as sf


def load_audio(path):
    audio, sr = sf.read(path)

    # Converter para mono se for estéreo
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # Converter para float32
    audio = audio.astype(np.float32)

    # Remover DC offset
    audio = audio - np.mean(audio)

    # Normalização por pico
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val

    return audio, sr
