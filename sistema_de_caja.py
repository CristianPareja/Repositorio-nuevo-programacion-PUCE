##sistema_de_caja
print("Este programa permite que el usuario ingrese la cantidad de productos y el precio unitario sin IVA y determina el total de productos, el subtotal con el IVA (15%) y el valor total a pagar")
decision=True
total_cantidad=0
subtotal_individual=0.0
valor_sin_iva=0.0
valor_con_iva=0.0
total_a_pagar=0.0

while decision:
    confirmacion=input("Desea ingresar productos? Digite s para 'si' o n para 'no'")
    if confirmacion=="s":
        cantidad_prod=int(input("Ingrese la cantidad de productos: "))
        valor_prod=float(input("Ingrese el precio unitario del producto: $ " ))
        print(cantidad_prod)
        print(valor_prod)
        total_cantidad+=cantidad_prod
        subtotal_individual=cantidad_prod*valor_prod
        valor_sin_iva+=subtotal_individual
        valor_con_iva=valor_sin_iva*0.15
        total_a_pagar=valor_sin_iva+valor_con_iva
    else:
        if confirmacion=='n':
            decision=False
    
print(f"cantidad de productos: {total_cantidad}")
print(f"subtotal sin IVA: ${valor_sin_iva}")
print(f"IVA: ${valor_con_iva}")
print(f"total a pagar: ${total_a_pagar}")



    