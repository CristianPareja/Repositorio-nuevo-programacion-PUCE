##de decimal a hexadecimal
numero=int(input("ingrese un numero entero: "))
valorDividir=numero
resultado=""
while True:
    if(valorDividir>15):
        residuo=(valorDividir%16)
    else:
        residuo=(valorDividir)
    match residuo:
         case 10:
              residuo="A"
         case 11:
              residuo="B"
         case 12:
              residuo="C"
         case 13:
              residuo="D"
         case 14:
              residuo="E"
         case 15:
              residuo="F"
         case _:
              residuo=str(residuo)
    resultado=residuo+resultado
    
    if(valorDividir<=1):
          print(resultado)
          break
    valorDividir//=16
    