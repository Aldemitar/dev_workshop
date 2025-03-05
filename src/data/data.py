class Pila:
    def __init__(self):
        self.elementos = []
    def push(self, valor):
        self.elementos.append(valor)
    def pop(self):
        if self.is_empty():
            raise IndexError("No se puede hacer pop en una pila vacía")
        return self.elementos.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("No se puede hacer peek en una pila vacía")
        return self.elementos[-1]
    def is_empty(self):
        return len(self.elementos) == 0

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, valor):
        self.elementos.append(valor)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("No se puede hacer dequeue en una cola vacía")
        return self.elementos.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("No se puede hacer peek en una cola vacía")
        return self.elementos[0]

    def is_empty(self):
        return len(self.elementos) == 0

class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista.reverse()
        return lista
    
    def buscar_elemento(self, lista, elemento):
         if elemento in lista:
            return lista.index(elemento)
         return -1
    
    def eliminar_duplicados(self, lista):
        vistos = set()
        resultado = []
        for elemento in lista:
            if (elemento, type(elemento)) not in vistos:
                resultado.append(elemento)
                vistos.add((elemento, type(elemento)))
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0  
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista or posiciones == 0:
            return lista
        n = len(lista)
        posiciones = posiciones % n
        return lista[-posiciones:] + lista[:-posiciones]
    
    def encuentra_numero_faltante(self, lista):
        if not lista:
            return None
        n = len(lista) + 1
        suma_esperada = (n * (n + 1)) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        return set(conjunto1).issubset(set(conjunto2))
    
    def implementar_pila(self):
        pila = Pila()
        return {
            "push": pila.push,
            "pop": pila.pop,
            "peek": pila.peek,
            "is_empty": pila.is_empty
        }
    
    def implementar_cola(self):
            cola = Cola()
            return {
                "enqueue": cola.enqueue,
                "dequeue": cola.dequeue,
                "peek": cola.peek,
                "is_empty": cola.is_empty
            }    
    
    def matriz_transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)]