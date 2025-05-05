import os

lista = []

while True:
    os.system('cls')
    print('Opciones:')
    print('1. Agregar una nueva calificación')
    print('2. Mostrar lista de calificaciones')
    print('3. Mostrar la calificación más alta')
    print('4. Mostrar la calificación más baja')
    print('5. Mostrar el promedio de las calificaciones')
    print('6. Cantidad de aprobados y reprobados')
    print('7. Salir')
    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        calificacion = float(input('Ingrese una calificación: '))
        if calificacion < 0 or calificacion > 100:
            print('La calificación debe estar entre 0 y 100.')
            os.system('pause')
            continue
        lista.append(calificacion)
        print('Calificación agregada con éxito.')
        os.system('pause')
    if opcion == '2':
        print('Lista de calificaciones:', lista)
        os.system('pause')
    if opcion == '3':
        if lista:
            print('La calificación más alta es:', max(lista))
            os.system('pause')
        else:
            print('No hay calificaciones registradas.')
            os.system('pause')
    if opcion == '4':
        if lista:
            print('La calificación más baja es:', min(lista))
            os.system('pause')
        else:
            print('No hay calificaciones registradas.')
            os.system('pause')
    if opcion == '5':
        if lista:
            promedio = sum(lista) / len(lista)
            print('El promedio de las calificaciones es:', promedio)
            os.system('pause')
        else:
            print('No hay calificaciones registradas.')
            os.system('pause')
    if opcion == '6':
        if lista:
            aprobados = sum(1 for calificacion in lista if calificacion >= 60)
            reprobados = len(lista) - aprobados
            print('Cantidad de aprobados:', aprobados)
            print('Cantidad de reprobados:', reprobados)
            os.system('pause')
        else:
            print('No hay calificaciones registradas.')
            os.system('pause')
    
    if opcion == '7':
        print('Saliendo del programa...')
        break
    
    if opcion not in ['1', '2', '3', '4', '5', '6']:
        print('Opción inválida. Por favor, ingrese una opción válida.')
        os.system('pause')

