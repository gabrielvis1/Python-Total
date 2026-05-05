"""
Archivo: prueba_test.py
Ejecuta pruebas unitarias sobre el archivo funciones_test.py
"""

import unittest
# Importamos las funciones desde nuestro otro archivo
from funciones_test import sumar, restar, a_mayusculas, a_minusculas, texto_a_binario

class TestFunciones(unittest.TestCase):

    def test_sumar(self):
        # Probamos números positivos, negativos y ceros
        self.assertEqual(sumar(10, 5), 15)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(5, 10), -5)
        self.assertEqual(restar(-5, -5), 0)

    def test_a_mayusculas(self):
        self.assertEqual(a_mayusculas("hola mundo"), "HOLA MUNDO")
        self.assertEqual(a_mayusculas("Python 3.10"), "PYTHON 3.10")
        
        # Probamos que levante un error si le pasamos un número en vez de texto
        with self.assertRaises(ValueError):
            a_mayusculas(123)

    def test_a_minusculas(self):
        self.assertEqual(a_minusculas("HOLA MUNDO"), "hola mundo")
        self.assertEqual(a_minusculas("PyThOn"), "python")

    def test_texto_a_binario(self):
        # La letra 'A' en binario es 01000001
        self.assertEqual(texto_a_binario("A"), "01000001")
        # Probamos una palabra corta ("hola")
        resultado_esperado = "01101000 01101111 01101100 01100001"
        self.assertEqual(texto_a_binario("hola"), resultado_esperado)

# Este bloque le dice a Python que corra las pruebas si ejecutamos este archivo
if __name__ == '__main__':
    unittest.main()