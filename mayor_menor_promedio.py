##mayor_menor_promedio
print("Este programa permite que el usuario ingrese una cantidad de numeros y los categoriza por mayor, menor y el promedio ")
cantidad_num=int(input("Ingrese la cantidad de numeros a analizar: "))
mayor=None
menor=None
suma=0.0
prom=0.0
for i in range(1,cantidad_num+1):
    num_x=float(input(f"Ingrese el numero {i}: "))
    suma+=num_x
    prom=suma/cantidad_num
    if (mayor is None and menor is None):
        mayor=num_x
        menor=num_x
    else:
        if num_x>mayor:
            mayor=num_x
        if  num_x<menor:
            menor=num_x
    
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
print(f"El promedio es: {prom}")
