"""
Se desea saber si el número igresado por el usuario es mayor a 100, si el número solicitado es mayor debere mostrar el
numere - 100 y si es menor a 100 solo debe mostrar el numero. No se podra utilizar numeros menores a 0, en caso contrario
debe notificar el error existente
Programa en phyton
"""
numero = int(input("Ingrese un número: "))

if numero < 0:
    print("Error: El número ingresado es menor que 0.")
else:
    if numero > 100:
        print("Resultado:", numero - 100)
    else:
        print("Resultado:", numero)