## Calcular el factorial de un numero
factorial = 1
numero = int(input("Ingrese un numero para calcular el factorial: "))
for i in range(1, numero + 1, 1):
    factorial = factorial * i
print(f"factorial es: {factorial}")
