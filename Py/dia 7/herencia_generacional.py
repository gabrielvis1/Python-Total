""" Herencia generacional en Python """
class Abuelo:
    """ Clase que representa al abuelo, con atributos y métodos básicos.  """
    def hablar(self):
        """ Método que simula el habla del abuelo.  """
        print("Hola, soy el abuelo.")
class Madre:
    """ Clase que representa a la madre, sin relación de herencia con abuelo.  """
    def reir(self):
        """ Método que simula la risa de la madre.  """
        print("Ja ja ja")
    def hablar(self):
        """ Método que simula el habla de la madre.  """
        print("Hola, soy la madre.")
class Padre(Abuelo):
    """ Clase que representa al padre, heredando de abuelo.  """
class Hijo(Padre, Madre):
    """ Clase que representa al hijo, heredando de padre.  """

mi_hijo = Hijo()
mi_hijo.hablar()  # Esto demostrará que el hijo puede usar el método
                  #hablar heredado del abuelo a través del padre.
mi_hijo.reir()   # Esto demostrará que el hijo puede usar el método reir heredado de la madre.

print(Hijo.__mro__)  # Esto muestra el orden de resolución de métodos (MRO) para la clase Hijo.
