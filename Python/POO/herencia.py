class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass # El "pass" sirve para cuando la sintaxis de Python requiere una declaración pero no se necesita hacer ninguna acción adicional

# Aquí como parametro se pone "animal" ya que se heredarán los atributos de esta clase
class Perro(animal):

    # Se crea un metodo el cual devuelve la palabra "Guau" en "hacer_sonido"
    def hacer_sonido(self):
        return "Guau"

# Se le define un valor a "nombre" desde "animal"
perro = Perro("Buddy")

# Desde "perro" podemos acceder a los atributos de animal ya que este los a heredado

print(perro.nombre)       
print(perro.hacer_sonido())
