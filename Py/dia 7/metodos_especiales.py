""" metodos especiales"""
mi_lista = [1, 2, 3]

print(len(mi_lista))

class Perro:
    """ esta es una clase perro """
    pass

mi_perro = Perro()
print(mi_lista)
print(mi_perro)

class CD:
    """este es un cd"""
    def __init__(self, autor, titulo, nro_canciones):
        self.autor = autor
        self.titulo = titulo
        self.nro_canciones = nro_canciones
    def __str__(self):
        return f"CD {self.titulo} del cantante {self.autor} con {self.nro_canciones} canciones "
    def __len__(self):
        return self.nro_canciones

cd_1 = CD("Zen P", "Afortunado", 13)
print(str(cd_1))
print(cd_1)
print(len(cd_1))