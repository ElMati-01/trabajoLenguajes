
# Aquí hacemos una operación en donde queremos hallar la raiz del numero propuesto

# Se crea la funcion "raiz" y "value" será el valor que se le asigne a la operación

def raiz(value):

    return value ** (1/2)

# Una vez registrado el valor "value" se retorna a la operación de la raiz y despues se imprime el resultado

print(f'La raiz cuadrada es: {raiz(4)}')


# Aquí se crea una función para validar si el parametro cumple como objeto

def validarsiexiste(obj):
# Si es objeto, aparece esto:

    if obj:

        print(f"{obj} is True")
# Si no es objeto, aparece esto:

    else:

        print(f"{obj} is False")

validarsiexiste(1)