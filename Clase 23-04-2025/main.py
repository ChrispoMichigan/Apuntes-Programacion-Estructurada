import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

baseUser = {
    'Juan': '1234',
    'Pedro': '5678',
    'Maria': '91011'
}

window = tk.Tk()
window.title("Login")

# Configurar el tema antes de crear estilos
style = ttk.Style()

# Para ttk.Label, la configuración funciona como la tienes
style.configure(
    "LB1.TLabel",
    background="#A1EEBD",
    foreground="#11235A",
    font=("Arial", 14)
)

# Para ttk.Entry, necesitamos un enfoque diferente
# 1. Opción 1: Si quieres usar ttk.Entry, pero los estilos son limitados
style.map("C.TEntry",
    fieldbackground=[("focus", "#11235A")],
    foreground=[("focus", "#EEF5FF")]
)
# Nota: background y foreground pueden no funcionar con ttk.Entry dependiendo del tema

# Función para salir de la ventanaW
def salirVentana():
    messagebox.showwarning("Salir", "¿Está seguro de que desea salir?")
    window.destroy()
    
def login():
    user = txtUser.get()
    passw = txtPass.get()

    if user in baseUser and baseUser[user] == passw:
        messagebox.showinfo("Login", "Bienvenido " + user)
    else:
        if user not in baseUser:
            messagebox.showerror("Login", "Usuario no encontrado")
        if user in baseUser and baseUser[user] != passw:
            messagebox.showerror("Login", "Contraseña incorrecta")

# Tamaño y color del fondo de la ventana
window.geometry("400x420")
window.configure(bg="#A1EEBD")

# Añadir icono a la ventana
try:
    window.iconbitmap("img/cuenta.ico")
except tk.TclError:
    print("Archivo de icono no encontrado")

# Quitar la capacidad de ampliar la ventana    
window.resizable(width=False, height=False)

# Añadir un label1
lblTextUser = ttk.Label(window, text="User", style="LB1.TLabel")
lblTextUser.place(relx=0.45, rely=0.29)


# Añadir un label1
lblTextUser = ttk.Label(window, text="User", style="LB1.TLabel")
lblTextUser.place(relx=0.45, rely=0.29)

# Añadir un label
lblTextPass = ttk.Label(window, text="Password", style="LB1.TLabel")
lblTextPass.place(relx=0.40, rely=0.43)

# OPCIÓN 1: Seguir usando ttk.Entry con estilos limitados
txtUser = ttk.Entry(window, style="C.TEntry")
txtUser.place(relx=0.33, rely=0.36, width=140)

txtPass = ttk.Entry(window, style="C.TEntry", show="*")
txtPass.place(relx=0.33, rely=0.51, width=140)

# OPCIÓN 2: Cambiar a tk.Entry para tener control total sobre los colores
# (descomenta estas líneas y comenta las de ttk.Entry de arriba si prefieres esta opción)
# txtUser = tk.Entry(window, width=20, justify="center", bg="#11235A", fg="#EEF5FF", font=("Arial", 10))
# txtUser.place(relx=0.33, rely=0.36, width=140)
# 
# txtPass = tk.Entry(window, width=20, justify="center", bg="#11235A", fg="#EEF5FF", font=("Arial", 10), show="*")
# txtPass.place(relx=0.33, rely=0.51, width=140)

# Añadir botón de salir
btnExit = tk.Button(window, text="Salir", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=salirVentana)
btnExit.place(relx=0.70, rely=0.70)

# Añadir botón de login
btnLogin = tk.Button(window, text="Login", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=login)
btnLogin.place(relx=0.10, rely=0.70)

# Añadir un label con una imagen
try:
    img = tk.PhotoImage(file="img/user.png")
    img = img.subsample(5) 
    labelImg = tk.Label(window, image=img, bg="#A1EEBD")
    labelImg.place(relx=0.37, rely=0.05)
except tk.TclError:
    print("Archivo de imagen no encontrado")

# Loop de la ventana
window.mainloop()