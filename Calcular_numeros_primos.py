## Validar si el numero ingresado es primo
esPrimo = True
numero = int(input("Ingrese un numero para verificar si es o no numero primo: "))
for i in range(2, numero):
    if (numero % i) == 0:
        esPrimo = False
        break
if esPrimo:
    print("es primo")
else:
    print("no es primo")
