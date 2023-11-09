# Funciones anónimas «lambda»

# Aquíse refleja una función de una manera un poco mas peculiar, en este caso se puede ver el parametro que es tel cual está almacenando una función con len
numero_palabras = lambda t: len(t.strip().split())

# Aquí se imprimen cuantas palabras existen en la oración, gracias al len y separado con un strip y split
print(numero_palabras("hola, esto es una prueba con lambda"))

