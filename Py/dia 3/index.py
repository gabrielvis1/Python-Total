"""
GUÍA MAESTRA: INDEXACIÓN Y SLICING EN PYTHON
Este script contiene ejemplos de acceso directo, recortes y búsqueda avanzada.
"""

# --- CONSTANTES ---
CANAL = "Dividendo Mental"
PRECIOS = [150.50, 200.00, 50.25, 800.00]

# --- 1. ACCESO DIRECTO (INDEXING) ---
# Se accede a un solo carácter o elemento por su posición numérica.
print("--- 1. ACCESO DIRECTO ---")
print(f"Primera letra: {CANAL[0]}")      # D (índice 0)
print(f"Última letra: {CANAL[-1]}")      # l (índice -1)
print(f"Precio antiguo: {PRECIOS[0]}")   # 150.5
print()

# --- 2. RECORTES (SLICING) ---
# Sintaxis: [inicio : fin : paso] -> El 'fin' es excluyente.
print("--- 2. SLICING (CORTES) ---")
print(f"Primera palabra: {CANAL[0:9]}")  # Dividendo
print(f"Segunda palabra: {CANAL[10:]}")  # Mental (hasta el final)
print(f"Precios medios: {PRECIOS[1:3]}") # [200.0, 50.25]
print()

# --- 3. BÚSQUEDA DESDE LA IZQUIERDA (.index) ---
# Parámetros: (valor, start, stop)
# Busca la primera aparición de izquierda a derecha.
print("--- 3. MÉTODO .index() ---")
# Buscamos la 'i' en "Dividendo Mental"
# La 'i' de la posición 1 es ignorada porque empezamos en el índice 2
idx_izq = CANAL.index("i", 2, 5) 
print(f"Index (rango 2-5): La 'i' está en la posición {idx_izq}") # Resultado: 3
print()

# --- 4. BÚSQUEDA DESDE LA DERECHA (.rindex) ---
# Parámetros: (valor, start, stop)
# Busca la primera aparición de derecha a izquierda (pero mantiene el índice original).
print("--- 4. MÉTODO .rindex() ---")
# Busca la última 'i' en todo el texto
idx_der = CANAL.rindex("i") 
print(f"Rindex (total): La última 'i' está en la posición {idx_der}") # Resultado: 3

# Busca la última 'i' pero limitada al trozo inicial [0:2]
idx_der_rango = CANAL.rindex("i", 0, 2)
print(f"Rindex (rango 0-2): La última 'i' es la de la posición {idx_der_rango}") # Resultado: 1
print()

# --- 5. NOTAS DE SEGURIDAD ---
# 1. Si el índice no existe (ej: PRECIOS[10]), lanza IndexError.
# 2. Si el valor no se encuentra, .index() y .rindex() lanzan ValueError.