""" explicacion de polimorfismo """
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hablar(self):
        print ("mu")
        
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        for n in range(0,3):
            print(f"Bee {n + 1 }")
