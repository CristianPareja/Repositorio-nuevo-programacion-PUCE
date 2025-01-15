destino=int(input("Ingrese su destino (1 Ciudad A. 2 Ciudad B. 3 Ciudad C.): "))
categoria=""
tarifaDestinoA=100
tarifaDestinoB=200
tarifaDestinoC=300
tarifaEconomica=50
tarifaEjecutiva=100
tarifaPrimeraclase=150
subtotal_ind1=0
subtotal_ind2=0
subtotal_ind3=0
subtotal_grupo=0
subtotal_acumulador1=0
subtotal_acumulador2=0
subtotal_acumulador3=0
total_a_pagar=0
match destino:
    case 1:
        pasajeros=int(input("Cuantos pasajeros van a viajar: "))
        for i in range(1,pasajeros+1):
            categoria=(input(f"Ingrese la categoria (1 Economica. 2 Ejecutiva. 3 Primera clase.) que desea para el pasajero {i}: "))
            if categoria=='1':
                subtotal_ind1=(pasajeros-(pasajeros-1))*(tarifaDestinoA+tarifaEconomica)
                subtotal_acumulador1+=subtotal_ind1
            elif categoria=='2':
                subtotal_ind2=(pasajeros-(pasajeros-1))*(tarifaDestinoA+tarifaEjecutiva)
                subtotal_acumulador2+=subtotal_ind2
            elif categoria=='3':
                subtotal_ind3=(pasajeros-(pasajeros-1))*(tarifaDestinoA+tarifaPrimeraclase)
                subtotal_acumulador3+=subtotal_ind3
            subtotal_grupo=subtotal_acumulador1+subtotal_acumulador2+subtotal_acumulador3
        print("Su destino es ciudad A")
        print(f"Pasajeros: {pasajeros}")
        print(f"subtotal a pagar: {subtotal_grupo}")
        total_a_pagar=subtotal_grupo+(subtotal_grupo*0.22)
        print(f"Total a pagar: {total_a_pagar}")
    case 2:
        pasajeros=int(input("Cuantos pasajeros van a viajar: "))
        for i in range(1,pasajeros+1):
            categoria=(input(f"Ingrese la categoria (1 Economica. 2 Ejecutiva. 3 Primera clase.) que desea para el pasajero {i}: "))
            if categoria=='1':
                subtotal_ind1=(pasajeros-(pasajeros-1))*(tarifaDestinoB+tarifaEconomica)
                subtotal_acumulador1+=subtotal_ind1
            elif categoria=='2':
                subtotal_ind2=(pasajeros-(pasajeros-1))*(tarifaDestinoB+tarifaEjecutiva)
                subtotal_acumulador2+=subtotal_ind2
            elif categoria=='3':
                subtotal_ind3=(pasajeros-(pasajeros-1))*(tarifaDestinoB+tarifaPrimeraclase)
                subtotal_acumulador3+=subtotal_ind3
            subtotal_grupo=subtotal_acumulador1+subtotal_acumulador2+subtotal_acumulador3
        print("Su destino es ciudad B")
        print(f"Pasajeros: {pasajeros}")
        print(f"subtotal a pagar: {subtotal_grupo}")
        total_a_pagar=subtotal_grupo+(subtotal_grupo*0.22)
        print(f"Total a pagar: {total_a_pagar}")
    case 3:
        pasajeros=int(input("Cuantos pasajeros van a viajar: "))
        for i in range(1,pasajeros+1):
            categoria=(input(f"Ingrese la categoria (1 Economica. 2 Ejecutiva. 3 Primera clase.) que desea para el pasajero {i}: "))
            if categoria=='1':
                subtotal_ind1=(pasajeros-(pasajeros-1))*(tarifaDestinoC+tarifaEconomica)
                subtotal_acumulador1+=subtotal_ind1
            elif categoria=='2':
                subtotal_ind2=(pasajeros-(pasajeros-1))*(tarifaDestinoC+tarifaEjecutiva)
                subtotal_acumulador2+=subtotal_ind2
            elif categoria=='3':
                subtotal_ind3=(pasajeros-(pasajeros-1))*(tarifaDestinoC+tarifaPrimeraclase)
                subtotal_acumulador3+=subtotal_ind3
            subtotal_grupo=subtotal_acumulador1+subtotal_acumulador2+subtotal_acumulador3
        print("Su destino es ciudad C")
        print(f"Pasajeros: {pasajeros}")
        print(f"subtotal a pagar: {subtotal_grupo}")
        total_a_pagar=subtotal_grupo+(subtotal_grupo*0.22)
        print(f"Total a pagar: {total_a_pagar}")


