## adivinar un numero. Si numero es menor a secreto, frio frio estas muy abajo, si numero es mayor a secreto frio frio estas muy arriba
num_secreto = 71
numero = int(
    input("Prueba suerte ingresando un numero, si adivinas te llevas un premio!!: ")
)
decision = True
while decision:
    while abs(numero - num_secreto) <= 10 and numero != num_secreto:
        numero = int(input("Caliente Caliente!! ya casi lo logras. Intenta de nuevo: "))
    if numero < num_secreto:
        numero = int(
            input(
                "Frio Frio!! estas muy por debajo del numero secreto. Intenta de nuevo: "
            )
        )

    elif numero > num_secreto:
        numero = int(
            input("Frio Frio!! estas por encima del numero secreto. Intenta de nuevo: ")
        )
    if numero == num_secreto:
        decision = False
        print("FELICIDADES!! adivinaste el numero")
        print(" /\_/\ ")
        print("( o.o ) ")
        print(" > ^ < ")
