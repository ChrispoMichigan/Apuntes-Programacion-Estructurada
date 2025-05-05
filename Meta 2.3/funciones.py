def suma(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return None

def resta(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return None

def multiplicacion(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return None

def formatear_resultado(resultado):
    if resultado is None:
        return "Error"
    
    if resultado == int(resultado):
        return str(int(resultado))
    else:
        return str(resultado)