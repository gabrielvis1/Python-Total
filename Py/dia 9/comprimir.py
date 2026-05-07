""" compresion de archivos"""
import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
# Le agregamos la ruta de las carpetas por delante
mi_zip.write("Py/dia 9/r_e.py")
mi_zip.write("Py/dia 9/aaa.jpeg") # Asumiendo que la imagen también está ahí
mi_zip.close()
