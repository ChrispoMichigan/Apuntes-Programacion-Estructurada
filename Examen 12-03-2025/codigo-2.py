import os
n = int(input("Ingrese el número de estudiantes: "))
promedios = []
aprobados = 0
reprobados = 0
alto_rendimiento = 0
i = 1
print("Calculadora de promedio use el rango del 1 al 100")
while i <= n:
    while True:
        print(f"Ingrese las calificaciones del estudiante {i}: ")
        mates = int(input("Ingrese la calificación de matematicas: "))
        ciencia = int(input("Ingrese la calificación de ciencias: "))
        programacion = int(input("Ingrese la calificación de programación: "))
        if mates <= 100 and mates >= 0 and ciencia <= 100 and ciencia >= 0 and programacion <= 100 and programacion >= 0:
            break
        else:
            os.system("cls")
            print("Ingrese un valor válido")

    promedio = (mates * 0.4 + ciencia * 0.35 + programacion * 0.25)
    promedios.append(promedio)
    if promedio >= 90:
        print("Alto rendimiento")
        alto_rendimiento += 1

    if promedio >= 60:
        print("Aprobado")
        aprobados += 1
    else:
        print("Reprobado")
        reprobados += 1
    i += 1
    os.system("cls")

print("Resultados: ")
print(f"Promedios de estudiantes: {promedios}")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
print(f"Promedio general: {sum(promedios)/n}")

if alto_rendimiento == 0:
    print("Estudiantes sin alto rendimiento")
else:
    print(f"Estudiantes con alto rendimiento: {alto_rendimiento}")