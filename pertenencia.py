texto="hola el dia de hoy es sabado"
busqueda=input("Que letra quiero buscar: ").lower()
if busqueda in texto.lower():
    print(f"{busqueda} esta en el texto.")
else:
    print(f"{busqueda} cambio de prueba.")