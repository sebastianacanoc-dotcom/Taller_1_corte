import numpy as np
import matplotlib.pyplot as plt

# Constantes del sensor 
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Rango de temperaturas desde -200 °C hasta 200 °C, no se tiene en cuenta el ultimo numero
# , 1 es el paso
temperaturas = np.arange(-200, 201, 1)

#Lista resistencias 
resistencias = []

# Cálculo de resistencia para cada temperatura
for T in temperaturas:

    # Temperaturas menores a 0 °C
    if T < 0:
        R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)

    # Temperaturas mayores o iguales a 0 °C
    else:
        R = R0 * (1 + A*T + B*T**2)

    # Guardar resistencia calculada
    resistencias.append(R)

# Gráfica
plt.plot(temperaturas, resistencias)

# Configuración de la gráfica
plt.title("COMPORTAMIENTO SENSOR PT100")
plt.xlabel("Temperatura [°C]")
plt.ylabel("Resistencia [Ω]")
plt.grid()

# Mostrar gráfica
plt.show()