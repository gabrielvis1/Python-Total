import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def extraer_precio(texto_precio):
    """Extrae el valor numérico del precio eliminando símbolos de moneda."""
    match = re.search(r'(\d+\.\d+)', texto_precio)
    return float(match.group(1)) if match else 0.0

def extraer_stock(texto_stock):
    """Extrae únicamente la cantidad numérica del texto de disponibilidad."""
    match = re.search(r'\d+', texto_stock)
    return int(match.group()) if match else 0

def iniciar_scraping():
    url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
    libros_encontrados = []
    
    # El sitio web de pruebas tiene exactamente 50 páginas
    for pagina in range(1, 51):
        print(f"Analizando página {pagina}...")
        url_actual = url_base.format(pagina)
        respuesta = requests.get(url_actual)
        
        # Si la página no existe o hay un error, salimos del bucle
        if respuesta.status_code != 200:
            break
            
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Cada libro está dentro de un <article> con la clase 'product_pod'
        articulos_libros = soup.find_all('article', class_='product_pod')
        
        for libro in articulos_libros:
            # 1. Condición: Únicamente libros con 5 estrellas
            if not libro.find('p', class_='star-rating Five'):
                continue
                
            # Extraer el precio para evaluarlo
            texto_precio = libro.find('p', class_='price_color').text
            precio = extraer_precio(texto_precio)
            
            # 2. Condición: Superar el costo de 50
            if precio > 50.0:
                # Extraemos el título y el enlace hacia el detalle del libro
                titulo = libro.find('h3').find('a')['title']
                enlace_relativo = libro.find('h3').find('a')['href']
                
                # Construimos la URL absoluta uniendo la URL de la página actual con el enlace relativo
                url_detalle = urllib.parse.urljoin(url_actual, enlace_relativo)
                
                # Hacemos una nueva petición a la página de detalle del libro
                respuesta_detalle = requests.get(url_detalle)
                soup_detalle = BeautifulSoup(respuesta_detalle.text, 'html.parser')
                
                # 3. Extraer el UPC de la tabla de información del producto
                th_upc = soup_detalle.find('th', string='UPC')
                upc = th_upc.find_next_sibling('td').text if th_upc else "N/A"
                
                # 4. Extraer el Stock y procesarlo con la expresión regular
                texto_disponibilidad = soup_detalle.find('p', class_='instock availability').text
                stock = extraer_stock(texto_disponibilidad)
                
                # 5. Extraer la Categoría desde el menú de navegación (breadcrumb)
                # La estructura es: Home > Books > [Categoría] > Título
                breadcrumb = soup_detalle.find('ul', class_='breadcrumb')
                elementos_lista = breadcrumb.find_all('li')
                categoria = elementos_lista[2].text.strip() if len(elementos_lista) >= 3 else "N/A"
                
                # Consolidamos la información
                datos_libro = {
                    'Página de origen': pagina,
                    'Título': titulo,
                    'Precio': precio,
                    'UPC': upc,
                    'Stock': stock,
                    'Categoría': categoria
                }
                
                libros_encontrados.append(datos_libro)
                print(f" -> ¡Match! {titulo} | Precio: £{precio} | UPC: {upc} | Categoría: {categoria} | Stock: {stock}")

    return libros_encontrados

if __name__ == '__main__':
    print("Iniciando recolección de datos...")
    resultados = iniciar_scraping()
    print(f"\nProceso finalizado. Se encontraron {len(resultados)} libros que cumplen con las condiciones.")
    
    # Ejemplo de cómo ver el primer resultado si existe
    if resultados:
        print("\nEjemplo del primer registro guardado:")
        print(resultados[0])