import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Toplevel

#   ['Invitado', 'Admin', 'Usuario']
# • Administrador
# • Secretaria
# • Invitado
# • Juegos de matemática
baseUser = {
    'Admin': '1234',
    'Secretaria': '5678',
    'Usuario': '9101',
    'Juegos de matemática': '1234'
}

window = tk.Tk()
window.title("Login")

# Configurar el tema antes de crear estilos
style = ttk.Style()

# Para ttk.Label, la configuración funciona como la tienes
style.configure(
    "LB1.TLabel",
    background="#7AB2D3",
    foreground="#11235A",
    font=("Arial", 14)
)

# 1. Opción 1: Si quieres usar ttk.Entry, pero los estilos son limitados
style.map("C.TEntry",
    fieldbackground=[("focus", "#11235A")],
    foreground=[("focus", "#001F3F")]
)
# Nota: background y foreground pueden no funcionar con ttk.Entry dependiendo del tema

# Función para salir de la ventanaW
def salirVentana():
    messagebox.showwarning("Salir", "¿Está seguro de que desea salir?")
    window.destroy()

def iniciarSesion(event=None):
    user = txtUser.get()
    passw = txtPass.get()
    print(user, passw)  # Para depuración
    if not user or not passw:
        messagebox.showinfo("Campos requeridos", "Por favor, complete todos los campos")
        return
    if baseUser[user] != passw:
        messagebox.showerror("Error", "Contraseña incorrecta")
        return
    messagebox.showinfo("Login", "Bienvenido(a) " + user)


    # 'Admin': '1234',
    # 'Secretaria': '5678',
    # 'Usuario': '9101',
    # 'Juegos de matemática': '1234'
    if user == 'Admin':
        print("Entrando a admin")
        InitialWindowAdmin(user=user)
    if user == 'Secretaria':  
        InitialWindowSecre(user=user)
    if user == 'Usuario':   
        InitialWindowUser(user=user)
    if user == 'Juegos de matemática': 
        InitialWindow(user=user)  # Llamar a la función para abrir la ventana principal

def InitialWindowAdmin(event=None, user=None):
    window.withdraw()
    mainWindo = Toplevel()
    mainWindo.title(f"sesión de {user}")
    mainWindo.geometry("400x420")
    mainWindo.configure(bg="#7AB2D3")
    # Añadir icono a la ventana
    try:
        mainWindo.iconbitmap("img/cuenta.ico")
    except tk.TclError:
        print("Archivo de icono no encontrado")

    # Añadir un label con una imagen
    try:
        img = tk.PhotoImage(file="img/admin.png")
        img = img.subsample(5) 
        # Cambiar window por mainWindo
        labelImg = tk.Label(mainWindo, image=img, bg="#7AB2D3")
        labelImg.place(relx=0.1, rely=0.05)
        # Guardar referencia a la imagen para evitar que sea eliminada por el recolector de basura
        mainWindo.img = img  # Importante: mantiene la referencia a la imagen
    except tk.TclError:
        print("Archivo de imagen no encontrado")

    # Quitar la capacidad de ampliar la ventana    
    mainWindo.resizable(width=False, height=False)
    
    def cerrarSesion():
        mainWindo.destroy()
        window.deiconify()
    
    # Añadir botón de cerrar sesión
    btnExit = tk.Button(mainWindo, text="Cerrar Sesión", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=cerrarSesion)
    btnExit.place(relx=0.75, rely=0.05)

def InitialWindowSecre(event=None, user=None):
    window.withdraw()
    mainWindo = Toplevel()
    mainWindo.title(f"sesión de {user}")
    mainWindo.geometry("400x420")
    mainWindo.configure(bg="#7AB2D3")
    # Añadir icono a la ventana
    try:
        mainWindo.iconbitmap("img/cuenta.ico")
    except tk.TclError:
        print("Archivo de icono no encontrado")

    # Añadir un label con una imagen
    try:
        img = tk.PhotoImage(file="img/secretaria.png")
        img = img.subsample(5) 
        # Cambiar window por mainWindo
        labelImg = tk.Label(mainWindo, image=img, bg="#7AB2D3")
        labelImg.place(relx=0.1, rely=0.05)
        # Guardar referencia a la imagen para evitar que sea eliminada por el recolector de basura
        mainWindo.img = img  # Importante: mantiene la referencia a la imagen
    except tk.TclError:
        print("Archivo de imagen no encontrado")

    # Quitar la capacidad de ampliar la ventana    
    mainWindo.resizable(width=False, height=False)
    
    def cerrarSesion():
        mainWindo.destroy()
        window.deiconify()
    
    # Añadir botón de cerrar sesión
    btnExit = tk.Button(mainWindo, text="Cerrar Sesión", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=cerrarSesion)
    btnExit.place(relx=0.75, rely=0.05)

