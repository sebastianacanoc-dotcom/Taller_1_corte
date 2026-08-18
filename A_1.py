"""
A.1 - Suma, resta, multiplicacion (punto y cruz) y division de vectores
"""

import numpy as np

# Vectores inicializados previamente (puedes cambiarlos)
v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])

# Suma
suma = v1 + v2

# Resta
resta = v1 - v2

# Producto punto (escalar)
producto_punto = np.dot(v1, v2)

# Producto cruz (vectorial) -> solo tiene sentido geometrico en R3
producto_cruz = np.cross(v1, v2)

# Division elemento a elemento
division = v1 / v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("-" * 40)
print("Suma       :", suma)
print("Resta      :", resta)
print("Prod. punto:", producto_punto)
print("Prod. cruz :", producto_cruz)
print("Division   :", division)
