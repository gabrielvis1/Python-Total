# ==========================================================
# GUÍA MAESTRA DE TIPOS Y ESTRUCTURAS DE DATOS EN PYTHON
# ==========================================================

# --- 1. TIPOS DE DATOS SIMPLES ---

# Texto (str): Almacena información alfanumérica [cite: 5]
nombre_curso = "Python" # [cite: 6]
precio_texto = "750"    # Los números entre comillas son texto [cite: 6]

# Números (int y float) [cite: 7]
entero = 250            # int: números sin decimales [cite: 8]
decimal = 12.50         # float: números con decimales [cite: 8]

# Booleanos (bool): Representan valores lógicos [cite: 9]
es_verdadero = True     # [cite: 10]
es_falso = False        # [cite: 10]


# --- 2. ESTRUCTURAS DE DATOS (Colecciones) ---

# Listas []: Son mutables, ordenadas y permiten duplicados [cite: 11, 12]
mi_lista = ["Python", 250, 12.50, "Python"] 

# Tuplas (): Son ordenadas y permiten duplicados, pero NO son mutables [cite: 11, 13, 14]
mi_tuple = ("Python", 250, 12.50)

# Sets {}: Son mutables, pero NO son ordenados y NO permiten duplicados [cite: 11, 13, 14]
mi_set = {"Python", 250, 12.50}

# Diccionarios {}: Son mutables y las llaves (keys) deben ser únicas [cite: 15, 18]
# Nota: En Python 3.7+ mantienen el orden de inserción 
mi_diccionario = {
    "nombre": "Python",
    "precio": 750,
    "version": 3.12
}


# --- 3. DEMOSTRACIÓN EN PANTALLA ---

print("--- TIPOS SIMPLES ---")
print("String:", nombre_curso, "| Tipo:", type(nombre_curso))
print("Entero:", entero, "| Tipo:", type(entero))
print("Flotante:", decimal, "| Tipo:", type(decimal))
print("Booleano:", es_verdadero, "| Tipo:", type(es_verdadero))

print("\n--- ESTRUCTURAS DE DATOS ---")
print("Lista (Mutable/Ordenada):", mi_lista)
print("Tupla (Inmutable/Ordenada):", mi_tuple)
print("Set (Sin orden/Sin duplicados):", mi_set)
print("Diccionario (Llave única):", mi_diccionario)

# ==========================================================
# EL GRAN DICCIONARIO DE TIPOS DE DATOS EN PYTHON
# ==========================================================

# --- 1. TIPOS SIMPLES (Un solo valor) ---

# String (str): Se reconoce por las comillas
texto = "Python" #
simbolos = "%$&" #
numero_como_texto = "123" #

# Integer (int): Números enteros sin punto ni comillas
entero_positiivo = 150 #
entero_negativo = -15 #

# Float (float): Siempre tienen un punto decimal
decimal = 3.14159 #
entero_flotante = 25.0 #

# Boolean (bool): Solo True o False (Mayúscula inicial)
es_programador = True #
le_gusta_el_error = False #


# --- 2. COLECCIONES (Contenedores de múltiples valores) ---

# Lista (list): Ordenada y modificable. Usa corchetes [ ]
mi_lista = ["sal", 1, -3, 4.5] #

# Tupla (tuple): Ordenada e inmutable (no cambia). Usa paréntesis ( )
mi_tupla = ("lun", "mar", "mie", "jue", "vie") #

# Diccionario (dict): Pares clave:valor. Usa llaves { } con dos puntos :
mi_diccionario = {"color": "rojo", "arte": "cine"} #

# Set (set): Sin duplicados y sin orden. Usa llaves { } sin dos puntos
mi_set = {"a", "b", "c", "d", "e"} #


# --- 3. VERIFICACIÓN DE TIPOS (La prueba de verdad) ---

print("--- RECONOCIMIENTO DE TIPOS ---")
print(f"'{texto}' es de tipo:", type(texto)) #
print(f"{entero_positiivo} es de tipo:", type(entero_positiivo)) #
print(f"{decimal} es de tipo:", type(decimal)) #
print(f"{es_programador} es de tipo:", type(es_programador)) #
print(f"{mi_lista} es de tipo:", type(mi_lista)) #
print(f"{mi_tupla} es de tipo:", type(mi_tupla)) #
print(f"{mi_diccionario} es de tipo:", type(mi_diccionario)) #
print(f"{mi_set} es de tipo:", type(mi_set)) #