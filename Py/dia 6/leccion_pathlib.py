"""Lección 6: pathlib"""
from pathlib import Path

# Crear un objeto Path
carpeta = Path("C:/Users/gabri/OneDrive/Escritorio/Drive/Python total/Py/dia 6/otra carpeta/archivo.txt")

print(carpeta.read_text()) # Leer el contenido del archivo
print(carpeta.name) # Obtener el nombre del archivo
print(carpeta.suffix) # Obtener la extensión del archivo
print(carpeta.stem) # Obtener el nombre del archivo sin la extensión
print(carpeta.parent) # Obtener la carpeta padre del archivo
print(carpeta.exists()) # Verificar si el archivo existe
print(carpeta.is_file()) # Verificar si es un archivo
print(carpeta.is_dir()) # Verificar si es una carpeta
print(carpeta.stat()) # Obtener información del archivo (tamaño, fecha de creación, etc.)

base = Path.home() # Obtener la ruta del directorio home del usuario
print(base) # Imprimir la ruta del directorio home
guia = Path(base,
            "Barcelona", 
            "Sagrada Familia",
            Path("guia.txt")) # Crear una ruta utilizando el directorio home y subcarpetas
guia2 = guia.with_name("La Pedrera.txt") # Cambiar el nombre del archivo en la ruta
print(guia) # Imprimir la ruta completa
print(guia2) # Imprimir la ruta completa con el nuevo nombre del archivo
print(guia.parent.parent) # Imprimir la carpeta padre de la ruta

guia3 = Path(Path.home()/"Europa")
for txt in Path(guia3).glob("*.txt"): # Buscar todos los archivos .txt en la carpeta "Europa"
    print(txt) # Imprimir la ruta de cada archivo encontrado
for txt in Path(guia3).glob("**/*.txt"): # Buscar todos los archivos .txt en la carpeta "Europa" y sus subcarpetas
    print(txt) # Imprimir la ruta de cada archivo encontrado
    
guia4 = Path("Europa","Espana","Barcelona","Sagrada familia.txt")
en_europa = guia4.relative_to(Path("Europa")) # Obtener la ruta relativa a la carpeta "Europa"
print(en_europa) # Imprimir la ruta relativa
en_espana = guia4.relative_to(Path("Europa","Espana")) # Obtener la ruta relativa a la carpeta "Espana"
print(en_espana) # Imprimir la ruta relativa