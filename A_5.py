# ==============================================================================
# Taller 1 – Python (código)
# A. Sin interacción de consola
# ==============================================================================
# Punto 5 Realice en funciones las rotaciones en X, Y y Z, donde se tenga un
# parámetro de entrada (ángulo) y un parámetro de salida (matriz).
# Las transformaciones tridimensionales en espacio cartesiano se representan
# mediante matrices de rotación 3 X 3
import numpy as np

def rotacion_x(angulo_grados: float) -> np.ndarray:
    """Retorna la matriz de rotación 3x3 en el eje X para un ángulo dado en grados."""
    rad = np.radians(angulo_grados)
    cos_a, sin_a = np.cos(rad), np.sin(rad)

    return np.array([
        [1,      0,       0],
        [0,  cos_a,  -sin_a],
        [0,  sin_a,   cos_a]
    ])

def rotacion_y(angulo_grados: float) -> np.ndarray:
    """Retorna la matriz de rotación 3x3 en el eje Y para un ángulo dado en grados."""
    rad = np.radians(angulo_grados)
    cos_a, sin_a = np.cos(rad), np.sin(rad)

    return np.array([
        [ cos_a,  0,  sin_a],
        [     0,  1,      0],
        [-sin_a,  0,  cos_a]
    ])

def rotacion_z(angulo_grados: float) -> np.ndarray:
    """Retorna la matriz de rotación 3x3 en el eje Z para un ángulo dado en grados."""
    rad = np.radians(angulo_grados)
    cos_a, sin_a = np.cos(rad), np.sin(rad)

    return np.array([
        [cos_a, -sin_a,  0],
        [sin_a,  cos_a,  0],
        [    0,      0,  1]
    ])

# ==============================================================================
# PRUEBA AUTOMÁTICA (SIN INTERACCIÓN DE CONSOLA)
# ==============================================================================

angulo_prueba = 45.0  # Ángulo de prueba en grados

matriz_x = rotacion_x(angulo_prueba)
matriz_y = rotacion_y(angulo_prueba)
matriz_z = rotacion_z(angulo_prueba)

print(f"--- MATRIZ DE ROTACIÓN EN X ({angulo_prueba}°) ---")
print(np.round(matriz_x, 4))

print(f"\n--- MATRIZ DE ROTACIÓN EN Y ({angulo_prueba}°) ---")
print(np.round(matriz_y, 4))

print(f"\n--- MATRIZ DE ROTACIÓN EN Z ({angulo_prueba}°) ---")
print(np.round(matriz_z, 4))

# Ejemplo de aplicación: Rotar un punto (1, 0, 0) 45° en el eje Z
punto_original = np.array([1, 0, 0])
punto_rotado = matriz_z @ punto_original

print(f"\nPunto original: {punto_original}")
print(f"Punto rotado 45° en Z: {np.round(punto_rotado, 4)}")