""" crear y manipular directorios en python """
#import os 
# crear el directorio actual de trabajo
#ruta_proyecto = os.getcwd()

#print(ruta_proyecto+"\\Py\\dia 6")

#os.chdir("C:\\Users\\gabri\\OneDrive\\Escritorio\\Drive")
#archi = open("xxx.txt","r",encoding="utf-8")
#print(archi.read())
#archi.close()

# crear un nuevo direcctorio
#os.mkdir("C:\\Users\\gabri\\OneDrive\\Escritorio\\Drive\\Python total\\Py\\dia 6\\otra")
# eliminar un directorio
#os.rmdir("C:\\Users\\gabri\\OneDrive\\Escritorio\\5")
# eliminar un archivo
#ruta="C:\\Users\\gabri\\OneDrive\\Escritorio\\Drive\\Python total\\Py\\dia 6\\xxx.txt"
#archivo = os.path.basename(ruta)
#print(archivo)

#directorio = os.path.dirname(ruta)
#print(directorio)

#mi_ruta = os.path.split(ruta)
#print(mi_ruta)

from pathlib import Path

carpeta = Path("C:/Users/gabri/OneDrive/Escritorio/Drive/Python total/Py/dia 6/otra carpeta")
mi_archivo = carpeta / "archivo.txt"
archivo = open(mi_archivo,"w",encoding="utf-8")
archivo.write("hola mundo") 
archivo.close()
archivo = open(mi_archivo,"r",encoding="utf-8")
print(mi_archivo)
print(archivo.read())