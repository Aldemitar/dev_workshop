class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.replace(" ", "").lower()
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        return texto[::-1]
    
    def contar_vocales(self, texto):
            texto = texto.lower()
            return sum(1 for char in texto if char in "aeiou")
    
    def contar_consonantes(self, texto):
        texto = texto.lower()
        return sum(1 for char in texto if char.isalpha() and char not in "aeiou")
    
    def es_anagrama(self, texto1, texto2):
            texto1 = texto1.replace(" ", "").lower()
            texto2 = texto2.replace(" ", "").lower()
            return sorted(texto1) == sorted(texto2)
    
    def contar_palabras(self, texto):
        palabras = texto.strip().split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.strip().split())
    
    def es_numero_entero(self, texto):
        try:
            int(texto)
            return True
        except ValueError:
            return False
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = []
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
                resultado.append(nuevo_caracter)
            else:
                resultado.append(caracter)
        return ''.join(resultado)

    
    def descifrar_cesar(self, texto, desplazamiento):
        resultado = []
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_caracter = chr((ord(caracter) - base - desplazamiento) % 26 + base)
                resultado.append(nuevo_caracter)
            else:
                resultado.append(caracter)
        return ''.join(resultado)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        i = 0
        while i < len(texto):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
                i += len(subcadena)
            else:
                i += 1
        return posiciones