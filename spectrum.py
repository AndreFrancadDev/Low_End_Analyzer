import numpy as np


def compute_spectrum(audio, sr):
    fft = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(fft), 1 / sr)

    magnitude = np.abs(fft)

    # Evitar log(0)
    magnitude[magnitude == 0] = 1e-10
    magnitude_db = 20 * np.log10(magnitude)

    mask = freqs > 0
    return freqs[mask], magnitude_db[mask]


def compute_stft(audio, sr, frame_size=2048, hop_size=512):
    frames = []
    window = np.hanning(frame_size)

    for i in range(0, len(audio) - frame_size, hop_size):
        frame = audio[i:i + frame_size]

        # Aplicar janela (reduz spectral leakage)
        frame = frame * window

        fft = np.fft.fft(frame)
        magnitude = np.abs(fft)

        magnitude[magnitude == 0] = 1e-10
        magnitude_db = 20 * np.log10(magnitude)

        frames.append(magnitude_db)

    frames = np.array(frames)

    freqs = np.fft.fftfreq(frame_size, 1 / sr)
    mask = freqs > 0

    return freqs[mask], frames[:, mask]
