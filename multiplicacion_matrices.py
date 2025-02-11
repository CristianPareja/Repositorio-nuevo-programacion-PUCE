##Dimensiones dinamicas filas y columnas y validacion de filas de B == columnas de A
filasA=int(input("Ingrese el numero de Filas de la matriz A: "))
columnasA=int(input("Ingrese el numero de Columnas de la matriz A: "))
matrizA=[[0 for _ in range(columnasA)]for _ in range(filasA)]
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        valor=int(input(f"Ingrese el valor para la matriz A ({i},{j}): "))
        matrizA[i][j]=valor
for i in range(len(matrizA)):
    print(matrizA[i])

filasB=int(input("Ingrese el numero de Filas de la matriz B: "))
while filasB!=columnasA:
    filasB=int(input("El numero de filas de B debe ser igual al numero de columnas de A. Ingrese el numero de Filas de la matriz B: "))
columnasB=int(input("Ingrese el numero de Columnas de la matriz B: "))
matrizB=[[0 for _ in range(columnasB)]for _ in range(filasB)]
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        valor=int(input(f"Ingrese el valor para la matriz B ({i},{j}): "))
        matrizB[i][j]=valor
for i in range(len(matrizB)):
    print(matrizB[i])

##multiplicar matriz A por matrix B

matrizC=[[0 for _ in range(columnasB)]for _ in range(filasA)]
for i in range(filasA): 
    for j in range(columnasB): 
        for k in range(columnasA): 
            matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

## imprimir la matriz resultante
print("Matriz C:")
for i in range(len(matrizC)):
    print(matrizA[i], "x" ,matrizB[i], "=" ,matrizC[i])