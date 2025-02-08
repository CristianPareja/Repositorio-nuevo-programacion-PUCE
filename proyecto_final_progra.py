# Variables globales
funciones = [
    {"pelicula": "Dune Part 2", "horario": "14:00", "disponibles": 50},
    {"pelicula": "Spider-Man: No Way Home", "horario": "18:00", "disponibles": 40},
    {"pelicula": "Oppenheimer", "horario": "21:00", "disponibles": 30},
]
person_types = ["Adulto", "Niño", "Tercera Edad"]
seat_types = ["Normal", "VIP"]
prices = {
    "Adulto": {"Normal": 8, "VIP": 12},
    "Niño": {"Normal": 5, "VIP": 8},
    "Tercera Edad": {"Normal": 6, "VIP": 10}
}
iva_rate = 0.14
group_discount = 0.10
promotions = {"14:00": "2x1 antes de las 3"}
snacks = {"Palomitas + Refresco": 5, "Nachos + Refresco": 6}

def seleccionar_funcion():
    while True:
        print("Funciones disponibles:")
        for i, funcion in enumerate(funciones):
            promo = f" - {promotions[funcion['horario']]}" if funcion['horario'] in promotions else ""
            print(f"{i+1}. {funcion['pelicula']} - {funcion['horario']} ({funcion['disponibles']} disponibles){promo}")
        try:
            seleccion = int(input("Seleccione la función: ")) - 1
            if 0 <= seleccion < len(funciones):
                return funciones[seleccion]
            print("Número inválido, intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def comprar_boletos(funcion):
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletos: "))
            if cantidad > 0 and cantidad <= funcion["disponibles"]:
                funcion["disponibles"] -= cantidad
                return cantidad
            print("Cantidad inválida o insuficiente.")
        except ValueError:
            print("Entrada inválida.")

def seleccionar_boletos(cantidad):
    boletos = []
    for i in range(cantidad):
        print(f"Boleto {i+1}")
        persona = input("Tipo de persona (Adulto, Niño, Tercera Edad): ").capitalize()
        asiento = input("Tipo de asiento (Normal, VIP): ").capitalize()
        boletos.append({"tipo": persona, "asiento": asiento})
    return boletos

def calcular_precio(boletos):
    total = 0
    for boleto in boletos:
        precio = prices[boleto["tipo"]][boleto["asiento"]]
        print(f"{boleto['tipo']} en {boleto['asiento']}: ${precio}")
        total += precio
    
    if len(boletos) >= 5:
        descuento = total * group_discount
        total -= descuento
        print(f"Descuento de grupo aplicado: -${descuento}")
    
    iva = total * iva_rate
    total_final = total + iva
    print(f"Total antes de IVA: ${total}")
    print(f"IVA: ${iva}")
    print(f"Total a pagar: ${total_final}")
    return total_final

def comprar_snacks():
    total_snacks = 0
    print("Menú de snacks:")
    for snack, precio in snacks.items():
        print(f"{snack}: ${precio}")
    
    while True:
        snack = input("Ingrese el snack que desea (o 'No' para omitir): ")
        if snack.lower() == "no":
            break
        if snack in snacks:
            total_snacks += snacks[snack]
            print(f"{snack} agregado por ${snacks[snack]}")
        else:
            print("Snack no válido, intente nuevamente.")
    return total_snacks

def imprimir_resumen(funcion, total_boletos, total_snacks):
    print("\nResumen de compra:")
    print(f"Función: {funcion['pelicula']} - {funcion['horario']}")
    print(f"Total boletos: ${total_boletos}")
    print(f"Total snacks: ${total_snacks}")
    print(f"Total a pagar: ${total_boletos + total_snacks}")

def main():
    funcion_seleccionada = seleccionar_funcion()
    cantidad_boletos = comprar_boletos(funcion_seleccionada)
    boletos_seleccionados = seleccionar_boletos(cantidad_boletos)
    total_boletos = calcular_precio(boletos_seleccionados)
    total_snacks = comprar_snacks()
    imprimir_resumen(funcion_seleccionada, total_boletos, total_snacks)

if __name__ == "__main__":
    main()