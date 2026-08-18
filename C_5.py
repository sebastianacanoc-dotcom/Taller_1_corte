import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D


# Función para dibujar un nombre
def dibujar_nombre(ax, nombre, x, y):

    # Convertir el nombre en una geometria de lineas
    trayectoria = TextPath((0, 0), nombre, size=2)

    # Mover el nombre a la posición indicada
    transformacion = (Affine2D().translate(x, y) + ax.transData)
    
    # Crear el contorno de las letras
    contorno = PathPatch(trayectoria, transform=transformacion, fill=False)

    # Dibujar el nombre a la gráfica
    ax.add_patch(contorno)

# Lista de nombres
nombres = [
    "Emily",
    "Gerley",
    "Sebastian",
    "Gisell"
]

# Crear figura y sistema de coordenadas
fig, ax = plt.subplots()

posicion_y = 0

# Dibujar todos los nombres
for nombre in nombres:

    dibujar_nombre(ax, nombre, 0, posicion_y)
    # Aumentar la posición en el eje y
    posicion_y += 3


ax.set_title("INTEGRANTES DEL GRUPO")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_xlim(-1, 18)
ax.set_ylim(-1, posicion_y)
ax.set_aspect("equal") # Mantener proporción de los ejes
ax.grid()

plt.show()