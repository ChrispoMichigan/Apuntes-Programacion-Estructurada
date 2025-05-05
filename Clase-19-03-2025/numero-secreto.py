import random

numeroSecreto = random.randrange(15, 30)
intentos = 20
i = 0

while i < intentos:
    valor = int(input("Seleccione un número "))
    if valor == numeroSecreto:
        print("Adivinaste el número")
        break
    if valor < numeroSecreto:
        print("El valor secreto es mayor")
    if valor > numeroSecreto:
        print("El valor secreto es menor")
    i += 1
    if i > intentos:
        print("Maximos intentos alcanzados")

