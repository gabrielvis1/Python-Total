# ==========================================
# GUÍA MAESTRA DE STRINGS - REFERENCIA RÁPIDA
# ==========================================

# 1. CREACIÓN Y NÚMEROS COMO TEXTO
print("--- 1. CREACIÓN ---")
print("Hola")                # Comillas dobles
print('Python')              # Comillas simples
print("42" + "8")            # Resultado: 428 (Texto, no suma)


# 2. COMILLAS ANIDADAS Y ESCAPE
print("\n--- 2. COMILLAS Y ESCAPE ---")
print("Él dijo 'hola'")      # Simples dentro de dobles
print('Ella dijo "adiós"')   # Dobles dentro de simples
print("Uso de escape: \"Texto entre comillas\"")


# 3. STRINGS MULTILÍNEA (Triple Comilla)
print("\n--- 3. MULTILÍNEA ---")
print("""Este texto
tiene varias
líneas.""")


# 4. CARACTERES ESPECIALES
print("\n--- 4. CARACTERES ESPECIALES ---")
print("Salto de\nlínea")     # \n
print("Texto\tTabulado")     # \t
print("Barra: C:\\Ruta")    # \\


# 5. UNIR (CONCATENAR) Y REPETIR
print("\n--- 5. UNIR Y REPETIR ---")
print("Hola" + " " + "Mundo") # Concatenar con +
print("Ja" * 3)               # Repetir con *
print("-" * 20)               # Útil para separadores visuales


# 6. ÍNDICES (ACCEDER A CARACTERES)
# Texto:   P  y  t  h  o  n
# Índice:  0  1  2  3  4  5
texto = "Python"
print("\n--- 6. ÍNDICES ---")
print("Primer carácter [0]:", texto[0])    # P
print("Último carácter [-1]:", texto[-1])  # n


# 7. SLICING (CORTAR PARTES)
print("\n--- 7. SLICING ---")
# [inicio:fin] -> El fin no se incluye
print("Corte [0:3]:", texto[0:3])  # Pyt
print("Hasta el [ :4]:", texto[:4])   # Pyth
print("Desde el [2: ]:", texto[2:])   # thon
print("Extensión:", "foto.png"[-3:])   # png


# 8. LONGITUD (len)
print("\n--- 8. LONGITUD ---")
frase = "Hola Mundo"
print("Longitud de '" + frase + "':", len(frase)) # Cuenta el espacio!