"""Explicación de polimorfismo en animales."""

class Vaca:
    """Representa a una vaca que puede hablar."""
    def __init__(self, nombre):
        """Inicializa el nombre de la vaca."""
        self.nombre = nombre
    def hablar(self):
        """Imprime el sonido característico de la vaca."""
        print("mu")

class Oveja:
    """Representa a una oveja con un balido repetitivo."""
    def __init__(self, nombre):
        """Inicializa el nombre de la oveja."""
        self.nombre = nombre
    def hablar(self):
        """Imprime el sonido de la oveja tres veces usando un bucle."""
        for n in range(0, 3):
            print(f"Bee {n + 1}")

vaca1 = Vaca("Aurora")
oveja1 =Oveja("Nube")

vaca1.hablar()
oveja1.hablar()

animales_granja = [vaca1, oveja1]
for animal in animales_granja:
    animal.hablar()

def animal_habla(animales):
    """funcion que hace hablar a un animal"""
    animales.hablar()

animal_habla(vaca1)
animal_habla(oveja1)