def InitialWindowUser(event=None, user=None):
    window.withdraw()
    mainWindo = Toplevel()
    mainWindo.title(f"sesión de {user}")
    mainWindo.geometry("400x420")
    mainWindo.configure(bg="#7AB2D3")
    # Añadir icono a la ventana
    try:
        mainWindo.iconbitmap("img/cuenta.ico")
    except tk.TclError:
        print("Archivo de icono no encontrado")

    # Añadir un label con una imagen
    try:
        img = tk.PhotoImage(file="img/user.png")
        img = img.subsample(5) 
        # Cambiar window por mainWindo
        labelImg = tk.Label(mainWindo, image=img, bg="#7AB2D3")
        labelImg.place(relx=0.1, rely=0.05)
        # Guardar referencia a la imagen para evitar que sea eliminada por el recolector de basura
        mainWindo.img = img  # Importante: mantiene la referencia a la imagen
    except tk.TclError:
        print("Archivo de imagen no encontrado")

    # Quitar la capacidad de ampliar la ventana    
    mainWindo.resizable(width=False, height=False)
    
    def cerrarSesion():
        mainWindo.destroy()
        window.deiconify()
    
    # Añadir botón de cerrar sesión
    btnExit = tk.Button(mainWindo, text="Cerrar Sesión", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=cerrarSesion)
    btnExit.place(relx=0.75, rely=0.05)

def InitialWindow(event=None, user=None):
    window.withdraw()
    mainWindo = Toplevel()
    mainWindo.title(f"sesión de {user}")
    mainWindo.geometry("600x420")
    mainWindo.configure(bg="#7AB2D3")
    # Añadir icono a la ventana
    try:
        mainWindo.iconbitmap("img/cuenta.ico")
    except tk.TclError:
        print("Archivo de icono no encontrado")

    # Quitar la capacidad de ampliar la ventana    
    mainWindo.resizable(width=False, height=False)

    # Añadir un label
    lblTitle = ttk.Label(mainWindo, text="Juego de Habilidades Matemáticas", style="LB1.TLabel", font=("Arial", 20))
    lblTitle.place(relx=0.15, rely=0.1)
    
    # Añadir un label
    lblModal = ttk.Label(mainWindo, text="Seleccione la modalidad", style="LB1.TLabel")
    lblModal.place(relx=0.1, rely=0.2)

    # Lista despleagable para el usuario
    txtUser = ttk.Combobox(mainWindo, values=['Facil', 'Intermedio', 'Avanzado'], justify="center", state="readonly")
    txtUser.place(relx=0.5, rely=0.2, width=140)

    def cerrarSesion():
        mainWindo.destroy()
        window.deiconify()
    
    def iniciarGame():
        import random
        # Definimos variables para el seguimiento del juego
        nonlocal turno, puntuacion, operando1, operando2, operador
        
        # Obtener la dificultad seleccionada
        dificultad = txtUser.get()
        
        if not dificultad:
            messagebox.showinfo("Información", "Seleccione una dificultad")
            return
        
        # Reiniciar variables del juego
        turno = 1
        puntuacion = 0
        
        # Configurar rango según dificultad
        if dificultad == "Facil":
            rango = 10
        elif dificultad == "Intermedio":
            rango = 100
        elif dificultad == "Avanzado":
            rango = 1000
        else:
            # Si no se seleccionó dificultad válida
            rango = 10
        
        # Generar primera operación matemática
        operando1 = random.randint(0, rango)
        operando2 = random.randint(0, rango)
        operador = "+"
        
        # Actualizar etiquetas
        lblNumber1.config(text=str(operando1))
        lblNumber2.config(text=str(operando2))
        lblSigno.config(text=operador)
        
        # Mostrar información del juego
        lblEstado.config(text=f"Turno {turno}/10. Puntuación: {puntuacion}")
        
    def validateAnswer():
        import random
        nonlocal turno, puntuacion, operando1, operando2, operador
        
        # Verificar si el juego está en curso
        if turno == 0 or turno > 10:
            messagebox.showinfo("Información", "Inicie un nuevo juego")
            return
        
        # Obtener respuesta del usuario
        try:
            respuesta_usuario = int(txtPass.get())
        except ValueError:
            messagebox.showerror("Error", "Introduce un número válido")
            return
        
        # Calcular respuesta correcta
        respuesta_correcta = operando1 + operando2
        
        # Verificar respuesta
        if respuesta_usuario == respuesta_correcta:
            messagebox.showinfo("Resultado", "¡Correcto!")
            puntuacion += 1
        else:
            messagebox.showwarning("Resultado", f"Fallido. La respuesta correcta era {respuesta_correcta}")
        
        # Limpiar campo de respuesta
        txtPass.delete(0, tk.END)
        
        # Incrementar turno
        turno += 1
        
        # Si todavía no se han completado 10 turnos, generar nueva operación
        if turno <= 10:
            # Actualizar etiqueta de estado
            lblEstado.config(text=f"Turno {turno}/10. Puntuación: {puntuacion}")
            
            # Obtener rango según dificultad
            dificultad = txtUser.get()
            if dificultad == "Facil":
                rango = 10
            elif dificultad == "Intermedio":
                rango = 100
            else:  # Avanzado
                rango = 1000
            
            # Generar nueva operación
            operando1 = random.randint(0, rango)
            operando2 = random.randint(0, rango)
            
            # Actualizar etiquetas
            lblNumber1.config(text=str(operando1))
            lblNumber2.config(text=str(operando2))
        else:
            # Mostrar resultado final
            messagebox.showinfo("Fin del Juego", f"Juego terminado.\nPuntuación final: {puntuacion}/10")
            
            # Reiniciar para un nuevo juego
            lblNumber1.config(text="0")
            lblNumber2.config(text="0")
            lblEstado.config(text="Seleccione dificultad e inicie un nuevo juego")


    # Variables para el juego (al inicio de InitialWindow())
    turno = 0
    puntuacion = 0
    operando1 = 0
    operando2 = 0
    operador = "+"

    # Añadir etiqueta para el estado del juego (después de los otros controles)
    lblEstado = ttk.Label(mainWindo, text="Seleccione dificultad e inicie un nuevo juego", style="LB1.TLabel")
    lblEstado.place(relx=0.2, rely=0.35)
        # Añadir botón de inicar el juego
    btnInit = tk.Button(mainWindo, text="Iniciar", bg="#11235A", width=20, height=1, fg="#EEF5FF", font=("Arial", 8), command=iniciarGame)
    btnInit.place(relx=0.78, rely=0.2)
    
    # Añadir botón de cerrar sesión
    btnExit = tk.Button(mainWindo, text="Cerrar Sesión", bg="#11235A", width=20, height=1, fg="#EEF5FF", font=("Arial", 8), command=cerrarSesion)
    btnExit.place(relx=0.78, rely=0.02)

    # Añadir un label
    lblNumber1 = ttk.Label(mainWindo, text="0", style="LB1.TLabel")
    lblNumber1.place(relx=0.2, rely=0.5)

    # Añadir un label
    lblSigno = ttk.Label(mainWindo, text="+", style="LB1.TLabel")
    lblSigno.place(relx=0.3, rely=0.5)

    lblNumber2 = ttk.Label(mainWindo, text="0", style="LB1.TLabel")
    lblNumber2.place(relx=0.4, rely=0.5)

    # Añadir un label
    lblIgual = ttk.Label(mainWindo, text="=", style="LB1.TLabel")
    lblIgual.place(relx=0.45, rely=0.5)

    # Añadir la entrada de la contraseña
    txtPass = ttk.Entry(mainWindo, style="C.TEntry")
    txtPass.place(relx=0.5, rely=0.5, width=140)

    # Añadir botón de cerrar sesión
    btnValit = tk.Button(mainWindo, text="Validar", bg="#11235A", width=20, height=1, fg="#EEF5FF", font=("Arial", 8), command=validateAnswer)
    btnValit.place(relx=0.5, rely=0.55)


