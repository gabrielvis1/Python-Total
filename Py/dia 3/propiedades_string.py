# --- 1. CONCATENACIÓN Y MULTIPLICACIÓN ---
saludo = "Hola" + " " + "Mundo" # Concatenación
print(saludo)

enfasis = "¡Gool! " * 3 # Multiplicación
print(enfasis)

# --- 2. MULTILÍNEA ---
poema = """Esto es un string
que ocupa varias líneas
en el código."""
print(poema)

# --- 3. LONGITUD Y VERIFICACIÓN ---
nombre_canal = "Dividendo Mental"
print(f"Longitud: {len(nombre_canal)}") # 16 caracteres

# Verificamos si existe una palabra
existe = "Mental" in nombre_canal
no_existe = "Inversión" not in nombre_canal

print(f"¿Está 'Mental'?: {existe}")    # True
print(f"¿No está 'Inversión'?: {no_existe}") # True

# --- 4. PRUEBA DE INMUTABILIDAD ---
texto = "Python"
# texto[0] = "p"  <- Esto daría error porque son inmutables
texto = texto.lower() # Esto sí funciona porque estamos REASIGNANDO la variable