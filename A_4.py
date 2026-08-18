# ==============================================================================
# Taller 1 – Python (código)
# Presentado por:
# Gisell González
# Emily Castillo
# Sebastian Cano
# Jose Perez
# A. Sin interacción de consola
# ==============================================================================
# Punto 4. Realice un programa para el cálculo de la resistencia de una RTD de
# platino (PT100) en función de la temperatura.
# Una RTD de platino 100 (conocida comúnmente como Pt100) es un sensor de
# temperatura de alta precisión. La sigla RTD significa Detector de Temperatura
# por Resistencia (Resistance Temperature Detector), Pt indica que está hecha de
# platino y 100 significa que tiene una resistencia eléctrica de exactamente
# 100 ohmios (Ω) a 0 °C.
# Para calcular la resistencia de un sensor PT100 en función de la temperatura
# se utiliza la ecuación de Callendar-Van Dusen.
# Para temperaturas mayores o iguales a
#      R(T) = R0 * (1 + A*T + B * T**2)
# Para temperaturas menores a
#      R(T) = R0 * (1 + A*T + B * T**2 + C * (T - 100) * T**3)
# ==============================================================================
# INSTALACIÓN Y CARGA DE LIBRERÍAS
# ==============================================================================
# Matplotlib y NumPy vienen preinstaladas en Google Colab, pero si usas un entorno
# local limpio, puedes instalarlas ejecutando: !pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# PARÁMETROS Y CONSTANTES DE LA ESTÁNDAR IEC 60751 (PT100)
# ==============================================================================
R0 = 100.0          # Resistencia a 0 °C en Ohms (Ω)
A = 3.9083e-3       # Coeficiente A (°C^-1)
B = -5.775e-7       # Coeficiente B (°C^-2)
C = -4.183e-12      # Coeficiente C (°C^-4) (solo para T < 0 °C)

# ==============================================================================
# FUNCIÓN DE CÁLCULO
# ==============================================================================
def resistencia_pt100(temp_celsius):
    """
    Calcula la resistencia (en Ohms) de una RTD PT100 dada la temperatura en °C.
    Soporta tanto valores escalares como arreglos de NumPy.
    """
    temp = np.array(temp_celsius, dtype=float)

    # Ecuación para T >= 0 °C
    r_pos = R0 * (1 + A * temp + B * (temp**2))

    # Ecuación para T < 0 °C
    r_neg = R0 * (1 + A * temp + B * (temp**2) + C * (temp - 100) * (temp**3))

    # Aplica la condición según el rango de temperatura
    resistencia = np.where(temp >= 0, r_pos, r_neg)

    return resistencia if resistencia.ndim > 0 else float(resistencia)

# ==============================================================================
# EJECUCIÓN DIRECTA (SIN INTERACCIÓN DE CONSOLA)
# ==============================================================================

# 1. Evaluación puntual de valores de prueba
temperaturas_prueba = [-50, 0, 25, 100, 200]
print("--- CÁLCULOS PUNTUALES ---")
for t in temperaturas_prueba:
    r = resistencia_pt100(t)
    print(f"Temperatura: {t:6.1f} °C  ==>  Resistencia: {r:8.4f} Ω")

# 2. Generación de curva de respuesta continua
rango_temp = np.linspace(-200, 660, 500) # Rango estándar de operación
rango_resistencias = resistencia_pt100(rango_temp)

# 3. Visualización gráfica de la curva característica
plt.figure(figsize=(9, 5))
plt.plot(rango_temp, rango_resistencias, color='#1f77b4', linewidth=2, label='Curva PT100 (IEC 60751)')
plt.axhline(100, color='red', linestyle='--', alpha=0.6, label='R0 = 100 Ω (0 °C)')
plt.axvline(0, color='red', linestyle='--', alpha=0.6)

plt.title('Curva Característica de Temperatura vs Resistencia (RTD PT100)', fontsize=12, fontweight='bold')
plt.xlabel('Temperatura (°C)', fontsize=10)
plt.ylabel('Resistencia (Ω)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()

# Muestra la gráfica directamente en la celda del notebook
plt.show()