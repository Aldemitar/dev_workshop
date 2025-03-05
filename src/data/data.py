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
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass