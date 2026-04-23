""" vamos a escribir un archivo de texto con python """
#metodo solo lectura
mi_archivo = open("Py/dia 6/prueba1.txt","r",encoding="utf-8")

#mi_archivo.write("hola mundo") #no se puede escribir en un archivo abierto en modo lectura

mi_archivo.close()

#metodo escritura
mi_archivo1 = open("Py/dia 6/prueba2.txt","w",encoding="utf-8")

mi_archivo1.write("hola mundo") #si se puede escribir en un archivo abierto en modo escritura

mi_archivo1.close()

#metodo agregar

mi_archivo2 = open("Py/dia 6/prueba3.txt","a",encoding="utf-8")

mi_archivo2.write("\n hola mundo 2") #si se puede escribir en un archivo abierto en modo agregar

mi_archivo2.close()

#metodo writelines
mi_archivo3 = open("Py/dia 6/prueba4.txt","w",encoding="utf-8")

lineas = ["hola mundo 1\n", "hola mundo 2\n", "hola mundo 3\n"]
mi_archivo3.writelines(lineas)

mi_archivo3.close()

# abrir mi_archivo.txt y cambiar contenido a Nuevo texto
mi_archivo4 = open("Py/dia 6/prueba1.txt","w",encoding="utf-8")
mi_archivo4.write("Nuevo texto")
mi_archivo4.close()
# abrir mi_archivo.txt y imprimir en pantalla el contenido
mi_archivo5 = open("Py/dia 6/prueba1.txt","r",encoding="utf-8")
print(mi_archivo5.read())
mi_archivo5.close()