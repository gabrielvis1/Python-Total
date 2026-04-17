"""
Guía de Referencia de Métodos de String
Basado en la documentación de Métodos de Análisis y Transformación.
"""

# --- 1. MÉTODOS DE ANÁLISIS ---
# Sirven para obtener información de la cadena sin modificarla[cite: 40].
s = "Hola mundo Hola Hola hola"
print(f"Búsqueda de 'Hola': {s.count('Hola')}")      # Cuenta repeticiones [cite: 41]
print(f"Posición de 'mundo': {s.find('mundo')}")    # Retorna índice o -1 [cite: 43, 45]
print(f"Posición de 'mundo': {s.index('mundo')}")   # Retorna índice o error [cite: 43, 47]

# Búsqueda desde el final [cite: 53]
ruta = "C:/python36/python.exe"
print(f"Última barra encontrada en: {ruta.rfind('/')}") # [cite: 57]

# Validaciones booleanas (True/False) [cite: 59, 60]
print(f"¿Empieza con 'Hola'?: {s.startswith('Hola')}") # [cite: 62]
print(f"¿Termina con 'mundo'?: {s.endswith('mundo')}") # [cite: 64]

# Comprobación de tipos de caracteres [cite: 67, 76]
print(f"¿Es decimal (0-9)?: {'1234'.isdecimal()}")   # Más restrictiva [cite: 70, 73]
print(f"¿Es alfanumérico?: {'abc123'.isalnum()}")    # Letras y números [cite: 77]
print(f"¿Es minúscula?: {'abc'.islower()}")          # Solo minúsculas [cite: 83]
print(f"¿Es título?: {'Hola Mundo'.istitle()}")      # Mayúscula inicial cada palabra [cite: 102, 103]
print(f"¿Identificador Python?: {'var_1'.isidentifier()}") # [cite: 96, 97]


# --- 2. MÉTODOS DE TRANSFORMACIÓN ---
# Retornan una nueva cadena con los cambios aplicados[cite: 108, 109].
original = "  hola Mundo  "

print(f"Capitalize: {original.capitalize()}") # Primera letra en mayúscula [cite: 110]
print(f"Upper: {original.upper()}")           # Todo a mayúsculas [cite: 160]
print(f"Lower: {original.lower()}")           # Todo a minúsculas [cite: 160]
print(f"Swapcase: {original.swapcase()}")     # Invierte mayúsculas/minúsculas [cite: 165]
print(f"Strip: '{original.strip()}'")         # Quita espacios laterales [cite: 173, 175]

# Formateo y Alineación [cite: 122]
texto = "Python"
print(f"Centrado: '{texto.center(10, '*')}'") # [cite: 130]
print(f"Relleno ceros: {'42'.zfill(5)}")       # [cite: 220, 222]

# Reemplazos y Limpieza avanzada [cite: 181, 195, 202]
archivo = "datos_abril.csv"
print(f"Sin prefijo: {archivo.removeprefix('datos_')}") # [cite: 184]
print(f"Sin sufijo: {archivo.removesuffix('.csv')}")    # [cite: 197]
print(f"Reemplazar: {s.replace('mundo', 'Python')}")    # [cite: 204]


# --- 3. MÉTODOS DE SEPARACIÓN Y UNIÓN ---
# Ideales para procesar listas de datos[cite: 228].
data = "Bitcoin,Ethereum,Solana"

# Dividir [cite: 229]
lista_criptos = data.split(",") # [cite: 229]
print(f"Lista separada: {lista_criptos}") 

# Unir [cite: 260]
union = " - ".join(lista_criptos) # [cite: 260, 264]
print(f"Unión con guiones: {union}")

# Partición (retorna tupla de 3 elementos) [cite: 251]
print(f"Partición por coma: {data.partition(',')}") # [cite: 254]