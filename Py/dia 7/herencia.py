"""Ejemplo de herencia en Python"""

class Animal:
    def __init__(self, edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido.")

class Pajaro(Animal):
    pass

class Mamifero(Animal):
    pass


print(Animal.__subclasses__())
print(Pajaro.__bases__)
piolin = Pajaro(2,"verde")
piolin.nacer()
