print("----------------------------------------Calculadora de matrices-------------------------------------------") 

def LeerNumero(mensaje):
     while True:
          try:
               numero= int(input(mensaje+" "))
               return numero
          except ValueError:
               print("Ingrese un numero valido. Intente nuevamenente")
          except Exception as e:
               print(f"Ha ocurrido un error al leer el numero {e}")


def CrearMatriz(nombre=" "):
    try:
        filas=LeerNumero(f"Ingrese el numero de Filas de {nombre}: ")
        columnas=LeerNumero(f"Ingrese el numero de Columnas de {nombre}: ")
        matriz=[[0 for _ in range(columnas)]for _ in range(filas)]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j]=LeerNumero(f"Ingrese el valor de la fila {i+1} y columna {j+1} en la {nombre}: ")
    except IndexError:
         print("Posicion no existe en el arreglo")
    except Exception as e:
         print(f"Ha ocurrido un error al crea la matriz {nombre}")
    print (f"{nombre} almacenada:")
    for i in range(len(matriz)):
        print(matriz[i])
    return matriz

def Imprimiropcion():
    opcionelegida = int(input("Escoge la opción que deseas realizar:\n(1) Ingresar Matriz A\n(2) Ingresar Matriz B\n(3) Sumar matrices\n(4) Multiplicar matrices\n(5) Matriz Transpuesta A\n(6) Matriz Transpuesta B\n(7) Salir\nOpcion:")) 
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


opcion=Imprimiropcion()
while opcion not in [1,2,3,4,5,6,7]:
    print("Ingrese una opcion correcta entre 1 y 7")
    opcion=Imprimiropcion()
while opcion in [1,2,3,4,5,6,7]:
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
                case 7:
                      print("------------------------Gracias por utilizar la calculadora de Matrices------------------------")
                      break  
                case _: 
                      print("!Error! La opción debe estar entre 1 y 7.")

            opcion=Imprimiropcion()                   

          