def var(text):
    print("No [1]")
    print("Si [2]")
    valor = int(input(f"{text}: "))
    return valor == 2

def comprobar():
    var1 = var("Tu personaje puede volar")
    var2 = var("Tu personaje es humano")
    var3 = var("Tu personaje tiene mascara")
    text = f"{int(var1)}{int(var2)}{int(var3)}"
    if text == "111":
        print("Tu personaje es IronMan")
    if text == "110":
        print("Tu personaje es Capitana Marvel")
    if text == "101":
        print("Tu personaje es Capitana Marvel")

comprobar()