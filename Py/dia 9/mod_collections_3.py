from collections import namedtuple

persona = namedtuple("persona",["nombre", "edad", "peso"])
ariel = persona("Ariel", 40, 80)

print(ariel)
