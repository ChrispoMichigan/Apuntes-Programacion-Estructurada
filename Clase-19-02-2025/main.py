from math import pi

radio = float(input("Insere a medida del radio: "))
print(f"El area del circulo es: {(pi * radio ** 2):.2f}")

radio_esfera = float(input("Insere a medida del radio de la esfera: "))
print(f"El volumen de la esfera es: {(4/3 * pi * radio_esfera ** 3):.2f}")

base = float(input("Insere a medida de la base del triangulo: "))
altura = float(input("Insere a medida de la altura del triangulo: "))
print(f"El area del triangulo es: {(base * altura / 2):.2f}")
