def imprimir_separador():
    """Imprime una línea divisoria estándar en toda la interfaz."""
    print("-" * 30)

def mostrar_menu():
    """Muestra las opciones principales y retorna la elección del usuario."""
    imprimir_separador()
    print("MENÚ PRINCIPAL - SABOR URBANO")
    print("1. Registrar Venta")
    print("2. Ver total acumulado del día")
    print("3. Cerrar caja y salir")
    return input("Ingrese opción: ")
