# # Modificando parámetros mutables

# # Aquí vemos que se crea una función donde hay un argumento y un resultado, cada argumento estará almacenado en "result"
# def lista(arg, result=[]):

#     result.append(arg)

#     print(result)
# # Aquí se imprime los argumentos dados y los almacenados
# lista('domingo', [])



def listalimpia(arg, result=None):

# Aquí, si result es igual a none, crea una nueva lista y almacena los datos de arg.

    if result is None:

        result = []

        result.append(arg)

        print(result)

# Aquí se dan valores al parametro "arg" para después ser almacenados en la lista "result"
listalimpia("a")

listalimpia("b")