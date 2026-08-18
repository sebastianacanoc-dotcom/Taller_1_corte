# ==============================================================================
# C. Uso de las funciones para graficar
# ==============================================================================
# Punto 2. Realice un programa que le permita al usuario ingresar los
# coeficientes de una función de transferencia de segundo orden y graficar su
# comportamiento, además se debe mostrar que tipo de sistema es: subamortiguado,
# criticamente amortiguado y sobreamortiguado.
# ==============================================================================
# 1. INSTALACIÓN Y CARGA DE LIBRERÍAS
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal # Módulo específico para sistemas de control

# ==============================================================================
# 2. DEFINICIÓN DE FUNCIONES
# ==============================================================================

def obtener_coeficientes():
    """
    Solicita al usuario los coeficientes de la ecuación característica
    del denominador: as^2 + bs + c.
    También solicita el numerador (ganancia o constante).
    """
    print("\n--- Ingreso de parámetros de la Función de Transferencia ---")
    print("Forma: H(s) = K / (as^2 + bs + c)")
    try:
        k = float(input("Ingrese el numerador (K): "))
        a = float(input("Ingrese coeficiente 'a' (s^2): "))
        b = float(input("Ingrese coeficiente 'b' (s): "))
        c = float(input("Ingrese coeficiente 'c' (constante): "))

        if a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero para un sistema de segundo orden.")

        return k, a, b, c
    except ValueError as e:
        print(f"[Error de Entrada]: {e}")
        return obtener_coeficientes() # Reintenta si hay error

def analizar_sistema(a, b, c):
    """
    Calcula zeta y determina el tipo de sistema.
    """
    # De la forma estándar: s^2 + 2*zeta*wn*s + wn^2
    # Normalizamos el polinomio dividiendo por 'a': s^2 + (b/a)s + (c/a)

    wn_cuadrado = c / a

    if wn_cuadrado <= 0:
        return None, "Inestable o No Válido (Wn^2 <= 0)"

    wn = np.sqrt(wn_cuadrado)
    # 2 * zeta * wn = b / a
    zeta = b / (2 * a * wn)

    tipo = ""
    if zeta > 1:
        tipo = "Sobreamortiguado"
    elif zeta == 1:
        tipo = "Críticamente amortiguado"
    elif zeta > 0:
        tipo = "Subamortiguado"
    elif zeta == 0:
        tipo = "No amortiguado"
    else:
        tipo = "Inestable (Amortiguamiento negativo)"

    return zeta, tipo

def graficar_respuesta(k, a, b, c, zeta, tipo):
    """
    Calcula la respuesta al escalón y genera la gráfica.
    """
    # Definimos la función de transferencia H(s) = num / den
    # scipy.signal usa listas de coeficientes en orden descendente de 's'
    num = [k]
    den = [a, b, c]

    sistema = signal.TransferFunction(num, den)

    # Calculamos la respuesta al escalón automático (step)
    # Scipy decide el vector de tiempo adecuado automáticamente
    t, y = signal.step(sistema)

    # Configuración de la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label='Respuesta al Escalón', color='#1f77b4', linewidth=2.5)

    # Línea de valor final (Estado Estable)
    valor_final = k / c if c != 0 else 0
    if tipo != "Inestable (Amortiguamiento negativo)" and tipo != "No amortiguado":
        plt.axhline(y=valor_final, color='red', linestyle='--', alpha=0.7, label=f'Valor Final ({valor_final:.2f})')

    # Títulos y Etiquetas
    plt.title(f'Respuesta Temporal del Sistema de 2do Orden\nTipo: {tipo} ($\zeta = {zeta:.3f}$)', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (segundos)', fontsize=12)
    plt.ylabel('Amplitud de Salida', fontsize=12)

    # Detalles visuales
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='best')
    plt.tight_layout()

    # Mostrar gráfica
    print("\nGenerando gráfica... cierre la ventana de la gráfica para continuar.")
    plt.show()

# ==============================================================================
# 3. PROGRAMA PRINCIPAL (FLUJO)
# ==============================================================================

if __name__ == "__main__":
    print("==================================================")
    print("  ANALIZADOR DE SISTEMAS DE SEGUNDO ORDEN")
    print("==================================================")

    # 1. Obtener datos
    k, a, b, c = obtener_coeficientes()

    # 2. Analizar
    zeta, tipo = analizar_sistema(a, b, c)

    if zeta is not None:
        print("\n--------------------------------------------------")
        print(f"RESULTADOS DEL ANÁLISIS:")
        print(f" Factor de amortiguamiento ($\zeta$): {zeta:.4f}")
        print(f" Tipo de sistema: {tipo.upper()}")
        print("--------------------------------------------------")

        # 3. Graficar
        graficar_respuesta(k, a, b, c, zeta, tipo)
    else:
        print(f"\n[Error]: El sistema no se puede analizar: {tipo}")

    print("\nPrograma finalizado.")