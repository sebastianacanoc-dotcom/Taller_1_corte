import matplotlib.pyplot as plt

print("Graficador de Vectores en 3D")
vx = float(input("Ingrese la componente X del vector: "))
vy = float(input("Ingrese la componente Y del vector: "))
vz = float(input("Ingrese la componente Z del vector: "))

# Crear la figura 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Dibujar el vector desde el origen (0, 0, 0) hasta (vx, vy, vz)
ax.quiver(0, 0, 0, vx, vy, vz, color='b', arrow_length_ratio=0.1, linewidth=2)

# Determinar límites de los ejes dinámicamente
max_val = max(abs(vx), abs(vy), abs(vz), 1.0)
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Etiquetas y títulos
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title(f'Vector 3D: [{vx}, {vy}, {vz}]')

# Configurar vista inicial y grilla
ax.grid(True)
plt.show()