class CineTicketApp:
    def __init__(self):
        self.funciones = [
            {"pelicula": "Dune Part 2", "horario": "14:00", "disponibles": 50},
            {"pelicula": "Spider-Man: No Way Home", "horario": "18:00", "disponibles": 40},
            {"pelicula": "Oppenheimer", "horario": "21:00", "disponibles": 30},
        ]
        self.person_types = ["Adulto", "Niño", "Tercera Edad"]
        self.seat_types = ["Normal", "VIP"]
        self.prices = {
            "Adulto": {"Normal": 8, "VIP": 12},
            "Niño": {"Normal": 5, "VIP": 8},
            "Tercera Edad": {"Normal": 6, "VIP": 10}
        }
        self.iva_rate = 0.14
        self.group_discount = 0.10  
        self.promotions = {"14:00": "2x1 antes de las 3"}
        self.snacks = {"Palomitas + Refresco": 5, "Nachos + Refresco": 6}
    
    def seleccionar_funcion(self):
        while True:
            print("Funciones disponibles:")
            for i, funcion in enumerate(self.funciones):
                promo = f" - {self.promotions[funcion['horario']]}" if funcion['horario'] in self.promotions else ""
                print(f"{i+1}. {funcion['pelicula']} - {funcion['horario']} ({funcion['disponibles']} disponibles){promo}")
            try:
                seleccion = int(input("Seleccione la función: ")) - 1
                if 0 <= seleccion < len(self.funciones):
                    return self.funciones[seleccion]
                else:
                    print("Número inválido, intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
    
    def comprar_boletos(self, funcion):
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de boletos: "))
                if cantidad > 0 and cantidad <= funcion["disponibles"]:
                    funcion["disponibles"] -= cantidad
                    return cantidad
                print("Cantidad inválida o insuficiente.")
            except ValueError:
                print("Entrada inválida.")
    
    def seleccionar_boletos(self, cantidad):
        boletos = []
        for i in range(cantidad):
            print(f"Boleto {i+1}")
            persona = input("Tipo de persona (Adulto, Niño, Tercera Edad): ").capitalize()
            asiento = input("Tipo de asiento (Normal, VIP): ").capitalize()
            boletos.append({"tipo": persona, "asiento": asiento})
        return boletos
    
    def calcular_precio(self, boletos, funcion):
        total = 0
        for boleto in boletos:
            precio = self.prices[boleto["tipo"]][boleto["asiento"]]
            print(f"{boleto['tipo']} en {boleto['asiento']}: ${precio}")
            total += precio
        if len(boletos) >= 5:
            descuento = total * self.group_discount
            total -= descuento
            print(f"Descuento de grupo aplicado: -${descuento}")
        iva = total * self.iva_rate
        total_final = total + iva
        print(f"Total antes de IVA: ${total}")
        print(f"IVA: ${iva}")
        print(f"Total a pagar: ${total_final}")
        return total_final
    
    def comprar_snacks(self):
        total_snacks = 0
        print("Menú de snacks:")
        for snack, precio in self.snacks.items():
            print(f"{snack}: ${precio}")
        while True:
            snack = input("Ingrese el snack que desea (o 'No' para omitir): ")
            if snack.lower() == "no":
                break
            elif snack in self.snacks:
                total_snacks += self.snacks[snack]
                print(f"{snack} agregado por ${self.snacks[snack]}")
            else:
                print("Snack no válido, intente nuevamente.")
        return total_snacks
    
    def imprimir_resumen(self, funcion, total_boletos, total_snacks):
        print("\nResumen de compra:")
        print(f"Función: {funcion['pelicula']} - {funcion['horario']}")
        print(f"Total boletos: ${total_boletos}")
        print(f"Total snacks: ${total_snacks}")
        print(f"Total a pagar: ${total_boletos + total_snacks}")
    
    def run(self):
        funcion = self.seleccionar_funcion()
        cantidad = self.comprar_boletos(funcion)
        boletos = self.seleccionar_boletos(cantidad)
        total_boletos = self.calcular_precio(boletos, funcion)
        total_snacks = self.comprar_snacks()
        self.imprimir_resumen(funcion, total_boletos, total_snacks)

if __name__ == "__main__":
    app = CineTicketApp()
    app.run()
