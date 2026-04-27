""" Mas sobre herencia en Python """

class Animal:
    """Clase que representa el comportamiento base de un animal."""
    def __init__(self, edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        """ Método que simula el nacimiento de un animal. """
        print("Este animal ha nacido.")
    def hablar(self):
        """ Método que simula el sonido que hace un animal. """
        print("Este animal hace un sonido.")
class Pajaro(Animal):
    """Clase que representa el compor específico de un pájaro, heredando de la clase Animal."""
    def __init__(self, edad, color, altura_vuelo, velocidad_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
        self.velocidad_vuelo = velocidad_vuelo

    def hablar(self):
        """ Método que simula el canto de un pájaro. """
        print("Pío pío")
    def volar(self, metros):
        """ Método que simula el vuelo de un pájaro. """
        print(f"Este pájaro está volando {metros} metros.")

class Mamifero(Animal):
    """Clase que representa el comportamiento específico de un mamífero."""
      # Al no tener atributos nuevos, hereda el __init__ de Animal solito.

simba = Animal(10,"amarillo")
piolin = Pajaro(2,"amarillo", 10, 5)
michi = Mamifero(3,"gris")
simba.nacer()
piolin.hablar()
michi.hablar()
