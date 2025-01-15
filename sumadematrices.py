filas=2
columnas=2
matrizA=[[0 for _ in range(columnas)]for _ in range(filas)]
matrizB=[[0 for _ in range(columnas)]for _ in range(filas)]

#Llenar matriz A
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        valor=int(input(f"Ingrese el valor para la matriz A ({i},{j}): "))
        matrizA[i][j]=valor

#Llenar matriz B
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        valor=int(input(f"Ingrese el valor para la matriz B ({i},{j}): "))
        matrizB[i][j]=valor
print("Matriz A:")
for i in range(len(matrizA)):
    print(matrizA[i])
print("Matriz B:")
for i in range(len(matrizB)):
    print(matrizB[i])

#Suma de matrices e impresion de la matriz resultado C
matrizC=[[0 for _ in range(columnas)]for _ in range(filas)]
for i in range(len(matrizC)):
    for j in range(len(matrizC[i])):
        matrizC[i][j]=matrizA[i][j]+matrizB[i][j]
print("Matriz C:")
for i in range(len(matrizC)):
    print(matrizA[i], "+" ,matrizB[i], "=" ,matrizC[i])