dimension_arreglo=int(input("Ingrese la dimension del arreglo: "))
arreglo=[0]*dimension_arreglo
for i in range(dimension_arreglo):
    arreglo[i]=int(input(f"Ingrese el valor de la posicion {i}: ")) 
print("Arreglo original : ",arreglo)
opcion=int(input("Elija 1. si quiere ordenar de forma ascendente y 2. si quiere ordenar de forma descendete: "))
match opcion:
    case 1:
        for i in range(len(arreglo)):
            print("Ordernar posicion",i)
            posicionmenor=i
            for j in range(i+1,len(arreglo)):
                print(f"{arreglo[j]} < {arreglo[posicionmenor]}")
                if arreglo[j]<arreglo[posicionmenor]:
                    posicionmenor=j
            aux=arreglo[posicionmenor]
            arreglo[posicionmenor]=arreglo[i]
            arreglo[i]=aux
        print(arreglo)
    case 2:
        for i in range(len(arreglo)):
            print("Ordernar posicion",i)
            posicionmayor=i
            for j in range(i+1,len(arreglo)):
                print(f"{arreglo[j]} > {arreglo[posicionmayor]}")
                if arreglo[j]>arreglo[posicionmayor]:
                    posicionmayor=j
            aux=arreglo[posicionmayor]
            arreglo[posicionmayor]=arreglo[i]
            arreglo[i]=aux
        print(f"posicion{i} Ordenada ")
        print(arreglo)


