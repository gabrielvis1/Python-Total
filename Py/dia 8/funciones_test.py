"""
Archivo: funciones_test.py
Contiene funciones matemáticas y de manipulación de texto básicas.
"""

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def a_mayusculas(texto):
    """Convierte una cadena de texto a mayúsculas."""
    if not isinstance(texto, str):
        raise ValueError("El argumento debe ser texto (string).")
    return texto.upper()

def a_minusculas(texto):
    """Convierte una cadena de texto a minúsculas."""
    if not isinstance(texto, str):
        raise ValueError("El argumento debe ser texto (string).")
    return texto.lower()

def texto_a_binario(texto):
    """
    Convierte una cadena de texto a su representación en código binario.
    Cada letra se transforma en un bloque de 8 bits (ceros y unos).
    """
    if not isinstance(texto, str):
        raise ValueError("El argumento debe ser texto (string).")
    # ord(char) obtiene el valor numérico de la letra.
    # format(numero, '08b') convierte ese número a binario de 8 dígitos.
    return ' '.join(format(ord(caracter), '08b') for caracter in texto)
