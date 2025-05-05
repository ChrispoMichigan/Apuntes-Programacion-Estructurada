import subprocess

def abrir_proceso(ruta):
    subprocess.Popen(ruta)

while True:
    print("Seleccione una opción")
    print("[1] Abrir bloc de notas")
    print("[2] Abrir Calculadora")
    print("[3] Salir")
    opc = int(input())
    if opc == 1:
        abrir_proceso('notepad.exe')
    if opc == 2:
        abrir_proceso('calc.exe')
    if opc == 3:
        print("Saliendo")
        break



