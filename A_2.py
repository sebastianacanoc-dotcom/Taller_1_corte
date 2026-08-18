import numpy as np

# Matrices a trabajar
A = np.array([[2, 5, 1],
              [0, 2, 0],
              [1, 9, 7]])

B = np.array([[1, 2, 5],
              [3, 4, 9],
              [5, 6, 8]])

# Suma
suma = A + B

# Resta
resta = A - B

# Multiplicación por elementos
multiplicacion_elemento = A * B

# Producto punto
producto_matricial = A @ B

#Producto cruz
producto_cruz = np.cross(A, B)

# División 
division = A / B

# Datos en consola
print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

# Resultados
print("\nSuma A + B:")
print(suma)

print("\nResta A - B:")
print(resta)

print("\nMultiplicación por elementos A * B:")
print(multiplicacion_elemento)

print("\nProducto punto A @ B:")
print(producto_matricial)

print("\nProducto cruz (A, B):")
print(producto_cruz)

print("\nDivisión A / B:")
print(division)

