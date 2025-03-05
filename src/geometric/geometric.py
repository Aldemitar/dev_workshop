import math

class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Área del rectángulo
        """
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)
    
    def area_circulo(self, radio):
        return math.pi * radio ** 2
    
    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio
    
    def area_triangulo(self, base, altura):
        return 0.5 * base * altura
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
       return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1 and lado1 > 0 and lado2 > 0 and lado3 > 0
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return 0.5 * (base_mayor + base_menor) * altura
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return 0.5 * diagonal_mayor * diagonal_menor
    
    def area_pentagono_regular(self, lado, apotema):
        return 0.5 * 5 * lado * apotema
    
    def perimetro_pentagono_regular(self, lado):
       return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        return 3 * lado * apotema
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
    
    def volumen_cubo(self, lado):
        return lado ** 3
    
    def area_superficie_cubo(self, lado):
        return 6 * (lado ** 2)
    
    def volumen_esfera(self, radio):
        return (4/3) * math.pi * (radio ** 3)
    
    def area_superficie_esfera(self, radio):
        return 4 * math.pi * (radio ** 2)
    
    def volumen_cilindro(self, radio, altura):
        return math.pi * (radio ** 2) * altura
    
    def area_superficie_cilindro(self, radio, altura):
        return 2 * math.pi * radio * (radio + altura)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            raise ZeroDivisionError("La pendiente de una línea vertical es infinita.")
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass
