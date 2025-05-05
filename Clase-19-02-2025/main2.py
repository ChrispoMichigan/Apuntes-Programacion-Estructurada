valor = int(input("Introduce un valor: "))

if valor >= 0:
    print(f"El valor: {valor} es positivo")
    if valor % 2 == 0:
        print(f"El valor: {valor} es par")
    else:
        print(f"El valor: {valor} es impar")
else:
    print(f"El valor: {valor} es negativo")
    if valor % 2 == 0:
        print(f"El valor: {valor} es par")
    else:
        print(f"El valor: {valor} es impar")