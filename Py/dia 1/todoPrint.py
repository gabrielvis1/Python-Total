# ==========================================
# GUÍA MAESTRA DEL PRINT() - REFERENCIA RÁPIDA
# ==========================================

# 1. LO BÁSICO (Texto y Números)
print("--- 1. LO BÁSICO ---")
print("Hola Mundo")             # Texto con comillas
print(42)                       # Números sin comillas
print(10 + 5)                   # Operaciones matemáticas
print()                         # Imprime una línea vacía


# 2. COMILLAS SIMPLES Y DOBLES
print("--- 2. COMILLAS ---")
print("Texto con 'comillas simples' adentro")
print('Texto con "comillas dobles" adentro')


# 3. IMPRIMIR VARIAS COSAS Y SEPARADORES (sep)
print("--- 3. VARIAS COSAS Y SEP ---")
print("Hola", "Mundo", "Python")            # Espacio por defecto
print("A", "B", "C", sep="-")               # Separador personalizado: A-B-C
print(2026, 4, 7, sep="/")                  # Formato fecha: 2026/4/7


# 4. CONTROLAR EL FINAL (end)
print("--- 4. CONTROL DEL FINAL ---")
print("Cargando", end="...") 
print("Listo!")                             # Resultado: Cargando...Listo!


# 5. CARACTERES ESPECIALES (Escapes)
print("--- 5. CARACTERES ESPECIALES ---")
print("Línea 1\nLínea 2")                   # \n = Salto de línea
print("Nombre:\tElvis")                     # \t = Tabulación
print("Ruta: C:\\Usuarios\\Documentos")    # \\ = Barra invertida
print("Ella dijo: \"¡Hola!\"")               # \" = Mostrar comillas


# 6. TEXTO EN VARIAS LÍNEAS (Comillas Triples)
print("--- 6. MULTILÍNEA Y ARTE ---")
print("""
Este es un texto
que ocupa varias líneas
sin usar el símbolo barra n.
""")

print("""
╔═══════════════════════╗
║    DIBUJO ASCII       ║
║   (Usa triples "")    ║
╚═══════════════════════╝
""")

print("--- FIN DE LA GUÍA ---")