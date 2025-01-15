num_base=int(input("Ingrese un numero a multiplicar: "))
inicio=int(input("Ingrese un rango minimo "))
fin=int(input("Ingrese un rango maximo "))
for i in range (inicio, fin+1):
    resultado=num_base*i
    print(f"{num_base}*{i}={resultado}")

