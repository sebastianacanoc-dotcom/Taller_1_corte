import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

print("--- Análisis de Sistema de 2do Orden (Forma Canónica) ---")
print("G(s) = K * (wn^2) / (s^2 + 2*zeta*wn*s + wn^2)\n")

# Lectura de los 3 parámetros de la imagen
K = float(input("Ingrese la Ganancia (K): "))
wn = float(input("Ingrese la Frecuencia natural (omega_n): "))
zeta = float(input("Ingrese el Factor de amortiguamiento (zeta): "))

# 1. Clasificación del sistema según zeta
if zeta < 0:
    tipo_sistema = "Inestable"
elif zeta == 0:
    tipo_sistema = "No amortiguado (Oscilatorio puro)"
elif 0 < zeta < 1:
    tipo_sistema = "Subamortiguado"
elif zeta == 1:
    tipo_sistema = "Críticamente amortiguado"
else: # zeta > 1
    tipo_sistema = "Sobreamortiguado"

print(f"\n---> El sistema es: {tipo_sistema}")

# 2. Definición del numerador y denominador para SciPy
num = [K * (wn**2)]
den = [1, 2 * zeta * wn, wn**2]

sistema = signal.TransferFunction(num, den)

# 3. Simulación de la respuesta al escalón
tiempo, respuesta = signal.step(sistema)

# 4. Graficación
plt.figure(figsize=(9, 5))
plt.plot(tiempo, respuesta, 'b-', linewidth=2, label=f'Respuesta Escalón (ζ = {zeta})')
plt.axhline(y=K, color='r', linestyle='--', label=f'Valor Final de Estado Estable (K = {K})')

plt.title(f'Respuesta al Escalón - Sistema {tipo_sistema}', fontsize=12)
plt.xlabel('Tiempo (s)', fontsize=10)
plt.ylabel('Amplitud', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='best')

# Mostrar la figura
plt.show()