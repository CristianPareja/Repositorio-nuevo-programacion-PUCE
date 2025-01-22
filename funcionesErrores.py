def LeerNumero(mensaje):
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Ingrese un numero valido")
        except Exception as e:
            print(f"Ha ocurrido un error en el proceso de lectura del numero {e}")
   
def InicializarMatriz(filas,columnas):
    matriz = [[0 for _ in range (columnas)] for _ in range(filas)]
    return matriz

def CrearMatriz():
    try: 
        filas= LeerNumero("Ingrese el numer de filas:")
        columnas= LeerNumero("Ingrese el numer de columnas:")
        matriz=InicializarMatriz(filas,columnas)
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                matriz [i][j]=LeerNumero(f"Ingrese el numero para la posicion {i},{j}: ")
        return matriz
    except IndexError:
        print("Posicion no existe en el arreglo")
    except Exception as e:
        print(f"Ha ocurrido un error al crear la matriz {e}")

matriz = CrearMatriz()
print(matriz)