"""BUSCADOR DE NUMEROS EN SERIES"""
import re           # Importamos el módulo de expresiones regulares para buscar los patrones
import os           # Importamos el módulo os para navegar por los directorios y archivos
import time         # Importamos time para poder medir cuánto tarda la ejecución del programa
import datetime     # Importamos datetime para obtener la fecha exacta de hoy
import math         # Importamos math para redondear el tiempo de búsqueda hacia arriba

# Iniciamos el cronómetro guardando el tiempo actual en la variable 'inicio'
inicio = time.time()

# Definimos la ruta de la carpeta principal donde vamos a buscar (usamos 'r' para que sea una cadena cruda)
ruta = r"C:\Users\gabri\OneDrive\Escritorio\Drive\Python total\Py\dia 9\Mi_Gran_Directorio"

# Definimos el patrón: 'N', luego 3 letras ([a-zA-Z]{3}), un guion (-), y 5 números (\d{5})
mi_patron = r'N[a-zA-Z]{3}-\d{5}'

# Creamos listas vacías para guardar los nombres de los archivos y los números encontrados
archivos_encontrados = []
numeros_encontrados = []

# Usamos os.walk para recorrer la ruta; esto nos devuelve la carpeta actual, subcarpetas y los archivos
for carpeta, _, archivos in os.walk(ruta):
    # Iteramos sobre cada archivo que se encuentre dentro de la lista de archivos
    for arch in archivos:
        # Unimos la ruta de la carpeta con el nombre del archivo para obtener su ruta completa
        ruta_completa = os.path.join(carpeta, arch)
        
        # Usamos try-except por seguridad, por si hay algún archivo que no sea de texto y no se pueda leer
        try:
            # Abrimos el archivo en modo lectura ('r')
            with open(ruta_completa, 'r') as mi_archivo:
                # Leemos todo el contenido del archivo y lo guardamos en la variable 'texto'
                texto = mi_archivo.read()
                
                # Buscamos si el patrón regex existe dentro del texto leído usando re.search()
                resultado = re.search(mi_patron, texto)
                
                # Si la búsqueda encontró un resultado (es decir, no es None)...
                if resultado:
                    # Agregamos el nombre del archivo a nuestra lista de archivos encontrados
                    archivos_encontrados.append(arch)
                    # Agregamos la coincidencia exacta (.group()) a nuestra lista de números encontrados
                    numeros_encontrados.append(resultado.group())
        # Si ocurre un error al intentar leer un archivo específico, simplemente lo ignoramos y pasamos al siguiente
        except:
            pass

# Detenemos el cronómetro guardando el tiempo actual en 'fin'
fin = time.time()

# Calculamos la duración restando el inicio al fin, y usamos math.ceil para redondear siempre hacia arriba
duracion = math.ceil(fin - inicio)

# Obtenemos la fecha de hoy usando la función date.today()
fecha_hoy = datetime.date.today()

# Formateamos la fecha al estilo "día/mes/año" (dd/mm/aa) usando strftime
fecha_formateada = fecha_hoy.strftime("%d/%m/%y")

# Imprimimos la línea de guiones superior (50 caracteres repetidos)
print("-" * 50)
# Imprimimos la fecha de búsqueda inyectando nuestra variable formateada
print(f"Fecha de búsqueda: {fecha_formateada}\n")

# Imprimimos las cabeceras de la tabla usando '\t' (tabulación) para alinear las columnas
print("ARCHIVO\t\tNRO. SERIE")
# Imprimimos las líneas divisorias debajo de las cabeceras, también separadas por tabulación
print("-------\t\t----------")

# Usamos un bucle for junto con zip() para iterar nuestras dos listas al mismo tiempo
for a, n in zip(archivos_encontrados, numeros_encontrados):
    # Imprimimos el nombre del archivo, una tabulación (\t), y luego el número de serie encontrado
    print(f"{a}\t{n}")

# Imprimimos un salto de línea (\n) y la cantidad de elementos en nuestra lista de números (len)
print(f"\nNúmeros encontrados: {len(numeros_encontrados)}")
# Imprimimos la duración de la búsqueda que calculamos antes
print(f"Duración de la búsqueda: {duracion} segundos")
# Imprimimos la línea de guiones final para cerrar nuestra "pantalla"
print("-" * 50)