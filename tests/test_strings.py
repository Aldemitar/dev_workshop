import pytest
from src.strings.strings import Strings

class Strings:
    def es_palindromo(self, cadena):
        cadena = cadena.replace(" ", "").lower()
        return cadena == cadena[::-1]

    def invertir_cadena(self, cadena):
        return cadena[::-1]

    def contar_vocales(self, cadena):
            cadena = cadena.lower()
            return sum(1 for char in cadena if char in "aeiou")
    
    def contar_consonantes(self, cadena):
        cadena = cadena.lower()
        return sum(1 for char in cadena if char.isalpha() and char not in "aeiou")

    def es_anagrama(self, cadena1, cadena2):
            cadena1 = cadena1.replace(" ", "").lower()
            cadena2 = cadena2.replace(" ", "").lower()
            return sorted(cadena1) == sorted(cadena2)
    
    def contar_palabras(self, frase):
        palabras = frase.strip().split()
        return len(palabras)

    def palabras_mayus(self, frase):
        return frase.title()

    def eliminar_espacios_duplicados(self, frase):
        return ' '.join(frase.strip().split())

class TestStrings:
    def setup_method(self):
        self.strings = Strings()
    
    def test_es_palindromo(self):
        # Test con palíndromos simples
        assert self.strings.es_palindromo("ana") == True
        assert self.strings.es_palindromo("reconocer") == True
        # Test con palíndromos con espacios y mayúsculas
        assert self.strings.es_palindromo("Anita lava la tina") == True
        # Test con no palíndromos
        assert self.strings.es_palindromo("sigmotoa") == False
        assert self.strings.es_palindromo("mundo") == False
        # Test con cadena vacía
        assert self.strings.es_palindromo("") == True
    
    def test_invertir_cadena(self):
        # Test con cadenas simples
        assert self.strings.invertir_cadena("hola") == "aloh"
        assert self.strings.invertir_cadena("Python") == "nohtyP"
        assert self.strings.invertir_cadena("sigmotoA") == "Aotomgis"
        # Test con cadena vacía
        assert self.strings.invertir_cadena("") == ""
        # Test con un solo carácter
        assert self.strings.invertir_cadena("a") == "a"
    
    def test_contar_vocales(self):
        # Test con cadenas con vocales
        assert self.strings.contar_vocales("sigmotoa") == 4
        assert self.strings.contar_vocales("murcielago") == 5
        # Test con cadena sin vocales
        assert self.strings.contar_vocales("rhythm") == 0
        # Test con vocales en mayúsculas y minúsculas
        assert self.strings.contar_vocales("AeIoU") == 5
        # Test con cadena vacía
        assert self.strings.contar_vocales("") == 0
    
    def test_contar_consonantes(self):
        # Test con cadenas con consonantes
        assert self.strings.contar_consonantes("sigmotoa") == 4
        assert self.strings.contar_consonantes("Python") == 5
        # Test con cadena sin consonantes
        assert self.strings.contar_consonantes("aeiou") == 0
        # Test con consonantes en mayúsculas y minúsculas
        assert self.strings.contar_consonantes("PythOn") == 5
        # Test con cadena vacía
        assert self.strings.contar_consonantes("") == 0
    
    def test_es_anagrama(self):
        # Test con anagramas simples
        assert self.strings.es_anagrama("roma", "amor") == True
        assert self.strings.es_anagrama("listen", "silent") == True
        assert self.strings.es_anagrama("ekans","sneak") == True
        # Test con anagramas con mayúsculas
        assert self.strings.es_anagrama("Dormitory", "Dirty room") == True
        # Test con no anagramas
        assert self.strings.es_anagrama("hello", "world") == False
        # Test con cadenas de diferente longitud
        assert self.strings.es_anagrama("python", "typhons") == False
    
    def test_contar_palabras(self):
        # Test con frases simples
        assert self.strings.contar_palabras("Hola mundo") == 2
        assert self.strings.contar_palabras("Python es divertido") == 3
        # Test con espacios múltiples
        assert self.strings.contar_palabras("  dev with sigmotoa    ") == 3
        # Test con cadena vacía
        assert self.strings.contar_palabras("") == 0
    
    def test_palabras_mayus(self):
        # Test con frases simples
        assert self.strings.palabras_mayus("hola mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("sigmotoa es genial") == "Sigmotoa Es Genial"
        # Test con palabras ya capitalizadas
        assert self.strings.palabras_mayus("Hola Mundo") == "Hola Mundo"
        # Test con espacios múltiples
        assert self.strings.palabras_mayus("  hola  mundo  ") == "  Hola  Mundo  "
        # Test con cadena vacía
        assert self.strings.palabras_mayus("") == ""
    
    def test_eliminar_espacios_duplicados(self):
        # Test con espacios múltiples
        assert self.strings.eliminar_espacios_duplicados("Hola  mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("  sigmotoa   es   genial  ") == "sigmotoa es genial"
        # Test sin espacios duplicados
        assert self.strings.eliminar_espacios_duplicados("Hola mundo") == "Hola mundo"
        # Test con cadena vacía
        assert self.strings.eliminar_espacios_duplicados("") == ""
    
    def test_es_numero_entero(self):
        # Test con números enteros
        assert self.strings.es_numero_entero("123") == True
        assert self.strings.es_numero_entero("-456") == True
        # Test con números no enteros
        assert self.strings.es_numero_entero("12.34") == False
        assert self.strings.es_numero_ent