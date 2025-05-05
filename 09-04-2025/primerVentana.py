import tkinter as tk
from tkinter import messagebox

#	Crear ventana
ventana = tk.Tk()

# Función para salir de la ventana
def salirVentana():
	messagebox.showwarning("Salir", "¿Está seguro de que desea salir?")
	ventana.destroy()

#	Poner titulo a ventana
ventana.title("Ventana de login")

#	Tamaño y color del fondo de la ventana
ventana.geometry("400x420")
#ventana.configure(width=400, height=420, bg="#3B1E54")
ventana.configure(bg="#176B87")

#	Quitar la capacidad de ampliar la ventana	
ventana.resizable(width=True, height=True)

#	Añadir icono a la ventana
ventana.iconbitmap("img/gato.ico")

#	Añadir botón de salir
btnExit = tk.Button(ventana, text="Salir", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=salirVentana)

#	Acomodar el botón con posición relativa
btnExit.place(relx=0.70, rely=0.70)

#	Añadir un label
lblText = tk.Label(ventana, text="Bienvenido", bg="#176B87", fg="#EEF5FF", font=("Arial", 14))

#	Acomodar el label con posición relativa
lblText.place(relx=0.38, rely=0.10)

#	Añadir un entry
txtUser = tk.Entry(ventana, width=20, justify="center",  show="*", bg="#11235A", fg="#EEF5FF", font=("Arial", 10))

#	Acomodar el entry con posición relativa
txtUser.place(relx=0.32, rely=0.18)

#	Loop de la ventana
ventana.mainloop()