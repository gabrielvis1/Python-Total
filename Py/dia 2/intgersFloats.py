# ==========================================================
# GUÍA MAESTRA DE NÚMEROS (INT Y FLOAT) EN PYTHON
# ==========================================================

# 1. IDENTIFICACIÓN DE TIPOS
# Regla: Si tiene punto decimal, es float. Si no, es int. 
print("--- 1. TIPOS ---")
print(type(42))      # <class 'int'>
print(type(100.0))   # <class 'float'> (aunque sea .0) 


# 2. OPERACIONES BÁSICAS
# IMPORTANTE: La división (/) siempre devuelve un float 
print("\n--- 2. OPERACIONES BÁSICAS ---")
print("Suma:", 10 + 5)          # 15
print("División:", 10 / 2)      # 5.0 (¡Siempre float!) 


# 3. OPERACIONES ESPECIALES
print("\n--- 3. OPERACIONES ESPECIALES ---")
print("División entera (//):", 17 // 5) # 3 (descarta decimales) 
print("Módulo (%):", 17 % 5)           # 2 (lo que sobra) 
print("Potencia (**):", 2 ** 3)         # 8 (2 al cubo) 
print("Raíz cuadrada:", 16 ** 0.5)      # 4.0 


# 4. REGLA DE PROMOCIÓN
# Al mezclar int y float, el resultado es float [cite: 4]
print("\n--- 4. PROMOCIÓN ---")
print("5 + 2.0 =", 5 + 2.0)             # 7.0 [cite: 4]


# 5. CONVERSIÓN VS REDONDEO
print("\n--- 5. CONVERSIÓN Y REDONDEO ---")
print("Truncar con int(3.7):", int(3.7))   # 3 (corta decimales) [cite: 5]
print("Redondear round(3.7):", round(3.7)) # 4 (aproxima) [cite: 6]
print("Redondeo decimal:", round(3.14159, 2)) # 3.14 [cite: 6]


# 6. NÚMEROS GRANDES Y PRECISIÓN
print("\n--- 6. FORMATOS AVANZADOS ---")
print("Notación científica (1e6):", 1e6)   # 1,000,000.0 
print("Separador visual:", 8_000_000_000)   # 8 mil millones 

# Precisión de floats: ¡Cuidado en finanzas! 
print("0.1 + 0.2 =", 0.1 + 0.2)             # 0.30000000000000004