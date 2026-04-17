"""Guía definitiva de Slicing: Todos los casos posibles."""

TEXTO = "ABCDEFGHIJ" # 10 caracteres (del 0 al 9)

print(f"Texto original: {TEXTO}\n")

# --- CATEGORÍA 1: CORTES SIMPLES ---
print("--- CORTES SIMPLES ---")
print(f"Del 2 al 5: {TEXTO[2:5]}")    # CDE
print(f"Primeros 3: {TEXTO[:3]}")     # ABC
print(f"Desde el 7: {TEXTO[7:]}")     # HIJ

# --- CATEGORÍA 2: EL PODER DEL NEGATIVO ---
print("\n--- NEGATIVOS ---")
print(f"Últimos 4:  {TEXTO[-4:]}")    # GHIJ
print(f"Todo menos los últimos 2: {TEXTO[:-2]}") # ABCDEFGH

# --- CATEGORÍA 3: SALTOS (STEP) ---
print("\n--- SALTOS Y TRUCOS ---")
print(f"De 2 en 2: {TEXTO[::2]}")     # ACEGI
print(f"Del 1 al 8, de 2 en 2: {TEXTO[1:8:2]}") # BDFH
print(f"TEXTO INVERTIDO: {TEXTO[::-1]}") # JIHGFEDCBA

# --- CATEGORÍA 4: CASOS "LOCOS" ---
print("\n--- CASOS BORDE ---")
print(f"Fuera de rango [0:100]: {TEXTO[0:100]}") # No da error, trae todo
print(f"Corte vacío [5:2]: {TEXTO[5:2]}") # Devuelve un string vacío