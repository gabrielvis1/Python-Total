# Creación de una tupla con diferentes tipos de datos
mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6)) #

# 1. Definimos datos que no deberían cambiar (ej. coordenadas de un local)
ubicacion = (-34.6037, -58.3816)

# 2. Intentar cambiarlo daría error
# ubicacion[0] = -35.0  <-- Esto rompería el programa

# 3. Unpacking para usar los datos fácilmente
latitud, longitud = ubicacion
print(f"Latitud: {latitud}, Longitud: {longitud}")

# 4. Conversión si realmente es necesario editar
lista_temp = list(ubicacion)
lista_temp[0] = -34.6100
ubicacion_final = tuple(lista_temp)

# 5 extraer los elementos de tupla en variables
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla