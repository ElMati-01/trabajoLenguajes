
# # Con atributos:


# class Persona:

#     # Atributos privados
#     def __init__(self, nombre, edad):

#         # Se usa ".__" para establecer como privado
#         self.__nombre = nombre  
#         self.__edad = edad      

#     # Se crea el método para obtener el atributo "nombre"
#     def obtener_nombre(self):
#         return self.__nombre
    
#     # Se crea el método para obtener el atributo "edad"
#     def obtener_edad(self):
#         return self.__edad

# # Crear un objeto "Persona" en el cual de otorga valores a los atributos
# persona = Persona("Juan", 30)


# # print(persona.__nombre) Generará un AttributeError

# # Aquí se accede a los atributos mediante métodos públicos

# print(persona.obtener_nombre())  
# print(persona.obtener_edad())    










# Con métodos: 


class MiClase:

    # Metodo privado:
    def __metodoPrivado(self):
        return "Este es un método privado"
    
    # Metodo publico:
    def metodo_publico(self):
        return self.__metodoPrivado()

# Se crea un objeto para llamar a la clase
objeto = MiClase()


# objeto.__metodo_privado()  Generará un AttributeError

# Llamar al método privado mediante un método público
print(objeto.metodo_publico())  