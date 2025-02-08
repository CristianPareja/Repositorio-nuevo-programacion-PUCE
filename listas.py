# lista=[1,"hola",True]
# listaCarros=[]

# listaCarros.append("Mercedes")
# print(listaCarros)

# listaCarros.append("Chevrolet")
# print(listaCarros)

# listaCarros.insert(2,"BMW")
# print(listaCarros)

# print(listaCarros.count("BMW"))


# # listaCarros.remove("BMW")
# # print(listaCarros)

# listaCarros.sort()
# print(listaCarros)
# listaCarros.sort(reverse=True)
# print(listaCarros)

plato =input("Ingrese el plato: ")
valor=float(input("Ingresa el valor: "))
cantidad=int(input("Ingrese la cantidad: "))
total=cantidad*valor

listaPedido=[]
pedido=[plato,valor,cantidad,total]
listaPedido.append(pedido)
print(listaPedido)

plato =input("Ingrese el plato: ")
valor=float(input("Ingresa el valor: "))
cantidad=int(input("Ingrese la cantidad: "))
total=cantidad*valor

pedido=[plato,valor,cantidad,total]
listaPedido.append(pedido)
print(listaPedido)

subtotal= 0
for pedido in listaPedido:
    print(pedido[3])
    subtotal+=pedido[3]
print("-----------")
print(subtotal)