var1 = True
var2 = False

"""
GUÍA DE BOOLEANOS Y LÓGICA
Este script muestra cómo realizar comparaciones y validaciones lógicas.
"""

# --- 1. DECLARACIÓN EXPLÍCITA ---
es_valido = True
mercado_abierto = False

# --- 2. OPERACIONES DE COMPARACIÓN ---
precio_bitcoin = 65000
mi_presupuesto = 50000

puedo_comprar = mi_presupuesto >= precio_bitcoin
print(f"¿Puedo comprar Bitcoin?: {puedo_comprar}") # False

# --- 3. OPERADORES LÓGICOS (Filtros complejos) ---
tiene_dinero = True
es_mayor_edad = True
cuenta_verificada = False

# AND: Se deben cumplir TODAS las condiciones
puede_invertir = tiene_dinero and es_mayor_edad and cuenta_verificada
print(f"¿Cumple todos los requisitos?: {puede_invertir}") # False

# OR: Basta con que una sea verdadera
tiene_permiso = cuenta_verificada or es_mayor_edad
print(f"¿Tiene algún tipo de permiso?: {tiene_permiso}") # True

# NOT: Invertir el sentido
print(f"Estado inverso de mercado: {not mercado_abierto}") # True

# --- 4. VERIFICACIÓN DE CONTENIDO (Devuelve booleano) ---
canal = "Dividendo Mental"
print(f"¿Está la palabra 'Mental'?: {'Mental' in canal}") # True