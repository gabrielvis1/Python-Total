"""Archivo de entrada y salida"""
mi_archivo = open("Py/dia 6/prueba1.txt", encoding="utf-8")
print(mi_archivo)
print(type(mi_archivo))
print(mi_archivo.read())
print(mi_archivo.readline())

for l in mi_archivo:
    print(l)

todas = mi_archivo.readlines()
print(todas)













mi_archivo.close()
