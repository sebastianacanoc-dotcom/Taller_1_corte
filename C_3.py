"""
C.3 - Carga y descarga de un circuito RC
El usuario ingresa V, C (uF) y R (Ohm) por teclado.
Se grafican ambas curvas: carga y descarga.
Taller de Python - Mecatronica
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Entradas por teclado ---
V = float(input("Ingrese el voltaje de la fuente V (Volts): "))
C_uF = float(input("Ingrese la capacitancia C (uF): "))
R = float(input("Ingrese la resistencia R (Ohm): "))

# Conversion de capacitancia a Faradios
C = C_uF * 1e-6

# Constante de tiempo tau = R*C
tau = R * C

# Vector de tiempo: se grafica hasta 5*tau (aprox. 99.3% de carga/descarga)
t = np.linspace(0, 5 * tau, 500)

# --- Ecuaciones del circuito RC ---
# Carga:    Vc(t) = V * (1 - e^(-t/tau))
# Descarga: Vc(t) = V * e^(-t/tau)
carga = V * (1 - np.exp(-t / tau))
descarga = V * np.exp(-t / tau)

print(f"\nConstante de tiempo tau = R*C = {tau:.6f} s")

# --- Grafica (una sola figura, curvas superpuestas) ---
plt.figure(figsize=(8, 5))
plt.plot(t, carga, color="tab:blue", label="Carga")
plt.plot(t, descarga, color="tab:red", label="Descarga")

plt.title(f"Carga y descarga circuito RC (V={V} V, C={C_uF} uF, R={R} Ohm, tau={tau:.4f} s)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje Vc (V)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("circuito_RC.png", dpi=150)
plt.show()
