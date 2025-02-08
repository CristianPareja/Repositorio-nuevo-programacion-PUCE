meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

categorias = ["Salud", "Alimentación", "Transporte", "Recreación", "Ahorro"]

presupuesto = [0] * len(categorias)  # Lista para almacenar el presupuesto por categoría
gastos_mes = []  # Lista para almacenar los gastos


def ingresar_presupuesto():
    for i, categoria in enumerate(categorias):
        while True:
            try:
                valor = float(input(f"Ingrese el presupuesto para {categoria}: "))
                if valor < 0:
                    print("Presupuesto no válido.")
                else:
                    presupuesto[i] = valor
                    break
            except ValueError:
                print("Ingrese un número válido.")


def ingresar_gastos():
    try:
        mes = int(input("Ingrese el mes (1-12): ")) - 1
        if mes not in range(12):
            print("Mes no válido.")
            return
        
        for i, categoria in enumerate(categorias):
            valor = float(input(f"Ingrese el gasto para {categoria}: "))
            if valor >= 0:
                gastos_mes.append([mes, i, valor])
            else:
                print("Gasto no válido.")
    except ValueError:
        print("Ingrese un número válido.")


def mostrar_gastos():
    if not gastos_mes:
        print("No hay gastos registrados.")
        return
    
    for mes in range(12):
        gastos_filtrados = [g for g in gastos_mes if g[0] == mes]
        if gastos_filtrados:
            print(f"\nGastos de {meses[mes]}:")
            total = sum(g[2] for g in gastos_filtrados)
            for g in gastos_filtrados:
                print(f"{categorias[g[1]]}: ${g[2]:.2f}")
            print(f"Total: ${total:.2f}")


def analizar_gastos_mensuales():
    try:
        mes = int(input("Ingrese el mes (1-12): ")) - 1
        if mes not in range(12):
            print("Mes no válido.")
            return
        
        gastos_filtrados = [g for g in gastos_mes if g[0] == mes]
        if not gastos_filtrados:
            print("No hay gastos para este mes.")
            return
        
        print(f"\nAnálisis de {meses[mes]}:")
        for g in gastos_filtrados:
            diferencia = presupuesto[g[1]] - g[2]
            print(f"{categorias[g[1]]}: Presupuesto ${presupuesto[g[1]]:.2f} - Gasto ${g[2]:.2f} = Diferencia ${diferencia:.2f}")
    except ValueError:
        print("Ingrese un número válido.")


def analizar_gastos_anuales():
    total_anual = sum(g[2] for g in gastos_mes)
    print(f"\nGasto total anual: ${total_anual:.2f}")
    
    for i, categoria in enumerate(categorias):
        total_categoria = sum(g[2] for g in gastos_mes if g[1] == i)
        presupuesto_total = presupuesto[i] * 12
        diferencia = presupuesto_total - total_categoria
        print(f"{categoria}: Presupuesto anual ${presupuesto_total:.2f} - Gasto ${total_categoria:.2f} = Diferencia ${diferencia:.2f}")


def main():
    while True:
        try:
            opcion = int(input("""
1. Ingresar Presupuesto
2. Ingresar Gastos Mensuales
3. Mostrar Gastos Mensuales
4. Analizar Gastos Mensuales
5. Analizar Gastos Anuales
6. Salir
Seleccione una opción: """))
            
            if opcion == 1:
                ingresar_presupuesto()
            elif opcion == 2:
                ingresar_gastos()
            elif opcion == 3:
                mostrar_gastos()
            elif opcion == 4:
                analizar_gastos_mensuales()
            elif opcion == 5:
                analizar_gastos_anuales()
            elif opcion == 6:
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Ingrese un número válido.")


main()
