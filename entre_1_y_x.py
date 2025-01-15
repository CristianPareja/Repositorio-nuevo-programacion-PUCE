## Entre el numero 1 y X que es ingresado por el usuario: sumar los pares, multiplicar los impares e imprimir los primos e imprimir los resultado
numero = int(
    input(
        "Ingrese un numero para determinar la suma de los pares, la multiplicacion de los impares e imprimir los numero primos entre el 1 y su numero ingresado: "
    )
)
pares = 0
impares = 1
primo = []
for i in range(1, numero + 1):
    if i % 2 == 0:
        pares = pares + i
    else:
        impares = impares * i
    esPrimo = True
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if (i % j) == 0:
                esPrimo = False
                break
        if esPrimo:
            primo.append(i)

print(f"suma de pares= {pares}")
print(f"multiplicacion de impares= {impares}")
print(f"Son primos: {primo}")
