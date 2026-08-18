# ==============================================================================
# B. Con interacción de consola (fprintf o disp) y teclado (input)
# ==============================================================================
# Punto 1. Realice un programa que calcule la potencia que consume un circuito
# ingresando por teclado el valor de corriente y voltaje.
# La fórmula básica para el cálculo de la potencia eléctrica consumida en un
# circuito de corriente continua (DC) o circuito de corriente alterna (AC)
# puramente resistivo es:  P = V * I
# Donde:P es la potencia en vatios (W)
# V es el voltaje en voltios (V}
# I es la corriente en amperios (A).
# ==============================================================================
def calcular_potencia():
    print("==========================================")
    print("    CÁLCULO DE POTENCIA EN UN CIRCUITO    ")
    print("==========================================")

    try:
        # Lectura de datos por teclado (input)
        voltaje_input = input("Ingrese el valor del voltaje (V en voltios): ")
        voltaje = float(voltaje_input)

        corriente_input = input("Ingrese el valor de la corriente (I en amperios): ")
        corriente = float(corriente_input)

        # Cálculo de la potencia
        potencia = voltaje * corriente

        # Salida formateada por consola (equivalente a fprintf / disp)
        print("\n------------------------------------------")
        print("RESULTADOS:")
        print(f" Voltaje (V)   : {voltaje:.2f} V")
        print(f" Corriente (I) : {corriente:.2f} A")
        print(f" Potencia (P)  : {potencia:.2f} W")
        print("------------------------------------------")

        # Conversión adicional a kW si el valor es alto
        if potencia >= 1000:
            print(f" Equivalente   : {potencia / 1000:.3f} kW")

    except ValueError:
        print("\n[Error]: Debe ingresar números válidos para el voltaje y la corriente.")

# ==============================================================================
# EJECUCIÓN
# ==============================================================================
if __name__ == "__main__":
    calcular_potencia()