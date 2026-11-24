# ==========================================
# 3. PROGRAMA PRINCIPAL MAIN_2.PY
# ==========================================
from funciones_interfaz import*
from funciones_ventas import*

def iniciar_caja():
 
    monto_total_diario = 0.0
    caja_abierta = True

    while caja_abierta:
        opcion = mostrar_menu()

        if opcion == "1":
            monto_total_diario += procesar_venta()
        elif opcion == "2":
            imprimir_separador()
            print("TOTAL ACUMULADO DEL DÍA")
            print(f"Monto acumulado: ${monto_total_diario:.0f}")
        elif opcion == "3":
            imprimir_separador()
            print("CERRAR CAJA Y SALIR")
            print(f"Balance final del día: ${monto_total_diario:.0f}")
            print("Gracias por usar el sistema de 'Sabor Urbano'. ¡Hasta luego!")
            caja_abierta = False
        else:
            print("Opción no válida, por favor ingrese 1, 2 o 3.")

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_caja()
