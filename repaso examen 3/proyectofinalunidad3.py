peliculas = [
    {"id":1,"nombre":"Spiderman 2 Funcion Vermount","fecha" :"08/02/2025","hora":"10:00am","asientos":10, "descuento":0.10},
    {"id":2,"nombre":"Spiderman 2","fecha" :"08/02/2025","hora":"18:30pm","asientos":4,"descuento":0.00},
    {"id":3,"nombre":"Batman","fecha" :"08/02/2025","hora":"14:15pm","asientos":30,"descuento":0.00 },
]

edades = [
    {"id":1,"nombre":"Adulto", "descuento":0.00},
    {"id":2,"nombre":"Niño(menor de 12 anios)","descuento":0.50},
    {"id":3,"nombre":"Tercera Edad(mayor de 65 anios)","descuento":0.50},
]

categorias = [
    {"id":1,"nombre":"Normal","valor":10.0},
    {"id":2,"nombre":"VIP","valor":14.0},
]

snacks = [
    {"id":1,"nombre":"No","valor":0.0},
    {"id":2,"nombre":"Nachos con queso","valor":6.0},
    {"id":3,"nombre":"Canguil","valor":5.0},
    {"id":4,"nombre":"Gaseosa","valor":2.0},
    {"id":5,"nombre":"Dulces","valor":3.0},
]

entradas = []

def obtenerPeliculaPorId(idPelicula):
    for pelicula in peliculas:
        if(pelicula["id"]==idPelicula):
            return pelicula

def obtenerEdadPorId(idEdad):
    for edad in edades:
        if(edad["id"]==idEdad):
            return edad
        
def obtenerCategoriaPorId(idCategoria):
    for categoria in categorias:
        if(categoria["id"]==idCategoria):
            return categoria
            
def obtenerSnackPorId(idSnack):
    for snack in snacks:
        if(snack["id"]==idSnack):
            return snack

def disponibilidadAsientos(idPelicula):
    for pelicula in peliculas:
        if(pelicula["id"]==idPelicula):
           return pelicula["asientos"]
    return 0

def actualizarAsientos(idPelicula,asientos):
    for pelicula in peliculas:
        if(pelicula["id"]==idPelicula):
            pelicula["asientos"] = pelicula["asientos"] - asientos
    
def calcularSubtotalDetalle(idCategoria,idSnack):
    categoria = obtenerCategoriaPorId(idCategoria)
    snack = obtenerSnackPorId(idSnack)
    return categoria["valor"] + snack["valor"]

def calcularDescuentoDetalle(idEdad, idPelicula):
    try:
        edad = obtenerEdadPorId(idEdad)
        peliculas = obtenerPeliculaPorId(idPelicula)
        return edad["descuento"] + peliculas["descuento"]   
    except Exception as e:
        print(e)

while True:
    try:
        print("------------------------------")
        print("Bienvenido a SUPERCINES")
        print("------------------------------")
        print("Funciones:")
        for pelicula in peliculas:
            print(f"{pelicula['id']}.- {pelicula['nombre']} - {pelicula['fecha']} - {pelicula['hora']} - Asientos disponibles: {pelicula['asientos']} - Descuento: {pelicula['descuento']*100}%")
        idPelicula = int(input("Seleccione la pelicula: "))
        if(idPelicula>0 and idPelicula<4):
            numero_asientos = int(input("Ingrese la cantidad de boletos: "))
            asientosDisponibles = disponibilidadAsientos(idPelicula)
            if(numero_asientos < asientosDisponibles):
                asientos=[]
                for i in range(numero_asientos):
                    print(f"Datos Asiento {i+1}")
                    for edad in edades:
                        print(f"{edad['id']}.- {edad['nombre']}")
                    idEdad = int(input("Seleccione la edad: "))
                    if(idEdad>0 and idEdad<4):
                        for categoria in categorias:
                           print(f"{categoria['id']}.- {categoria['nombre']} - ${categoria['valor']}") 
                        idCategoria = int(input("Seleccione la categoria: "))
                        if(idCategoria>0 and idCategoria<3):
                            for snack in snacks:
                                print(f"{snack['id']}.- {snack['nombre']} - ${snack['valor']}")
                            idSnack = int(input("Seleccione el snack: "))
                            if(idSnack>0 and idSnack<6):
                               
                                subtotal= calcularSubtotalDetalle(idCategoria, idSnack)
                                descuento=  calcularDescuentoDetalle(idEdad, idPelicula)
                                asiento ={
                                    "edad" : obtenerEdadPorId(idEdad)["nombre"],
                                    "categoria" : f"{obtenerCategoriaPorId(idCategoria)['nombre']} - ${obtenerCategoriaPorId(idCategoria)['valor']}" ,
                                    "snacks": f"{obtenerSnackPorId(idSnack)['nombre']} - ${obtenerSnackPorId(idSnack)['valor']}",
                                    "subtotal"  : subtotal,
                                    "descuento" : subtotal*descuento,
                                    "total"     : subtotal - (subtotal*descuento) 
                                }
                                asientos.append(asiento)

                            else:
                                print("Seleccione una snack existente")
                    else:
                        print("Seleccione una edad existente")
                
                actualizarAsientos(idPelicula, numero_asientos)
                subtotal = 0
                for asiento in asientos:
                    subtotal = subtotal + asiento["total"]    
                iva = subtotal * 0.14
                total = subtotal + iva
                entrada = {
                   "pelicula" : obtenerPeliculaPorId(idPelicula)["nombre"], 
                   "fecha"    : obtenerPeliculaPorId(idPelicula)["fecha"], 
                   "hora"     : obtenerPeliculaPorId(idPelicula)["hora"], 
                   "asientos" : asientos,
                   "subtotal" : subtotal,
                   "iva"      : iva,
                   "total"    : total
                }
                
                #Impresion
                print("--------------------------------")
                print(f"Pelicula: {entrada['pelicula']}")
                print(f"Fecha: {entrada['fecha']}")
                print(f"Hora: {entrada['hora']}")
                contador = 1
                for asiento in entrada['asientos']:
                    print(f"\tAsiento {contador}:")
                    print(f"\t\tEdad:{asiento['edad']}")
                    print(f"\t\tCategoria:{asiento['categoria']}")
                    print(f"\t\tSnacks:{asiento['snacks']}")
                    print(f"\t\tSubtotal:${asiento['subtotal']}")
                    print(f"\t\tDescuento:${asiento['descuento']}")
                    print(f"\t\tTotal:${asiento['total']}")
                    contador +=1
                print(f"Subtotal: ${round(entrada['subtotal'],2)}")
                print(f"IVA: ${round(entrada['iva'],2)}")
                print(f"TOTAL A PAGAR: ${round(entrada['total'],2)}")
                print("--------------------------------")
                entradas.append([entrada])
            else:
                print("No hay asientos disponibles")
        else:
            print("Seleccione una película existente")
    except ValueError : 
        print("Ingrese un valor numerico")
    except Exception as e:
            print(f"Error: {e}")
