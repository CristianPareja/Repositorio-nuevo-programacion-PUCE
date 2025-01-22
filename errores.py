try:
    numeroA=int(input("Ingrese numero a: "))
    numeroB=int(input("Ingrese numero b: "))
    resultado=numeroA/numeroB
except ValueError:
    print(" no se puede convertir el numero")
except ZeroDivisionError:
    print("No se puede dividir para cero")
except Exception as e: ##generico
    print(f"Error no controlado {e}")
else:
    print(resultado)
finally:
    print("Programa terminado")
