"""
Módulo de práctica sobre Diccionarios.
Este script muestra métodos básicos de manipulación y consulta.
"""

# 3. Diccionario de cartera de criptoactivos
cartera = {
    "usuario": "Elvis",
    "activos": ["BTC", "ETH", "ADA"],
    "saldos": {"BTC": 0.5, "ETH": 2.1}
}

# 4. Acceso anidado: Saldo de Ethereum
print(f"Saldo ETH: {cartera['saldos']['ETH']}")

# 5. Agregar nuevo activo
cartera["activos"].append("SOL")

# 6. Modificar un valor
cartera["usuario"] = "Elvis_Pro"

# 7. Listar solo las categorías principales (.keys)
# Usamos el método keys() para obtener las etiquetas [cite: 335]
print(f"Campos disponibles: {cartera.keys()}")

# 8. Uso de .get() para evitar errores
# Recupera información a partir de los nombres de sus claves [cite: 320]
precio = cartera.get("precio_usd", "Dato no disponible")
print(f"Consulta de precio: {precio}")
print(cartera)

dic = {"clave1":["a","b","c"],
       "clave2":["d","e","f"]}
print(dic["clave2"][1].upper())

"""
GUÍA DEFINITIVA DE DICCIONARIOS EN PYTHON
Este script consolida la creación, manipulación, análisis y casos reales
de uso de diccionarios (pares clave:valor).
"""

# --- 1. CREACIÓN Y REGLAS DE LAS CLAVES ---
# Los diccionarios son mutables y ordenados (desde Python 3.7+) [cite: 318, 324, 338]
producto = {
    "nombre": "Laptop HP",
    "precio": 850,
    "stock": 23,
    "disponible": True
}

# Creación mediante la función dict()
persona = dict(nombre="Ana", edad=30, ciudad="Madrid")

# Regla de claves: Deben ser inmutables (Strings, Números o Tuplas)
diccionario_mixto = {
    1: "Entero como clave",
    3.14: "Float como clave",
    ("x", "y"): "Tupla como clave"
}


# --- 2. ACCESO SEGURO A VALORES ---
print("--- 2. ACCESO A DATOS ---")
# Forma 1: Corchetes (Lanza KeyError si la clave no existe) [cite: 331]
print(f"Producto: {producto['nombre']}")

# Forma 2: Método .get() (Seguro, evita errores)
# Si no existe, devuelve el segundo argumento opcional [cite: 330]
marca = producto.get("marca", "Sin marca definida")
print(f"Marca: {marca}")
print()


# --- 3. AGREGAR, MODIFICAR Y ELIMINAR ---
print("--- 3. MANIPULACIÓN ---")
# Agregar o Modificar: Se usa la misma sintaxis [cite: 329, 330]
producto["marca"] = "HP"      # Agrega clave nueva
producto["precio"] = 799     # Modifica valor existente

# Eliminar clave y valor
del producto["disponible"]    # Elimina permanentemente
precio_quitado = producto.pop("precio") # Elimina y devuelve el valor

# Actualización masiva (.update)
producto.update({"stock": 10, "color": "Gris"})
print(f"Producto actualizado: {producto}")
print()


# --- 4. MÉTODOS DE ANÁLISIS ---
# Permiten listar claves, valores o ambos [cite: 334]
print("--- 4. MÉTODOS .keys(), .values(), .items() ---")
print(f"Claves: {list(producto.keys())}")   # [cite: 335]
print(f"Valores: {list(producto.values())}") # [cite: 336]
print(f"Pares completos: {list(producto.items())}") # [cite: 337]
print()


# --- 5. RECORRER (ITERAR) DICCIONARIOS ---
print("--- 5. ITERACIONES ---")
# La forma más usada: desempaquetar clave y valor
for clave, valor in producto.items():
    print(f"- {clave}: {valor}")
print()


# --- 6. DICCIONARIOS ANIDADOS (ESTRUCTURA API/JSON) ---
print("--- 6. DATOS ANIDADOS ---")
pedido = {
    "id": 1234,
    "cliente": {
        "nombre": "María García",
        "email": "maria@mail.com"
    },
    "productos": [
        {"nombre": "Laptop", "precio": 850},
        {"nombre": "Mouse", "precio": 25}
    ]
}

# Acceso en profundidad [cite: 332]
nombre_cliente = pedido["cliente"]["nombre"]
primer_producto = pedido["productos"][0]["nombre"]
print(f"Cliente: {nombre_cliente} | Compró: {primer_producto}")
print()


# --- 7. CASOS DE USO REALES ---
print("--- 7. CASOS REALES ---")

# A. Contar frecuencias (Muy común en análisis de datos)
ventas = ["laptop", "mouse", "laptop", "teclado", "laptop", "mouse"]
contador = {}
for item in ventas:
    # Si la clave no existe, empieza en 0 y suma 1
    contador[item] = contador.get(item, 0) + 1
print(f"Frecuencia de ventas: {contador}")

# B. Agrupar datos por categoría
empleados = [
    {"nombre": "Ana", "depto": "Ventas"},
    {"nombre": "Luis", "depto": "IT"},
    {"nombre": "María", "depto": "Ventas"}
]

por_depto = {}
for emp in empleados:
    depto = emp["depto"]
    if depto not in por_depto:
        por_depto[depto] = []
    por_depto[depto].append(emp["nombre"])

print(f"Personal por departamento: {por_depto}")