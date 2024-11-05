import customtkinter as ctk
import random

# Inicializar customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Distribución de Sitios")
ventana.geometry("850x500")
ventana.configure(bg="#f0f8ff")  # Fondo azul claro

# Diccionario para asociar cada número con un nombre
nombres = {
    1: "Umar",          2: "Salima",    3: "Manar",     4: "Mario",         5: "Marc B.", 
    6: "Judith",        7: "Joel",      8: "Irene",     9: "Noumi",         10: "Albert",       
    11: "Laia",         12: "Michelle", 13: "Adriana",  14: "Claudia",      15: "Yingqing",     
    16: "Abdulrafia",   17: "Aleix",    18: "Emma",     19: "Julen",        20: "Biel",         
    21: "Eric",         22: "Nayara",   23: "Max",      24: "Maria",        25: "Arnau",        
    26: "Marc R.",      27: "Camila",   28: "Ivan",     29: "Arlet",        30: "Nuoxuan"
}


# Generar texto para cada columna
texto_columna_izq = "\n".join([f"{i + 1}. {nombres[i + 1]}" for i in range(15)])
texto_columna_der = "\n".join([f"{i + 16}. {nombres[i + 16]}" for i in range(15)])

# Crear dos CTkLabels para cada columna y alinearlos
cuadro_nombres_izq = ctk.CTkLabel(
    ventana, 
    text=texto_columna_izq,
    font=("Arial", 18),
    width=160,
    height=450,
    #text_color="white",
    anchor="w",
    justify="left"
)
cuadro_nombres_izq.place(x=900, y=10)

cuadro_nombres_der = ctk.CTkLabel(
    ventana, 
    text=texto_columna_der,
    font=("Arial", 18),
    width=160,
    height=450,
    #text_color="white",
    anchor="w",
    justify="left"
)
cuadro_nombres_der.place(x=1020, y=10)

# Posiciones de las mesas para la distribución solicitada
mesas = {
    "fila_1": [(50, 30), (150, 30)],                            # 2 mesas en la fila 1
    "fila_2": [(50, 100), (150, 100), (300, 100), (400, 100), (500, 100), (650, 100), (750, 100)],  # 2, 3, 2 en la fila 2
    "fila_3": [(50, 170), (150, 170), (300, 170), (400, 170), (500, 170), (650, 170), (750, 170)],  # 2, 3, 2 en la fila 3
    "fila_4": [(50, 240), (150, 240), (300, 240), (400, 240), (500, 240), (650, 240), (750, 240)],  # 2, 3, 2 en la fila 4
    "fila_5": [(50, 310), (150, 310), (300, 310), (400, 310), (500, 310), (650, 310), (750, 310)],  # 2, 3, 2 en la fila 5
}

# Diccionario para almacenar números generados y valores fijos en las mesas
numeros_asignados = {}
valores_fijos = {}

# Cuadro de entrada para valores fijos
entrada_valor_fijo = ctk.CTkEntry(ventana, placeholder_text="Ingresa un valor (1-30)")
entrada_valor_fijo.place(x=355, y=400)

# Función para fijar un valor en una mesa
def fijar_valor(posicion):
    try:
        valor = int(entrada_valor_fijo.get())
        if valor < 1 or valor > 30:
            print("El número debe estar entre 1 y 30.")
            return
        if valor in valores_fijos.values():
            print("Este número ya está en uso.")
            return
        valores_fijos[posicion] = valor  # Guardar valor fijo
        mesas_labels[posicion].configure(text=str(valor), fg_color="green")  # Mostrar en la mesa
        entrada_valor_fijo.delete(0, 'end')
    except ValueError:
        entrada_valor_fijo.delete(0, 'end')  # Limpiar si no es un número válido

