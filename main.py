from audio_loader import load_audio
from spectrum import compute_spectrum
from metrics import dominant_frequency, band_energy, low_end_score
from assistant import generate_mix_feedback
from report import generate_report

import librosa


SUB_LOW = 40
SUB_HIGH = 80


# Carregar arquivos
kick_audio, kick_sr = load_audio("kick.wav")
bass_audio, bass_sr = load_audio("bass.wav")

# Tratamento inteligente de sample rate
if kick_sr != bass_sr:
    print("\n⚠ Sample Rate Incompatibility Detected")
    print(f"Kick: {kick_sr} Hz")
    print(f"Bass: {bass_sr} Hz")
    print("Reamostrando bass automaticamente para igualar ao kick...\n")

    bass_audio = librosa.resample(
        bass_audio,
        orig_sr=bass_sr,
        target_sr=kick_sr
    )

    bass_sr = kick_sr
    print("Reamostragem concluída.\n")

# Calcular espectro
kick_freqs, kick_mag = compute_spectrum(kick_audio, kick_sr)
bass_freqs, bass_mag = compute_spectrum(bass_audio, bass_sr)

# Métricas principais
kick_dom = dominant_frequency(kick_freqs, kick_mag)
bass_dom = dominant_frequency(bass_freqs, bass_mag)

kick_sub = band_energy(kick_freqs, kick_mag, SUB_LOW, SUB_HIGH)
bass_sub = band_energy(bass_freqs, bass_mag, SUB_LOW, SUB_HIGH)

score = low_end_score(kick_sub, bass_sub)

# Feedback inteligente
feedback = generate_mix_feedback(kick_dom, bass_dom, kick_sub, bass_sub)

for msg in feedback:
    print(">>", msg)

# Gerar relatório visual
generate_report(
    kick_freqs, kick_mag,
    bass_freqs, bass_mag,
    kick_dom, bass_dom,
    kick_sub, bass_sub,
    score
)
