import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


window = tk.Tk()
window.title("Ventana")

# Tamaño y color del fondo de la ventana
window.geometry("600x400")
window.configure(bg="#A1EEBD")

# Quitar la capacidad de ampliar la ventana    
window.resizable(width=False, height=False)

# Añadir un label1
lblTextNum1 = ttk.Label(window, text="Inserte valor 1 ->", style="LB1.TLabel")
lblTextNum1.place(relx=0.05, rely=0.05)

# Añadir un label1
lblTextNum2 = ttk.Label(window, text="Inserte valor 2 ->", style="LB1.TLabel")
lblTextNum2.place(relx=0.05, rely=0.15)


txtNum1 = ttk.Entry(window, style="C.TEntry")
txtNum1.place(relx=0.25, rely=0.05, width=140)

txtNum2 = ttk.Entry(window, style="C.TEntry")
txtNum2.place(relx=0.25, rely=0.15, width=140)

# Añadir un label1
lblTextNum2 = ttk.Label(window, text="Calculadora", style="LB1.TLabel")
lblTextNum2.place(relx=0.55, rely=0.10)


# Loop de la ventana
window.mainloop()

