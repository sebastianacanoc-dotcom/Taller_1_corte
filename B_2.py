"""
B.2 - Genera X numeros aleatorios en un rango dado por el usuario
"""

import random

# --- Entradas por teclado ---
cantidad = int(input("¿Cuántos números aleatorios desea generar? "))
maximo = float(input("Ingrese el valor máximo del rango: "))

# Se valida que el minimo sea menor que el maximo; si no, se vuelve a pedir
while True:
    minimo = float(input("Ingrese el valor mínimo del rango: "))
    if minimo <= maximo:
        break
    print(f"Error: el mínimo ({minimo}) no puede ser mayor que el máximo ({maximo}). Intente de nuevo.\n")

# --- Generacion de numeros ---
numeros = [round(random.uniform(minimo, maximo), 3) for _ in range(cantidad)]

# --- Salida en consola ---
print(f"\nSe generaron {cantidad} números entre {minimo} y {maximo}:")
print(numeros)
print(f"Promedio: {sum(numeros)/len(numeros):.3f}")
