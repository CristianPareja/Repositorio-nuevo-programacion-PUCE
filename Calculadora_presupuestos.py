from collections import defaultdict

meses = [
    [0,'Enero'],
    [1,'Febrero'],
    [2,'Marzo'],
    [3,'Abril'],
    [4,'Mayo'],
    [5,'Junio'],
    [6,'Julio'],
    [7,'Agosto'],
    [8,'Septiembre'],
    [9,'Octubre'],
    [10,'Noviembre'],
    [11,'Diciembre']
]

categorias = [
    [0,"Salud"],
    [1,"Alimentación"],
    [2,"Trasportes"],
    [3,"Recreación"],
    [4,"Ahorro"],
]

#[[categorioa,valor]]
prespuesto=[]

# [[mes,categoria,valor]]
gastos_mes=[]

def ingresar_presupuesto():
    try:        
        for categoria in categorias:
            valor = float(input(f"Ingrese el presupuesto para la categoría {categoria[1]}: "))
            if valor < 0:
                print("Presupuesto no válido")
                return
            prespuesto.append([categoria[0],valor])
    except ValueError:
        print("Error en el ingreso de datos")

def ingresar_gastos():
        mes = int(input("Ingrese el mes (1-12): "))
        if mes < 1 or mes > 12:
            print("Mes no válido")
            return     
        for categoria in categorias:
            valor = float(input(f"Ingrese el gasto para la categoría {categoria[1]}: "))
            if valor < 0:
                print("Presupuesto no válido")
                return
            gastos_mes.append([mes-1,categoria[0],valor])

def mostrar_gastos():
    #Order por mes
    array_ordenado = sorted(gastos_mes, key=lambda x: x[0])

    # Usar defaultdict para agrupar
    grupos = defaultdict(list)

    # Agrupar por meses
    for elemento in array_ordenado:
        clave = elemento[0]  # Campo por el cual agrupar
        grupos[clave].append(elemento)


    # Mostrar los grupos
    for clave, grupo in grupos.items():
        total = 0
        print("-----------------------------")
        print(f"Gastos del mes de {meses[clave][1]}:")
        for elemento in grupo:
            print(f"{categorias[elemento[1]][1]}: $ {elemento[2]}")
            total += elemento[2]
        print(f"TOTAL: $ {total}")
        

def actualizar_gastos():
    count  = 0
    print("----------Actualizar----------")
    for elemento in gastos_mes:
        print(f"{count +1 }) {meses[elemento[0]][1]}: {categorias[elemento[1]][1]} ${elemento[2]}")
        count += 1
    indice = int(input("Seleccione la opción que desea actualizar: "))

    if(indice <0 or indice > count):
        print("La opción seleccionada no es correcta")
    else:
        mes =meses[gastos_mes[indice-1][0]][1]
        categoria =categorias[gastos_mes[indice-1][1]][1]
        valor = float(input(f"Ingrese el gasto para la categoría {categoria} del mes {mes}: "))
        gastos_mes[indice-1][2]=valor
        print("Gasto actualizado correctamente")


def analizar_gastos_mensuales():
    mes = int(input("Ingrese el mes (1-12): "))
    if mes < 1 or mes > 12:
        print("Mes no válido")
        return 

    gastos_mes_seleccionado = [gasto for gasto in gastos_mes if gasto[0] == mes-1]    
    if(len(gastos_mes_seleccionado) == 0):
        print("No hay gastos registrados para este mes")
        return
    
    for indice in range(len(gastos_mes_seleccionado)):
        valor_presupuesto = prespuesto[gastos_mes_seleccionado[indice][1]][1]
        valor_mes = gastos_mes_seleccionado[indice][2]
        print(f"{categorias[gastos_mes_seleccionado[indice][1]][1]}: {valor_presupuesto} - {valor_mes} = ${valor_presupuesto - valor_mes}")

def analizar_gastos_anuales():
    meses_unicos = set(gasto[0] for gasto in gastos_mes)
    numero_meses = len(meses_unicos)
    total = 0
    # Crear un diccionario para almacenar la suma de valores por categoría
    suma_por_categoria = {}

    # Recorrer la lista de gastos
    for gasto in gastos_mes:
        categoria = gasto[1]  # Obtener la categoría
        valor = gasto[2]      # Obtener el valor

        # Si la categoría ya existe en el diccionario, sumar el valor
        if categoria in suma_por_categoria:
            suma_por_categoria[categoria] += valor
        # Si no existe, crear una nueva entrada en el diccionario
        else:
            suma_por_categoria[categoria] = valor  

    print("-----------------------------")
    print(f"Gasto Anual:")     
    for categoria, suma in suma_por_categoria.items():
        valor_presupuesto = (prespuesto[categoria][1])*numero_meses
        valor_anual = valor_presupuesto-suma
        print(f"{categorias[categoria][1]}: {valor_presupuesto}-{suma} = ${valor_anual}")
        total += valor_anual
    print(f"TOTAL: ${total}")
def main():
    try:
        while True:
            opcion = int(input("""
        1. Ingresar Presupuesto
        2. Ingresar Gastos Mensuales
        3. Mostrar Gastros Mensuales
        4. Actualizar Gastos
        5. Analizar Gastos Mensuales
        6. Analizar Gastos Anuales
        7. Salir
        Seleccione una opción: """))
            match opcion :
                case 1:
                    ingresar_presupuesto()
                case 2:
                    ingresar_gastos()
                case 3:
                    mostrar_gastos()
                case 4:
                    actualizar_gastos()
                case 5:
                    analizar_gastos_mensuales()
                case 6:
                    analizar_gastos_anuales()
                case 7:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")
    except ValueError:
        print("Error en el ingreso de datos")

main()