import math

# Parámetros en SI
presion_pascales = 600000.0  # 6 Bar en Pascales (N/m^2)
diametro_embolo_m = 0.05    # diámetro del émbolo en m
diametro_vastago_m = 0.02   # diámetro del vástago en m

# Cálculo de áreas (m^2)
area_embolo = (math.pi / 4) * (diametro_embolo_m ** 2)
area_vastago = (math.pi / 4) * (diametro_vastago_m ** 2)
area_retroceso = area_embolo - area_vastago

# Cálculo de fuerzas (Newtons)
fuerza_avance = presion_pascales * area_embolo
fuerza_retroceso = presion_pascales * area_retroceso

print(f"Presión de trabajo: {presion_pascales / 100000:.1f} bar")
print(f"Fuerza de avance: {fuerza_avance:.2f} N")
print(f"Fuerza de retroceso: {fuerza_retroceso:.2f} N")