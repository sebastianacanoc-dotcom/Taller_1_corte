"""
B.4 - Selección de tipo de robot (Cilindrico, Cartesiano, Esferico)
"""

print("Seleccione el tipo de robot:")
print("1. Cilíndrico")
print("2. Cartesiano")
print("3. Esférico")

opcion = input("Ingrese el numero de opción: ")

if opcion == "1":
    print("\nRobot CILINDRICO")
    print("Configuracion de articulaciones: R-P-P")
    print("- 1 articulación rotacional (base)")
    print("- 2 articulaciones prismáticas (lineales)")
    print("Número total de articulaciones: 3")

elif opcion == "2":
    print("\nRobot CARTESIANO")
    print("Configuración de articulaciones: P-P-P")
    print("- 3 articulaciones prismáticas (ejes X, Y, Z)")
    print("Número total de articulaciones: 3")

elif opcion == "3":
    print("\nRobot ESFERICO (polar)")
    print("Configuración de articulaciones: R-R-P")
    print("- 2 articulaciones rotacionales")
    print("- 1 articulación prismática")
    print("Número total de articulaciones: 3")

else:
    print("Opción no válida. Debe ingresar 1, 2 o 3.")