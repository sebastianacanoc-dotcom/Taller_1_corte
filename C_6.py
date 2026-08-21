import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))

file_mazda = os.path.join(script_dir, 'Mazda1.jpeg')
file_toyota = os.path.join(script_dir, 'toyota-logo.png')


def extraer_y_graficar_contornos(ruta_imagen, titulo="Logo", guardar_csv=True):
    """
    Lee la imagen, extrae las coordenadas (X, Y) de todos los contornos,
    los grafica y retorna una lista de arrays con las coordenadas de cada trazo.
    """
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"Error: No se encontró la imagen en {ruta_imagen}")
        return []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Extraer todos los contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    puntos_por_contorno = []
    todos_los_puntos = []

    plt.figure(figsize=(9, 6))

    for i, contour in enumerate(contours):
        # Extraer arreglos X e Y
        x = contour[:, 0, 0]
        y = contour[:, 0, 1]

        # Guardar en las listas de retorno
        coordenadas_contorno = np.column_stack((x, y))
        puntos_por_contorno.append(coordenadas_contorno)

        # Graficar
        plt.plot(x, y, color='blue', linewidth=1)

        # Acumular para exportar
        for px, py in zip(x, y):
            todos_los_puntos.append([i + 1, px, py])

    plt.gca().invert_yaxis()
    plt.title(f"Coordenadas de TODOS los Contornos: {titulo}")
    plt.xlabel("Coordenada X (píxeles)")
    plt.ylabel("Coordenada Y (píxeles)")
    plt.grid(True, linestyle='--', alpha=0.6)

    # --- Opcional: Guardar coordenadas en archivo CSV ---
    if guardar_csv and todos_los_puntos:
        nombre_csv = os.path.join(script_dir, f"coordenadas_{titulo.lower()}.csv")
        np.savetxt(
            nombre_csv,
            todos_los_puntos,
            fmt='%d',
            delimiter=',',
            header='ID_Contorno,X,Y',
            comments=''
        )
        print(f"-> Coordenadas guardadas en: {nombre_csv}")

    plt.show()

    return puntos_por_contorno


# --- EJECUCIÓN Y USO DE LOS PUNTOS ---

print("Procesando Mazda...")
coordenadas_mazda = extraer_y_graficar_contornos(file_mazda, "Mazda")

print("\nProcesando Toyota...")
coordenadas_toyota = extraer_y_graficar_contornos(file_toyota, "Toyota")

# Ejemplo: Cómo acceder a los puntos directamente en Python
if coordenadas_mazda:
    primer_contorno = coordenadas_mazda[0]  # Array Nx2 del primer trazo
    print(f"\nTotal de contornos detectados en Mazda: {len(coordenadas_mazda)}")
    print(f"Primeros 5 puntos del Contorno 1 (X, Y):\n{primer_contorno[:5]}")
