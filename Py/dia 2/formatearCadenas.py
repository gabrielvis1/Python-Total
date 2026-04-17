# Variables de prueba
color_auto = "rojo"
matricula = "ABC-123"
precio = 25000.789

# --- MÉTODO FORMAT ---
print("--- Método .format() ---")
print("Auto: {} | Matrícula: {}".format(color_auto, matricula))

# --- MÉTODO F-STRING ---
print("\n--- Método f-string ---")
print(f"Auto: {color_auto} | Matrícula: {matricula}")

# --- FORMATEO NUMÉRICO ---
print("\n--- Precisión y Miles ---")
print(f"Precio con 2 decimales: ${precio:.2f}") # $25000.79
print(f"Precio con separador: ${precio:,.2f}") # $25,000.79

# --- ALINEACIÓN ---
print("\n--- Tabla Alineada ---")
print(f"{'PRODUCTO':<12} | {'PRECIO':>10}")
print("-" * 25)
print(f"{'Manzana':<12} | {'$1.50':>10}")
print(f"{'Computadora':<12} | {'$950.00':>10}")

nombre = "Elvis"
vistas = 5000
# No necesitas convertir a str(), la f-string lo hace sola
print(f"Hola {nombre}, tu video tiene {vistas} reproducciones.")
# --- 1. F-STRINGS BÁSICAS ---
canal = "Dividendo Mental"
print(f"Bienvenidos a {canal}")


# --- 2. FORMATEO NUMÉRICO (El más útil) ---
valor_accion = 150.78923
ganancia = 2500000

# :.2f -> Dos decimales y redondeo
print(f"Precio de acción: ${valor_accion:.2f}") # $150.79

# :, -> Separador de miles
print(f"Ganancia total: ${ganancia:,}") # $2,500,000

# Combinado: Miles y decimales
print(f"Balance final: ${ganancia + valor_accion:,.2f}")


# --- 3. OPERACIONES DENTRO DE LLAVES ---
# Podés hacer cálculos directamente
print(f"El doble de la acción es: {valor_accion * 2}")


# --- 4. ALINEACIÓN (Para tablas) ---
print("\n--- TABLA DE DATOS ---")
print(f"{'Activo':<10} | {'Precio':>10}")
print("-" * 25)
print(f"{'BTC':<10} | {'65000.50':>10}")
print(f"{'ETH':<10} | {'3500.20':>10}")