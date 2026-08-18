import math

#Punto de prueba (x, y, z)
x, y, z = 3.0, 4.0, 5.0

#Conversión a Coordenadas Cilíndricas (r, theta, z)
r = math.sqrt(x**2 + y**2)
theta_rad = math.atan2(y, x)
theta_deg = math.degrees(theta_rad)

#Conversión a Coordenadas Esféricas (rho, theta, phi)
rho = math.sqrt(x**2 + y**2 + z**2)
phi_rad = math.acos(z / rho)
phi_deg = math.degrees(phi_rad)

# Resultados
print(f"Punto Rectangular: ({x}, {y}, {z})")
print(f"Cilíndricas: r = {r:.4f}, theta = {theta_deg:.2f}°, z = {z:.4f}")
print(f"Esféricas:  p = {rho:.4f}, theta = {theta_deg:.2f}°, phi = {phi_deg:.2f}°")