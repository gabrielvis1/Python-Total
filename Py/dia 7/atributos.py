"""Atributos de clase y de instancia"""

class Pajaro:
    alas = True  # Atributo de clase
    
    def __init__(self, color,especie):
        self.color = color
        self.especie = especie
    def piar(self):
        return "Pío pío"
    def volar(self, metros):
        return f"El pájaro vuela {metros} metros."
    def pintar_negro(self):
        self.color = "negro"
        print("El pájaro se ha pintado de negro.")
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pájaro pone {cantidad} huevos.")
        
    @staticmethod
    def mirar():
        print("El pájaro mira con sus ojos.")

mi_pajaro = Pajaro("rojo", "Tucán")
print(mi_pajaro.color)  # Imprime "rojo"
print(mi_pajaro.especie)  # Imprime "Tucán"
print(mi_pajaro.alas)  # Imprime "True"
print(mi_pajaro.piar())  # Imprime "Pío pío"
print(mi_pajaro.volar(10))  # Imprime "El pájaro vuela 10 metros"
mi_pajaro.color = "azul"
print(mi_pajaro.color)  # Imprime "azul"

pajaro = Pajaro("verde", "Paradero")
print(pajaro.piar())  # Imprime "Pío pío"
print(pajaro.volar(15))  # Imprime "El pájaro vuela 15 metros"
print(pajaro.piar())  # Imprime "Pío pío"

canario = Pajaro("amarillo", "Canario")
canario.piar()  # Imprime "Pío pío"
canario.volar(20)  # Imprime "El pájaro vuela 20 metros"
canario.pintar_negro()  # Imprime "El pájaro se ha pintado de negro"

canario.poner_huevos(10)  # Imprime "El pájaro pone 10 huevos"
