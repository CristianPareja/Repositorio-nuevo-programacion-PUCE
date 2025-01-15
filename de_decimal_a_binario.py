##de decimal a binario
numero=int(input("ingrese un numero entero: "))
valorDividir=numero
resultado=""
while True:
    if(valorDividir>1):
        residuo=str(valorDividir%2)
    else:
        residuo=str(valorDividir)

    resultado=residuo+resultado
    if(valorDividir<=1):
          print(resultado)
          break
    valorDividir//=2
    