# Función para crear la interfaz de mesas
mesas_labels = {}
def crear_mesas():
    for fila, posiciones in mesas.items():
        for x, y in posiciones:
            mesa = ctk.CTkLabel(
                ventana,
                text="",
                width=50,
                height=30,
                fg_color="gray",
                text_color="white",
                corner_radius=10,
                font=("Arial", 14)
            )
            mesa.place(x=x, y=y)
            mesas_labels[(x, y)] = mesa
            mesa.bind("<Button-1>", lambda event, pos=(x, y): fijar_valor(pos))

# Función para generar la distribución aleatoria de números en las mesas
def generar_distribucion():
    numeros = [num for num in range(1, 31) if num not in valores_fijos.values()]
    random.shuffle(numeros)
    
    # Asignar números a mesas no fijas
    indice = 0
    for posicion, mesa_label in mesas_labels.items():
        if posicion in valores_fijos:
            # Mostrar valores fijos
            mesa_label.configure(text=str(valores_fijos[posicion]), fg_color="green")
            numeros_asignados[posicion] = valores_fijos[posicion]
        else:
            # Asignar un número aleatorio a mesas no fijas
            mesa_label.configure(text=str(numeros[indice]), fg_color="blue")
            numeros_asignados[posicion] = numeros[indice]
            indice += 1

# Función para mostrar nombres en lugar de números en todas las mesas
def mostrar_nombres():
    for posicion, numero in numeros_asignados.items():
        nombre = nombres.get(numero, "")
        mesas_labels[posicion].configure(text=nombre, fg_color="purple")

# Función para alternar entre modo claro y oscuro
modo_oscuro_activado = False
def alternar_modo_oscuro():
    global modo_oscuro_activado
    if modo_oscuro_activado:
        ctk.set_appearance_mode("light")
        switch_modo_oscuro.configure(text="Modo Oscuro")
        ventana.configure(bg="#f0f8ff")  # Fondo claro
    else:
        ctk.set_appearance_mode("dark")
        switch_modo_oscuro.configure(text="Modo Claro")
        ventana.configure(bg="#333333")  # Fondo oscuro
    modo_oscuro_activado = not modo_oscuro_activado

# Switch para alternar entre modo claro y oscuro
switch_modo_oscuro = ctk.CTkSwitch(
    ventana,
    text="Modo oscuro",
    command=alternar_modo_oscuro,
    font=("Arial", 14),
    corner_radius=8,
    width=120,
    height=40,
    fg_color="#333333",
    
)
switch_modo_oscuro.place(x=675, y=400)

# Botón para generar la distribución
boton_generar = ctk.CTkButton(
    ventana,
    text="GENERAR",
    command=generar_distribucion,
    font=("Arial", 14),
    corner_radius=8,
    width=100,
    height=40,
    fg_color="#4CAF50",
    text_color="white",
    hover_color="#388E3C"
)
boton_generar.place(x=75, y=450)

# Botón para mostrar los nombres en todas las mesas
boton_mostrar_nombres = ctk.CTkButton(
    ventana,
    text="MOSTRAR NOMBRES",
    command=mostrar_nombres,
    font=("Arial", 14),
    corner_radius=8,
    width=150,
    height=40,
    fg_color="#3B83F6",
    text_color="white",
    hover_color="#1C66CC"
)
boton_mostrar_nombres.place(x=346, y=450)

# Función para borrar la distribución y los números fijos
def borrar_distribucion():
    for posicion, mesa_label in mesas_labels.items():
        mesa_label.configure(text="", fg_color="gray")  # Limpiar las mesas
    numeros_asignados.clear()
    valores_fijos.clear()

# Botón para borrar la distribución
boton_borrar = ctk.CTkButton(
    ventana,
    text="BORRAR",
    command=borrar_distribucion,
    font=("Arial", 14),
    corner_radius=8,
    width=100,
    height=40,
    fg_color="#f44336",
    text_color="white",
    hover_color="#c62828"
)
boton_borrar.place(x=675, y=450)

crear_mesas()
ventana.mainloop()