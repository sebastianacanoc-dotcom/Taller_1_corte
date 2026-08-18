import os
import cv2
import matplotlib.pyplot as plt
from google.colab import drive
import numpy as np # Added numpy import for returning empty arrays

# 1. Montar Google Drive
# drive.mount('/content/drive') # Already mounted by a previous cell, uncomment if needed

# 2. Definir la ruta del directorio y los archivos
# !!! ATENCIÓN: DEBES CAMBIAR ESTA RUTA POR LA RUTA REAL DONDE TIENES TUS IMÁGENES EN GOOGLE DRIVE !!!
# Por ejemplo: '/content/drive/MyDrive/MiCarpetaDeImagenes'
folder_path = '/content/'  # <--- ACTUALIZA ESTA LÍNEA
file_chevrolet = os.path.join(folder_path, 'Chevrolet1.jpeg')
file_mazda = os.path.join(folder_path, 'Mazda1.jpeg')

def obtener_y_graficar_contornos(ruta_imagen, titulo="Contorno del Logo"):
    """
    Lee una imagen, procesa sus contornos y grafica las coordenadas (X, Y).
    """
    # Cargar la imagen
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
        return np.array([]), np.array([]) # Return empty numpy arrays on failure

    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralizado (Binarización) para separar el logo del fondo
    # Ajusta cv2.THRESH_BINARY_INV según si el fondo es claro u oscuro
    # Se agrega THRESH_OTSU para un umbralizado automático más robusto.
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontrar contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not contours:
        print(f"No se encontraron contornos en {titulo}")
        return np.array([]), np.array([]) # Return empty numpy arrays on no contours

    # Seleccionar el contorno con mayor área (asumiendo que es el logo principal)
    main_contour = max(contours, key=cv2.contourArea)

    # Extraer las coordenadas X e Y
    # El contorno devuelto por OpenCV tiene forma (N, 1, 2)
    x_coords = main_contour[:, 0, 0]
    y_coords = main_contour[:, 0, 1]

    # Graficar las coordenadas
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, color='blue', linewidth=1.5, label='Contorno detectado')

    # Invertir el eje Y porque en imágenes el origen (0,0) está en la esquina superior izquierda
    plt.gca().invert_yaxis()

    plt.title(f"Coordenadas del Contorno: {titulo}")
    plt.xlabel("Coordenada X (píxeles)")
    plt.ylabel("Coordenada Y (píxeles)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

    return x_coords, y_coords

# 3. Procesar y graficar ambos logos
# Primero, verifica que la ruta de la carpeta existe
if not os.path.exists(folder_path):
    print(f"[ADVERTENCIA]: La ruta '{folder_path}' no existe. Asegúrate de actualizar 'folder_path' con la ruta correcta a tus imágenes.")
else:
    print("Procesando logo de Chevrolet...")
    x_chevrolet, y_chevrolet = obtener_y_graficar_contornos(file_chevrolet, "Chevrolet")

    print("Procesando logo de Mazda...")
    x_mazda, y_mazda = obtener_y_graficar_contornos(file_mazda, "Mazda")

    # Puedes añadir aquí impresiones de las coordenadas si lo deseas, por ejemplo:
    # if x_chevrolet.size > 0:
    #     print(f"Primeras 5 coordenadas X para Chevrolet: {x_chevrolet[:5]}")
    #     print(f"Primeras 5 coordenadas Y para Chevrolet: {y_chevrolet[:5]}")
