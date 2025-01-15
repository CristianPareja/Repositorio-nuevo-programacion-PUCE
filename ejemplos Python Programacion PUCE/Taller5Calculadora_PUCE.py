print("!Bienvenido a tu primera calculadora en Python!")
resultado = 0.0

while True:
    print("1. SUMA\n2. RESTA\n3. MULTIPLICACION\n4. DIVISION ")
    operacion = int(
        input("Digita el numero que corresponde a la operacion que deseas realizar: ")
    )

    if operacion in [1, 2, 3, 4]:
        dig1 = float(input("Ingrese el primer numero: "))
        dig2 = float(input("Ingrese el segundo numero: "))
        match operacion:
            case 1:
                resultado = dig1 + dig2
                print(resultado)
            case 2:
                resultado = dig1 - dig2
                print(resultado)
            case 3:
                resultado = dig1 * dig2
                print(resultado)
            case 4:
                while dig2 == 0:
                    dig2 = float(
                        input(
                            "No se puede realizar la division para cero (0); porfavor ingresa un valor diferente de cero: "
                        )
                    )
                resultado = dig1 / dig2
                print(resultado)
    else:
        print("Operacion incorrecta")
    decision = input(
        "Digita 's' si deseas realizar otra operacion o 'n' si deseas salir: "
    )
    if decision != "s":
        print("Gracias por usar tu primera calculadora.")
        break
