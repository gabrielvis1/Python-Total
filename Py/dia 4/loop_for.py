# 1. Creamos la lista con 20 nombres
nombres = [
    "Juan", "María", "Carlos", "Lucía", "Pedro", 
    "Sofía", "Diego", "Elena", "Marcos", "Valeria", 
    "Lucas", "Martina", "Mateo", "Julia", "Bruno", 
    "Sara", "Leo", "Clara", "Hugo", "Valentina"
]

# 2. El loop for recorre cada elemento de la lista
for n in nombres:
    # Usamos un f-string para insertar el nombre en el mensaje
    if n.startswith("J"):
        numero_nombre = nombres.index(n) + 1  # Obtenemos el número del nombre (1-based)
        print(f"{numero_nombre}. Mucho gusto, {n}")


# 1. Creamos la lista de 20 números del 1 al 20
# Usamos range(1, 21) porque el límite superior no se incluye
numeros = list(range(1, 21))

# 2. Creamos la variable valor inicializada en 0
valor = 0

# 3. Loop for para recorrer cada número de la lista
for numero in numeros:
    # Asignamos a valor la suma de su contenido actual más el número de turno
    valor = valor + numero
    print(f"Valor actual: {valor}")  # Imprimimos el valor en cada iteración para ver el progreso

# 4. Imprimimos el resultado final fuera del bucle
print(valor)

# Lista que contiene 5 listas con 2 números cada una
lista_numeros = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]

print("Iterando la lista de números:")
for x,z in lista_numeros:
    # 'sublista' representa cada par de números en cada vuelta
    print(x)
    print(z)

# 1. Creamos el diccionario (ejemplo: cartera de dividendos)
cartera = {
    "Coca-Cola": "KO",
    "PepsiCo": "PEP",
    "McDonald's": "MCD",
    "Apple": "AAPL"
}

# 2. Recorremos ambos valores con un loop for
# 'empresa' recibirá la clave y 'ticker' recibirá el valor
for empresa, ticker in cartera.items():
    print(f"Empresa: {empresa} | Ticker en Bolsa: {ticker}")
