print("----------------------------------------Calculadora de matrices-------------------------------------------") 

def CrearMatriz(nombre=" "):
    filas=int(input(f"Ingrese el numero de Filas de {nombre}: "))
    columnas=int(input(f"Ingrese el numero de Columnas de {nombre}: "))
    matriz=[[0 for _ in range(columnas)]for _ in range(filas)]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor=int(input(f"Ingrese el valor de la fila {i+1} y columna {j+1} en la {nombre}: "))
            matriz[i][j]=valor
    print (f"{nombre} almacenada:")
    for i in range(len(matriz)):
        print(matriz[i])
    return matriz

def Imprimiropcion():
    opcionelegida = int(input("Escoge la opción que deseas realizar:\n(1) Ingresar Matriz A\n(2) Ingresar Matriz B\n(3) Sumar matrices\n(4) Multiplicar matrices\n(5) Matriz Transpuesta A\n(6) Matriz Transpuesta B\n")) 
    return opcionelegida

def ExistenciaMatrices():
    global MatrizA, MatrizB
    if MatrizA is None or MatrizB is None: 
                print("!No existen las matrices! Ingresar los valores de las Matrices A y B (opciones 1 y 2)") 
                return False 
    return True

def SumaMatrices(matrizA, matrizB): 
    if len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0]): 
        print("Las matrices no tienen el mismo tamaño, modifica las matrices A y B para que tengan la misma dimension")
        return Imprimiropcion()
    matrizC = [[0] * len(matrizA[0]) for _ in range(len(matrizA))] 
    for i in range(len(matrizC)): 
        for j in range(len(matrizC[0])): 
             matrizC[i][j] = matrizA[i][j] + matrizB[i][j] 
    for i in range(len(matrizC)): 
        print(matrizA[i], "+", matrizB[i], "=", matrizC[i]) 
    return matrizC

def MultiplicacionMatrices(matrizA, matrizB):
    while len(matrizB[0])!=len(MatrizA):
        print("El numero de filas de B debe ser igual al numero de columnas de A. Ingrese nuevamente la matriz B (opcion 2)")
        return Imprimiropcion()
    matrizC=[[0 for _ in range(len(MatrizB))]for _ in range(len(MatrizA[0]))]
    for i in range(len(MatrizA[0])): 
        for j in range(len(MatrizB)): 
            for k in range(len(MatrizA)): 
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    for i in range(len(matrizC)):
        print(matrizA[i], "x" ,matrizB[i], "=" ,matrizC[i]) 
    return matrizC  

def Transpuesta(matriz):
     transMatriz=[[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
     for i in range(len(matriz)): 
        for j in range(len(matriz[0])): 
            transMatriz[j][i] = matriz[i][j] 
     for i in range(len(transMatriz)): 
        print(transMatriz[i]) 
     return transMatriz
        
MatrizA = None 
MatrizB = None
listaOpciones=list(range(1,6))

opcion=Imprimiropcion()
while opcion not in listaOpciones:
    print("Ingrese una opcion correcta entre 1 y 6")
    opcion=Imprimiropcion()
    while opcion in listaOpciones: 
            match opcion: 
                case 1: 
                    MatrizA = CrearMatriz("MatrizA")

                case 2: 
                    MatrizB = CrearMatriz("MatrizB")

                case 3: 
                      if ExistenciaMatrices():
                        print("-------------SUMA--------------") 
                        SumaMatrices(MatrizA,MatrizB) 

                case 4: 
                      if ExistenciaMatrices():
                        print("-------------MULTIPLICACION--------------")  
                        MultiplicacionMatrices(MatrizA,MatrizB)

                case 5: 
                      if ExistenciaMatrices():
                        print("-------------TRANSPUESTA DE A--------------") 
                        Transpuesta(MatrizA)

                case 6: 
                      if ExistenciaMatrices():
                        print("-------------TRANSPUESTA DE B--------------")  
                        Transpuesta(MatrizB)

                case _: 
                      print("!Error! La opción debe estar entre 1 y 6.")

            opcion=Imprimiropcion()                   

          