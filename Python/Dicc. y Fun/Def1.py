
# Aquí se crea la función "saludar"
def saludar():

    print("saludo")

# Aquí se crea la función "retornarnumero" y aquíse usa la función return la cyal retorna en este caso el numero 1

def retornarnumero():

    return 1


saludar()

retornarnumero()

# Si en la función se retorna 1, se imprime "devolvió un uno"
if retornarnumero()==1:

    print("devolvió un uno")

# Si no, se imprime lo siguiente:
else:

    print("No devolvió un uno")