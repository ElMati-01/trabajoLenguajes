import math


# Se crea la clase "Rectangulo"
class Rectangulo:

    # Atributos
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    # Metodo para hallar el area
    def area(self):
        return self.longitud * self.ancho

# Se crea la clase "Circulo"
class Circulo:
    
    #Atributos
    def __init__(self, radio):
        self.radio = radio

    # Metodo para hallar el area
    def area(self):
        return math.pi * self.radio**2


# Función para llamar a "area"
def calcular_area(figura):
    return figura.area()

# Aquí se crean objetos para poder llamar a rectangulo y circulo y al mismo tiempo se les otorga valores
rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)

# Se imprime los resultados de "calcular_area"
print(calcular_area(rectangulo))  
print(calcular_area(circulo))     
