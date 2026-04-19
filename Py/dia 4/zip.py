"""Union de dos listas con zip()"""

nombres = ["Juan", "María", "Carlos", "Lucía", "Pedro", "Elvis", "Sofía", "Diego", "Elena", "Marcos"]
edades = [25, 30, 22, 28, 35, 55, 27, 31, 29, 26]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Bilbao", "Granada", "Málaga", "Murcia", "Valladolid"]

combinados = zip(nombres, edades, ciudades)  # Combina las tres listas en tuplas correspondientes
#print(list(combinados))  # Convertimos el resultado a una lista para mostrarlo

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")