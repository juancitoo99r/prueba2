"""
Se desea saber si el número igresado por el usuario es mayor a 100, si el número solicitado es mayor debere mostrar el
numere - 100 y si es menor a 100 solo debe mostrar el numero. No se podra utilizar numeros menores a 0, en caso contrario
debe notificar el error existente
Programa en phyton
"""
        print("Resultado:", numero)
 numero= int(input("escriba el numero: "))
resta= numero-100

if numero>=100:
    print("El valor es: " ,resta)
elif numero<=100 and numero>0:
    print("El valor es: " ,numero)
else:
    print("El numero es negativo")       