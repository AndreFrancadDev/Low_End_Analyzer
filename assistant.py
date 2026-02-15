import numpy as np


def detect_frequency_conflict(kick_dom, bass_dom, threshold=10):
    if abs(kick_dom - bass_dom) < threshold:
        return True
    return False


def energy_balance_feedback(kick_energy, bass_energy):
    ratio = bass_energy / (kick_energy + 1e-10)

    if ratio < 0.8:
        return "O kick está dominando a região sub. O bass pode estar fraco."
    elif ratio < 1.2:
        return "Boa relação entre kick e bass na região sub."
    else:
        return "O bass está dominando a região sub. O kick pode estar sendo mascarado."


def generate_mix_feedback(kick_dom, bass_dom, kick_energy, bass_energy):
    feedback = []

    if detect_frequency_conflict(kick_dom, bass_dom):
        feedback.append(
            f"Possível conflito espectral: kick ({kick_dom:.1f} Hz) e bass ({bass_dom:.1f} Hz) estão muito próximos."
        )

    feedback.append(energy_balance_feedback(kick_energy, bass_energy))

    return feedback
