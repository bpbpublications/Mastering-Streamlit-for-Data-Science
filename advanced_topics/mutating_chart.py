import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Generate a simple plot function
def generate_plot(sin_frequency=1.0):
    plt.figure(figsize=(10, 4))
    t = np.linspace(0, 1, 500)
    plt.plot(t, np.sin(2 * np.pi * sin_frequency * t))
    plt.title(f"Sin Wave - Frequency: {sin_frequency} Hz")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    return plt

# Sidebar widget for user input
frequency = st.sidebar.slider("Frequency", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Display the chart
st.pyplot(generate_plot(sin_frequency=frequency))
