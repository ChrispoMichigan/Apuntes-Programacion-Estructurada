import tkinter as tk
from tkinter import messagebox
import funciones

num_actual = ""
primer_num = None
operacion = None
resultado = None

def presionar_numero(numero):
    """Maneja el evento"""
    global num_actual
    
    if num_actual == "0" and numero != ".":
        num_actual = numero
    else:
        if numero == "." and "." in num_actual:
            return
        num_actual += numero
    
    actualizar_display()

def presionar_operacion(op):
    """Maneja el evento botón de operación"""
    global num_actual, primer_num, operacion
    
    if primer_num is not None and num_actual:
        calcular_resultado()
    
    if num_actual:
        primer_num = float(num_actual)
        operacion = op
        num_actual = ""
        
        display.config(state="normal")
        display.delete(0, tk.END)
        texto = str(primer_num) if primer_num == int(primer_num) else str(primer_num)
        display.insert(0, f"{texto} {op}")
        display.config(state="readonly")

def calcular_resultado():
    """Calcula el resultado de la operación"""
    global num_actual, primer_num, operacion, resultado
    
    if primer_num is not None and num_actual and operacion:
        num1 = primer_num
        num2 = float(num_actual)
        
        if operacion == "+":
            resultado = funciones.suma(num1, num2)
        elif operacion == "-":
            resultado = funciones.resta(num1, num2)
        elif operacion == "×":
            resultado = funciones.multiplicacion(num1, num2)
        
        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, funciones.formatear_resultado(resultado))
        display.config(state="readonly")
        
        primer_num = resultado
        num_actual = ""
        operacion = None

def limpiar():
    """Reinicia la calculadora"""
    global num_actual, primer_num, operacion, resultado
    
    num_actual = ""
    primer_num = None
    operacion = None
    resultado = None
    
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, "0")
    display.config(state="readonly")

def actualizar_display():
    """Actualiza la pantalla de la calculadora"""
    display.config(state="normal")
    display.delete(0, tk.END)
    
    if not num_actual:
        display.insert(0, "0")
    else:
        display.insert(0, num_actual)
    
    display.config(state="readonly")

def configurar_boton_redondo(event, boton):
    width = event.width
    height = event.height
    radius = min(width, height) // 2
    boton.config(highlightthickness=0, bd=0)
    
    canvas = tk.Canvas(boton.master, width=width, height=height, bg="#A1EEBD", 
                      highlightthickness=0)
    canvas.place(x=boton.winfo_x(), y=boton.winfo_y())
    
    canvas.create_oval(2, 2, width-2, height-2, fill=boton["bg"], outline="")
    canvas.create_text(width/2, height/2, text=boton["text"], font=boton["font"])
    
    boton.lift()

def crear_botones():
    """Crea los botones de la calculadora"""
    color_numero = "#FFFFFF"
    color_operacion = "#FFD580"
    color_igual = "#90EE90"
    color_limpiar = "#FF9999"
    
    botones_info = [
        {"texto": "7", "fila": 0, "columna": 0, "color": color_numero},
        {"texto": "8", "fila": 0, "columna": 1, "color": color_numero},
        {"texto": "9", "fila": 0, "columna": 2, "color": color_numero},
        {"texto": "×", "fila": 0, "columna": 3, "color": color_operacion},
        
        {"texto": "4", "fila": 1, "columna": 0, "color": color_numero},
        {"texto": "5", "fila": 1, "columna": 1, "color": color_numero},
        {"texto": "6", "fila": 1, "columna": 2, "color": color_numero},
        {"texto": "-", "fila": 1, "columna": 3, "color": color_operacion},
        
        {"texto": "1", "fila": 2, "columna": 0, "color": color_numero},
        {"texto": "2", "fila": 2, "columna": 1, "color": color_numero},
        {"texto": "3", "fila": 2, "columna": 2, "color": color_numero},
        {"texto": "+", "fila": 2, "columna": 3, "color": color_operacion},
        
        {"texto": "C", "fila": 3, "columna": 0, "color": color_limpiar},
        {"texto": "0", "fila": 3, "columna": 1, "color": color_numero},
        {"texto": ".", "fila": 3, "columna": 2, "color": color_numero},
        {"texto": "=", "fila": 3, "columna": 3, "color": color_igual},
    ]
    
    for boton_info in botones_info:
        boton = tk.Button(
            botones_frame,
            text=boton_info["texto"],
            bg=boton_info["color"],
            font=("Arial", 16, "bold"),
            borderwidth=0,
            relief="flat"
        )

        boton.configure(width=3, height=1)
        
        if boton_info["texto"] in "0123456789.":
            boton.config(command=lambda b=boton_info["texto"]: presionar_numero(b))
        elif boton_info["texto"] in "+-×":
            boton.config(command=lambda b=boton_info["texto"]: presionar_operacion(b))
        elif boton_info["texto"] == "=":
            boton.config(command=calcular_resultado)
        elif boton_info["texto"] == "C":
            boton.config(command=limpiar)
        
        boton.grid(
            row=boton_info["fila"],
            column=boton_info["columna"],
            padx=5,
            pady=5,
            sticky="nsew"
        )
        
        boton.bind("<Configure>", lambda event, b=boton: configurar_boton_redondo(event, b))

def iniciar_calculadora():
    """Configuración inicial de la calculadora"""
    global root, display, botones_frame
    
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("300x400")
    root.configure(bg="#A1EEBD")
    root.resizable(width=False, height=False)
    
    display_frame = tk.Frame(root, bg="#F0F0F0", bd=5)
    display_frame.place(x=20, y=20, width=260, height=60)
    
    display = tk.Entry(display_frame, font=("Arial", 18), justify="right", bd=0)
    display.pack(fill=tk.BOTH, expand=True)
    display.insert(0, "0")
    display.config(state="readonly")
    
    botones_frame = tk.Frame(root, bg="#A1EEBD")
    botones_frame.place(x=20, y=100, width=260, height=280)
    
    for i in range(4):
        botones_frame.grid_rowconfigure(i, weight=1)
        botones_frame.grid_columnconfigure(i, weight=1)
    
    crear_botones()


iniciar_calculadora()
root.mainloop()