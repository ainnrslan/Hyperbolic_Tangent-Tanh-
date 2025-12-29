import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Tanh Activation Function")

x = np.linspace(-10, 10, 400)
tanh = np.tanh(x)

plt.figure()
plt.plot(x, tanh)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Hyperbolic Tangent (Tanh)")
st.pyplot(plt)