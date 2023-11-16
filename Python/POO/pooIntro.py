
# nombre de la clase
class miClase:
    # Aquí se ponen los "atributos" de la clase
    atributo1 = "Hola"
    atributo2 = 42

    # Aquí se ponen los "métodos" de la clase

    def metodo1(self): 
        return "método 1"

    def metodo2(self, parametro):
        return f"método 2 + {parametro}"
    
    # "Self" y "Parametro" son los objetos

# Aquí se crea una clase para poder llamar a "miClase"

objetoClase = miClase()


# Con el nombre de el objeto mas un "." podemos llamar a un atributo o un metodo

# Llamada de un atributo y lo imprime
print(objetoClase.atributo1)
# Llamada de un método y lo imprime
print(objetoClase.metodo1()) 

# Aquí se llama al método "metodo2" y se le impone un valor al objeto "parametro"
print(objetoClase.metodo2("ejemplo")) 



