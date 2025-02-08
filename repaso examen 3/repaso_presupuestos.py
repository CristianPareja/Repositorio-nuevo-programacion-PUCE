categorias=["salud","alimentacion","transporte","recreacion"]
# presupuesto=[categoria,valor]
presupuesto=[]
# gasto=[mes,categoria,valor]
gastos=[]



def agregarPresupuesto():
    try:
        for categoria in categorias:
            valor=float(input(f"Ingrese valor del presupuesto para {categoria}: "))
            presupuesto.append([categoria,valor])
    except ValueError:
        print("Ingrese un numero valido")
    except Exception as e:
        print(f"ocurrio un error: {e}")


def agregarGastos():
    try:
        mes=int(input("ingrese el mes (1-12): "))
        for categoria in categorias:
            valor=float(input(f"Ingrese valor del presupuesto para {categoria}: "))
            gastos.append([mes,categoria,valor])
    except ValueError:
        print("Ingrese un numero valido")
    except Exception as e:
        print(f"ocurrio un error: {e}")


def mostrarGastosPorMes():
    pass


while True:
    try:
        print("1. Agregar presupuesto")
        print("2. Agregar gasto")
        print("3. Mostrar gastos por mes")
        opcion=int(input("seleccione una opcion: "))

        match opcion:
            case 1:
                agregarPresupuesto()
                print(presupuesto)
            case 2:
                agregarGastos()
                print(gastos)
            case 3:
                mostrarGastosPorMes()
    except ValueError:
        print("Ingrese un numero valido")
    except Exception as e:
        print(f"ocurrio un error: {e}")
