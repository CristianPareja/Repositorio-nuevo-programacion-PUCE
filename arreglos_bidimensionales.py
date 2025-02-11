# arreglo= [1,2,3]
# matriz=[[1,2,3],[4,5,6]]
# print(matriz)
# aux= matriz[1][2] #coge el valor de 6 de la lista
# print(aux)
filas=3
columnas=2
matriz=[[0 for _ in range(columnas)]for _ in range(filas)] #para que el usuario ingrese el tamano de la matriz 
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        valor=int(input(f"ingrese el valor para ({i},{j}): ")) #para que el usuario ingrese los valores de la matriz 
        matriz[i][j]=valor
for i in range(len(matriz)):
    print(matriz[i])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("posicion: ",i,",",j)
        print(matriz[i][j]) #imprime todos los valores, uno por uno, de la lista

