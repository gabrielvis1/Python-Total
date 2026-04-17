# --- CONVERSIONES BÁSICAS ---
numero_txt = "100"
numero_int = int(numero_txt)      # De str a int
numero_flt = float(numero_txt)    # De str a float

print("Suma de textos:", "5" + "5")      # Resultado: 55
print("Suma convertida:", int("5") + 5)  # Resultado: 10


# --- EL TRUCO DEL SET (Eliminar duplicados) ---
precios_repetidos = [10, 20, 10, 50, 20]
unicos = list(set(precios_repetidos))
print("Precios únicos:", unicos) # Resultado: [10, 20, 50]


# --- VERIFICACIÓN DE LOGICA ---
print("¿Es verdadero 'Hola'?:", bool("Hola")) # True
print("¿Es verdadero un cero?:", bool(0))      # False


# --- TRUNCAR VS REDONDEAR ---
valor = 9.99
print("Con int() (trunca):", int(valor))     # 9
print("Con round() (redondea):", round(valor)) # 10