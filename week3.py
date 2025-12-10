import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Color Palettes
# -------------------------
def simple_tidy():
    return [
        (0.85, 0.85, 0.85),
        (0.30, 0.40, 0.55),
        (0.80, 0.60, 0.50),
        (0.60, 0.75, 0.70),
        (0.90, 0.90, 0.70)
    ]

def splendid_complex():
    return [
        (0.9, 0.4, 0.4),
        (0.4, 0.7, 0.9),
        (0.8, 0.9, 0.4),
        (0.7, 0.4, 0.8),
        (0.4, 0.9, 0.6),
        (0.95, 0.7, 0.3)
    ]

def pastel_only():
    return [
        (0.95, 0.80, 0.80),
        (0.80, 0.90, 0.95),
        (0.85, 0.85, 0.95),
        (0.90, 0.85, 0.90),
        (0.95, 0.90, 0.80)
    ]

def high_contrast():
    return [
        (0.95, 0.10, 0.10),
        (0.10, 0.10, 0.95),
        (0.10, 0.80, 0.10),
        (0.95, 0.95, 0.10),
        (0.90, 0.10, 0.80)
    ]

def monochrome():
    shades = np.linspace(0.2, 0.85, 6)
    return [(s, s, s) for s in shades]

# -------------------------
# Shape / Blob Generator
# -------------------------
def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2 * math.pi, points)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Generative Abstract Poster", layout="centered")

st.title("🎨 Generative Abstract Poster with Style Controls")

color_choice = st.selectbox(
    "Choose a color palette:",
    ["simple&tidy", "splendid&complex", "Pastel colors only", "High contrast vivid", "Monochrome shade"]
)

style_choice = st.selectbox(
    "Choose a visual style:",
    ["minimal", "vivid", "noise touch"]
)

# Mapping palette choice
palette_map = {
    "simple&tidy": simple_tidy,
    "splendid&complex": splendid_complex,
    "Pastel colors only": pastel_only,
    "High contrast vivid": high_contrast,
    "Monochrome shade": monochrome
}

# Visual style effects
def apply_style(style):
    if style == "minimal":
        return 0.25, 0.5     # low alpha
    elif style == "vivid":
        return 0.5, 0.9      # high alpha
    elif style == "noise touch":
        return 0.3, 0.7      # medium alpha with wobble
    return 0.25, 0.5

# -------------------------
# Generate Poster
# -------------------------
if st.button("Generate Poster"):
    palette = palette_map[color_choice]()  # chosen palette
    alpha_min, alpha_max = apply_style(style_choice)

    plt.figure(figsize=(7, 10))
    plt.axis('off')
    plt.gca().set_facecolor((0.98, 0.98, 0.97))

    n_layers = 8

    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        wobble = random.uniform(0.05, 0.25)

        x, y = blob(center=(cx, cy), r=rr, wobble=wobble)
        color = random.choice(palette)
        alpha = random.uniform(alpha_min, alpha_max)

        if style_choice == "noise touch":
            # Random jitter effect
            x += np.random.normal(0, 0.003, len(x))
            y += np.random.normal(0, 0.003, len(y))

        plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

    plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight="bold", transform=plt.gca().transAxes)
    plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=plt.gca().transAxes)

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    st.pyplot(plt)
else:
    st.info("Choose style options and click Generate Poster!")
