texto = "Hola perdida"
numero = 25
decimal = 25.98
es_verdadero = True
char = "H"

anio = int(input("ingrese el anio: "))
peso = int(input("ingrese el peso: "))
clase = 0
valor = 0.0

if anio <= 1970:
    if peso < 2700:
        clase = 1
        valor = 16.50
    elif peso >= 2700 and peso <= 3800:
        clase = 2
        valor = 25.50
    else:
        clase = 3
        valor = 46.50
elif anio >= 1971 and anio <= 1979:
    if peso < 2700:
        clase = 1
        valor = 27
    elif peso >= 2700 and peso <= 3800:
        clase = 2
        valor = 30.50
    else:
        clase = 3
        valor = 52.50
else:
    if peso < 3500:
        clase = 7
        valor = 19.50
    else:
        clase = 8
        valor = 52.50
print(f"La categoria es: {clase} y debe cancelar ${valor}")
