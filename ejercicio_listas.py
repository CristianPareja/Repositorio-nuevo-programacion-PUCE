def elementos_lista():
    lista = []
    while True:
        elemento = input("Ingrese los elementos de la lista o escriba 'salir' para terminar: ") 
        if elemento.lower() == "salir":  
            break
        lista.append(elemento)  
    return lista

lista_user = elementos_lista()
print("Lista:", lista_user)