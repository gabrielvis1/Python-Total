# Importamos la librería 'requests' para hacer peticiones HTTP (descargar la página)
import requests
# Importamos 'BeautifulSoup' desde el paquete 'bs4' para analizar el HTML
from bs4 import BeautifulSoup

# 1. Definimos la URL de la página web que queremos analizar
url = "https://books.toscrape.com/"

# 2. Hacemos la petición a la página web y guardamos la respuesta
# 'requests.get' actúa como tu navegador web, solicitando el contenido del sitio
respuesta = requests.get(url)

# 3. Extraemos el texto HTML puro de la respuesta que nos dio el servidor
html_contenido = respuesta.text

# 4. Creamos el "objeto BeautifulSoup" (la sopa) pasando el HTML y el analizador 'lxml'
# Esto transforma el texto plano en una estructura de árbol por la que podemos navegar
soup = BeautifulSoup(html_contenido, 'lxml')


# --- EJEMPLOS DE BÚSQUEDAS ---

print("=== EXTRACCIÓN DE DATOS DE LA PÁGINA ===")

# Ejemplo A: Buscar el primer elemento de un tipo (El título principal de la página)
# '.find()' busca la primera etiqueta <h1> que encuentre en todo el documento
titulo_pagina = soup.find('h1')
# '.text' extrae solo el texto limpio que está dentro de la etiqueta, omitiendo los símbolos < >
# '.strip()' elimina los espacios en blanco innecesarios o saltos de línea al inicio y al final
print(f"Título de la web: {titulo_pagina.text.strip()}\n")


# Ejemplo B: Buscar MULTIPLES elementos (Todos los libros de la página)
# '.find_all()' busca TODOS los elementos que cumplan con la condición y los devuelve en una lista
# En esta web, cada libro está dentro de una etiqueta <article> que tiene la clase 'product_pod'
articulos_libros = soup.find_all('article', class_='product_pod')

# Usamos un bucle 'for' para recorrer cada uno de los libros encontrados en la lista
for libro in articulos_libros:
    
    # Ejemplo C: Buscar sub-elementos dentro de un elemento ya encontrado
    # Dentro de este libro, buscamos la etiqueta <h3>, luego la etiqueta <a>, y extraemos el atributo 'title'
    # Usamos ['title'] porque a veces el texto visible está cortado con "...", pero el atributo 'title' tiene el nombre completo
    titulo_libro = libro.h3.a['title']
    
    # Ejemplo D: Buscar por nombres de clases CSS (El precio del libro)
    # Buscamos la primera etiqueta <p> dentro del libro que tenga la clase 'price_color'
    precio_libro = libro.find('p', class_='price_color').text
    
    # Ejemplo E: Buscar atributos específicos (La calificación en estrellas)
    # Buscamos la etiqueta <p> que contiene las clases de calificación.
    # En esta web usan clases como "star-rating Three". Buscamos la que empiece con "star-rating"
    # El método '.attrs' nos da un diccionario de los atributos, y seleccionamos ['class']
    # 'class' devuelve una lista, por ejemplo: ['star-rating', 'Three']. Tomamos el segundo elemento [1]
    clases_calificacion = libro.find('p', class_='star-rating').attrs['class']
    estrellas = clases_calificacion[1] # Esto nos devolverá palabras como 'One', 'Two', 'Three', etc.
    
    # 5. Mostramos los resultados en la consola de forma ordenada
    print(f"Libro: {titulo_libro}")
    print(f"Precio: {precio_libro}")
    print(f"Calificación: {estrellas} estrellas")
    print("-" * 40) # Una línea divisoria para que sea fácil de leer en la terminal