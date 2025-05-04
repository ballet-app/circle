import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit UI
st.title('Rysowanie okręgu na podstawie środka i promienia')

x0 = st.number_input('Podaj współrzędną x środka okręgu:', value=0.0)
y0 = st.number_input('Podaj współrzędną y środka okręgu:', value=0.0)
r = st.number_input('Podaj promień okręgu:', min_value=0.0, value=1.0)

# Rysowanie okręgu
fig, ax = plt.subplots()
theta = np.linspace(0, 2*np.pi, 200)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)
ax.plot(x, y, label='Okrąg')
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.scatter([x0], [y0], color='red', label='Środek')
ax.legend()
st.pyplot(fig)

# Równanie okręgu i nierówność
rownanie = f'(x - {x0})² + (y - {y0})² = {r**2}'
nierownosc = f'(x - {x0})² + (y - {y0})² ≤ {r**2}'
st.markdown(f'**Równanie okręgu:** {rownanie}')
st.markdown(f'**Nierówność dla koła:** {nierownosc}')
