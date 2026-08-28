def calculo_propina(total_cuenta: float, porcentaje_p: float) -> float: 
    """Calcula el monto exacto de la propina redondeado a 2 decimales."""
    propina = total_cuenta * (porcentaje_p / 100.0)
    return round(propina, 2)

def calculo_total_por_persona(total_cuenta: float, porcentaje_p: float, num_personas: int) -> float:
    """Calcula la cuota individual a pagar incluyendo la propina equitativamente."""
    if num_personas <= 0:
        raise ValueError("Sorry, el número de personas debe ser mayor a 0.")
    
    monto_propina = calculo_propina(total_cuenta, porcentaje_p)
    total_general = total_cuenta + monto_propina
    cuota_individual = total_general / num_personas
    return round(cuota_individual, 2)

def formatear_factura(total_cuenta: float, propina: float, total_por_persona: float) -> str:
    """Retorna un resumen formateado de la cuenta con formato monetario $X.XX."""
    gran_total = total_cuenta + propina
    return (
        f"--- RESUMEN DE TU CUENTA 🍽️ ---\n"
        f"Subtotal:         ${total_cuenta:.2f}\n"
        f"Propina:          ${propina:.2f}\n"
        f"Total a Pagar:    ${gran_total:.2f}\n"
        f"Cuota Individual: ${total_por_persona:.2f}"
    )

if __name__ == "__main__":
    print("=" * 60)
    print("CALCULA AQUÍ TU PROPINA Y FACTURACIÓN")
    print("=" * 60)
    try:
        entrada_cuenta = float(input("Ingrese el total de la cuenta ($): "))
        entrada_porcentaje = float(input("Ingrese el porcentaje de propina (ej. 15): "))
        entrada_personas = int(input("¿Entre cuántas personas se dividirá?: "))
        
        propina_calc = calculo_propina(entrada_cuenta, entrada_porcentaje)
        cuota_calc = calculo_total_por_persona(entrada_cuenta, entrada_porcentaje, entrada_personas)
        
        print("\n" + formatear_factura(entrada_cuenta, propina_calc, cuota_calc))
    except ValueError as err:
        print(f"⚠️ Error en la entrada de datos: {err}")