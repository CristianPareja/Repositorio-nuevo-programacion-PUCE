categorias=["salud","alimentacion","transporte"]
gastos=[]
def IngresarPresupuesto():
    PresupuestoCategoria=[]
    for categoria in categorias:
        valor=float(input(f"Ingrese su presupuesto mensual para {categoria}: "))
        presupuesto=[categoria,valor]
        PresupuestoCategoria.append(presupuesto)

def IngresarGastos(mes):
    for categoria in categorias:
        valor=float(input(f"Ingrese su presupuesto del mes {mes} para {categoria}: "))
        gasto=[mes,categoria,valor]
        gastos.append(gasto)
    print(gastos)
    

def AnalizarPresupuestoMes(mes):
    for gasto in gastos:
        if gasto[0]!=mes:
            continue
    for categoria in presupuesto:
        if gasto[1]!=categoria[0]:
            continue
        print(f"Presupuesto para {categoria[0]} era de {categoria[1]}")
        print(f"valor gastado para {categoria[0]} fue de {gasto[2]}")
        gastoMensual+=gasto[2]
        presupuestoMensual+=categoria[1]

        if (gasto[2]>categoria[1]):
            print("supero el valor")
    print(f"Presuuesto total era de {presupuestoMensual}")



presupuesto=IngresarPresupuesto()

