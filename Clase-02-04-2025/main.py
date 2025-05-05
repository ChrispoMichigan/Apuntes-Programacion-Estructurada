from funciones import llena_lista, busca_lista, cuenta_cadena
from os import system
# r = suma(5, 5, 10)
# cadena = "Hola@Mundo! @Python"
# r = contar_mayusculas(cadena)
# print(f'La cadena "{cadena}" tiene {r} mayúsculas.')

# z = contar_caracter(cadena) 
# print(f'La cadena "{cadena}" tiene {z} caracteres "@"')
lista = []
while True:
    system('cls')
    print('Menu')
    print('1. Llenar lista')
    print('2. Buscar valor en lista')
    print('3. Cuenta cadena')
    print('4. Mostrar lista')	
    print('5. Salir')
    opc = int(input('Selecciona una opción: '))

    if opc == 1:
        llena_lista(lista)
    if opc == 2:
        busca_lista(lista)
    if opc == 3:
        cuenta_cadena()
    if opc == 4:
        print('Lista: ')
        print(lista)
        system('pause')
    if opc == 5:
        print('Saliendo...')
        break
