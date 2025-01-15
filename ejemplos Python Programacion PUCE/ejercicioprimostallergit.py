# Solicitar números al usuario
inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

print(f"Los números primos entre {inicio} y {fin} son:")

for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2,num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
