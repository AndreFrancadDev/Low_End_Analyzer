import matplotlib.pyplot as plt


def generate_report(kick_freqs, kick_mag,
                    bass_freqs, bass_mag,
                    kick_dom, bass_dom,
                    kick_sub, bass_sub,
                    score):

    # --------- TERMINAL OUTPUT ---------
    print("\n=== LOW END ANALYSIS REPORT ===")
    print(f"Kick Dominant Frequency: {kick_dom:.2f} Hz")
    print(f"Bass Dominant Frequency: {bass_dom:.2f} Hz")
    print(f"Kick Sub Energy: {kick_sub:.2f}")
    print(f"Bass Sub Energy: {bass_sub:.2f}")
    print(f"Low-End Score: {score}")
    print("================================\n")

    # --------- DARK MODE STYLE ---------
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Background custom
    fig.patch.set_facecolor("#121212")
    ax.set_facecolor("#1e1e1e")

    # Plot lines
    ax.plot(kick_freqs, kick_mag, label="Kick", linewidth=2)
    ax.plot(bass_freqs, bass_mag, label="Bass", linewidth=2)

    # Região Sub
    ax.axvspan(40, 80, alpha=0.15)

    # Dominant lines
    ax.axvline(kick_dom, linestyle="--", linewidth=1.5)
    ax.axvline(bass_dom, linestyle="--", linewidth=1.5)

    # Layout
    ax.set_xlim(0, 200)
    ax.set_xlabel("Frequency (Hz)", fontsize=11)
    ax.set_ylabel("Magnitude (dB)", fontsize=11)
    ax.set_title("Low-End Spectrum Analysis", fontsize=13, pad=15)

    ax.grid(alpha=0.2)
    ax.legend()

    # Score text inside graph
    ax.text(
        0.02, 0.95,
        f"Low-End Score: {score}",
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment="top"
    )

    plt.tight_layout()
    plt.show()
