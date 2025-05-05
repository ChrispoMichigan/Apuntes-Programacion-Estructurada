from os import system
import random
# def suma(v1, v2, v3):
#     z = int(input("Introduce el cuarto valor: "))
#     suma = v1 + v2 + v3 + z
#     return suma

# def contar_mayusculas(cadena):
#     e = suma(1 for c in cadena if c.isupper())
#     return e

# def contar_caracter(cadena):
#     caracter = input('Introduce el caracter a contar: ')
#     return cadena.count(caracter)

def llena_lista(lista):
    cantidad = int(input('Introduce la cantidad de valores a agregar: '))
    ran_min = int(input('Introduce el valor mínimo del rango: '))
    ran_max = int(input('Introduce el valor máximo del rango: '))
    for i in range(cantidad):
        valor = random.randint(ran_min, ran_max)
        lista.append(valor)

    print(f'Lista llena: {lista}')
    system('pause')

def busca_lista(lista):
    valor = int(input('Introduce el valor a buscar: '))
    for i, value in enumerate(lista):
        if value == valor:
            print(f'El valor {value} se encuentra en la posición {i}')
    system('pause')

def buscar_mayusculas(cadena):
    letras = []
    for i in cadena:
        if i.isupper():
            letras.append(i)
    return letras

def buscar_minusculas(cadena):
    letras = []
    for i in cadena:
        if i.islower():
            letras.append(i)
    return letras

def buscar_numeros(cadena):
    numeros = []
    for i in cadena:
        if i.isdigit():
            numeros.append(i)
    return numeros

def buscar_numero_tres(cadena):
    numeros = []
    for i in cadena:
        if i.isdigit() and int(i) == 3:
            numeros.append(i)
    return numeros

def reemplazar_caracter(cadena):
    caracter = '3'
    cadena = cadena.replace(caracter, 'E')
    return cadena

def cuenta_cadena():
    cadena = 'P3P3Peca5p1C4PaPa5'
    print(f'La cadena "{cadena}" tiene {len(buscar_mayusculas(cadena))}, son {buscar_mayusculas(cadena)}.')
    print(f'La cadena "{cadena}" tiene {len(buscar_minusculas(cadena))}, son {buscar_minusculas(cadena)}.')
    print(f'La cadena "{cadena}" tiene {len(buscar_numeros(cadena))}, son {buscar_numeros(cadena)}.')
    print(f'La cadena "{cadena}" tiene {len(buscar_numero_tres(cadena))} numeros 3.')
    system('pause')