# Lista 1

calificaciones = {

'nombre': 'Sandra',

'notafinal': 5.0

}

# Lista 2

calificaciones = {

'Sandra': 5.0,

'Adriana':5.0,

'Mauricio':4.5,

'Jose':2.5

}

# para cada par clave-valor, el bucle asigna la clave a la variable i y el valor a la variable j

for i, j in calificaciones.items():

    print(i,j)

# Agregar datos al diccionario después de creado

# calificaciones.update({"Rosa": 3.7, "German": 4.8})


print("Técnicas por clave")

# .keys se utiliza para obtener una de las claves de un diccionario

for i in calificaciones.keys():

    print(i)

# .values se utiliza para obtener uno de los valores del diccionario

print("Iterar por valor")

for j in calificaciones.values():

    print(j)
    
    
nombres = ['Maria', 'Sebastian', 'Ana']

edades = ['18', '25', '30']

for n, e in zip(nombres, edades):

    print('Tú nombre es {0} y tu edad {1}.'.format(n, e))