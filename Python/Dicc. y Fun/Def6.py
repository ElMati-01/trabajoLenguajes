
# Aquí a traves de una variable se asignan parametros en el cual x e y equivalen a "X" and "Y"

operadorand = lambda x, y: x & y

for i in range(2):

    for j in range(2):

        print(f"{i} & {j} = {operadorand(i, j)}")

#  Aquí se está haciendo una especie de caulciladora de numeros binarios, los valores se impriminen hasta 2 gracias al for.
# el for itera sobre los números del 0 al 1 . La variable j se utiliza para almacenar el número actual en el bucle.