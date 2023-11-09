
# Funciones con Parámetros Posicionales

# Aquí se crea la función compra, la cual va a almacenar la marca, cantidady el valor total
def compra(marca,cantidad,valor):

    return dict(

    marca=marca,

    cantidad=cantidad,

    valor=valor*cantidad
    )

# Aquí se ingresan los datos a retornar en la función para que aparezca el total de la compra, todo a traves delorden y la poscición del los parametros

print(f' lo comprado fue:{compra("AMD",3,2500000)}')


# Funciones con Parámetros Nominales

# Aquí se crea la función compra, la cual va a almacenar la marca, cantidady el valor total

def compra(marca,cantidad,valor):

    return dict(

    marca=marca,

    cantidad=cantidad,

    valor=valor*cantidad

    )

# Aquí se ingresan los datos a retornar en la función para que aparezca el total de la compra de forma nominal especificando que valor va con que parametro
print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')

# Parámetros por defecto

# Aquí se crea la función compra, la cual va a almacenar la marca, cantidad y el valor. al parametro "valor" se le predetermina un dato fijo
def compra(marca,cantidad,valor=2500000):

    return dict(

    marca=marca,

    cantidad=cantidad,

    valor=valor*cantidad

    )

print(f' lo comprado fue:{compra("AMD",3)}')