window.bind("<Return>", iniciarSesion)  # Permitir iniciar sesión con Enter
#   <Return> es el evento de la tecla Enter
#   <Escape> es el evento de la tecla Escape
#   <Button-1> es el evento del botón izquierdo del ratón
#   <KeyPress> es el evento de la tecla presionada

#   <Control-q> es el evento de Ctrl + q
#   <Control-Shift-q> es el evento de Ctrl + Shift + q
#   <Control-Shift-Alt-q> es el evento de Ctrl + Shift + Alt + q

# Tamaño y color del fondo de la ventana
window.geometry("400x420")
window.configure(bg="#7AB2D3")

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

# Añadir un label
lblTextUser = ttk.Label(window, text="User", style="LB1.TLabel")
lblTextUser.place(relx=0.45, rely=0.29)

# Añadir un label
lblTextPass = ttk.Label(window, text="Password", style="LB1.TLabel")
lblTextPass.place(relx=0.40, rely=0.43)

# Lista despleagable para el usuario
txtUser = ttk.Combobox(window, values=[key for key in baseUser], justify="center", state="readonly")
txtUser.place(relx=0.33, rely=0.36, width=140)

# Añadir la entrada de la contraseña
txtPass = ttk.Entry(window, style="C.TEntry", show="*")
txtPass.place(relx=0.33, rely=0.51, width=140)

# Añadir botón de salir
btnExit = tk.Button(window, text="Salir", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=salirVentana)
btnExit.place(relx=0.70, rely=0.70)

# Añadir botón de login
btnLogin = tk.Button(window, text="Login", bg="#11235A", width=10, height=2, fg="#EEF5FF", font=("Arial", 10), command=iniciarSesion)
btnLogin.place(relx=0.10, rely=0.70)

# Añadir un label con una imagen
try:
    img = tk.PhotoImage(file="img/user.png")
    img = img.subsample(5) 
    labelImg = tk.Label(window, image=img, bg="#7AB2D3")
    labelImg.place(relx=0.37, rely=0.05)
except tk.TclError:
    print("Archivo de imagen no encontrado")

# Loop de la ventana
window.mainloop()