def ingresar_productos():
    """Pide precios al usuario hasta escribir 'fin' o '0'. Retorna el subtotal."""
    print("REGISTRO DE VENTAS")
    subtotal = 0.0
    while True:
        entrada = input("Ingrese precio (o 'fin' para terminar): ")
        if entrada == "0" or entrada.lower() == "fin":
            return subtotal  # Retorno temprano para salir limpio del ciclo
        
        try:
            precio = float(entrada)
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
            else:
                subtotal += precio
        except ValueError:
            print("Error: Ingrese un número válido o 'fin' para terminar.")

def seleccionar_metodo_pago():
    """Valida y retorna '1' (Efectivo) o '2' (Tarjeta)."""
    imprimir_separador()
    print("--- Método de pago ---")
    
def seleccionar_metodo_pago():
    """Valida y retorna '1' (Efectivo) o '2' (Tarjeta)."""
    imprimir_separador()
    print("--- Método de pago ---")

    metodo_pago = ""

    while metodo_pago not in ["1", "2"]:
        metodo_pago = input("1. Efectivo\n2. Tarjeta\nOpción: ")

        if metodo_pago not in ["1", "2"]:
            print("Opción inválida. Seleccione 1 o 2.")

    return metodo_pago
    pass

def calcular_totales(subtotal, metodo_pago):
    """Calcula IVA, descuento y total final. Retorna el total_final."""
monto_iva = subtotal_cliente * 0.19
total_iva_cliente = subtotal_cliente + monto_iva
   descuento = 0.0

if metodo_pago == "1":
    descuento = total_iva * 0.05

total_final = total_iva - descuento
  imprimir_separador()
print("DETALLE DE LA BOLETA")
print(f"Subtotal: ${subtotal:.0f}")
print(f"IVA (19%): ${monto_iva:.0f}")
print(f"Total con IVA: ${total_iva:.0f}")

if metodo_pago == "1":
    print(f"Descuento efectivo (5%): ${descuento:.0f}")

print(f"TOTAL FINAL: ${total_final:.0f}
if total_final > 15000:
    print("Clasificación: Venta Alta")
else:
    print("Clasificación: Venta Habitual")
    monto_total_diario = monto_total_diario + total_final_cliente
    pass

def procesar_venta():
    """Orquesta el flujo completo de una venta y retorna el monto final."""
    subtotal = ingresar_productos()
    if subtotal == 0:
        print("Venta cancelada (monto $0).")
        return 0.0
    
    metodo = seleccionar_metodo_pago()
    total_venta = calcular_totales(subtotal, metodo)
    return total_venta
metodo = seleccionar_metodo_pago()
    total_venta = calcular_totales(subtotal, metodo)

    