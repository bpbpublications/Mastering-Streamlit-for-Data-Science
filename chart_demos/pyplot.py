import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave')
plt.title("Line Chart with Matplotlib")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

st.pyplot(plt)
