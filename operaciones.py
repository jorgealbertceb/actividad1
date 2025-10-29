# Programa que pida al usuario cuantos numeros quiere introducir
# Y que diga qué operación quiere hacer (suma, resta, multiplicación o división)
# Con un if que valide la operación que tiene que hacer
# Con un bucle for que pida los números que haya solicitado
# Que imprima el resultado de la operación

print("Bienvenido al programa de operaciones.")

operacion = str(input("Introduzca la operación que desea realizar (suma, suma facil): "))

if operacion == "suma":
    
    numeros_introducir = int(input("¿Cuántos números desea introducir?: "))

    lista = []
    suma = 0

    for i in range(numeros_introducir):
        numero = int(input("Introduzca un número: "))
        lista.append(numero)

    for x in lista:
        suma = suma + x

    print("La suma es de", suma)

elif operacion == "suma facil":

    numeros_introducir = int(input("¿Cuántos números desea introducir?: "))
    suma = 0

    for i in range(numeros_introducir):
        numero = int(input("Introduzc un número: "))
        suma = suma + numero

    print("La suma es de", suma)