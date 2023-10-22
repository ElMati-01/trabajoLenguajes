# Aquí se almacenan los datos en estas listas
aprendices = []
edades = []


# Con un rango de 30 personas se registra el nombre y la edad de cada uno manualmente.
for i in range (1,31):
    datoAprendiz = input("Ingrese su nombre: ")
    datoEdad = int(input("Ingrese la edad: "))
    aprendices.append(datoAprendiz)
    edades.append(datoEdad)

# Aquí se imprimen las listas
print(f"Listado aprendices: {aprendices}")
print(f"Listado edades: {edades}")

########################################### Segunda forma ####################################

# Se ingresa los datos necesarios.
datoAprendiz = input("Ingrese su nombre: ")
datoEdad = input("Ingrese la edad: ")

# Aquí se pide que se separe los datos con comas si se va a registrar muchos datos a la vez.
dato1 = datoAprendiz.split(',')
dato2 = datoEdad.split(',')

# Como la función .split no acepta datos numericos y solo tipo cadena, esta operación se encarga de convertir esos datos a numeros a traves de un for...

valorNumero= [int(x) for x in dato2]

# Aquí se almacenan los datos  ingresados. (el .extend ayuda a agregar mas funciones a un codigo. Aquí estamos simplemente juntandolo con otra variable como también otra lista)
aprendices = []
aprendices.extend(dato1)
edades = []
edades.extend(valorNumero)

# Aquí s eguardan los datos y se llevan al final de la lista.
aprendices.append(datoAprendiz)
edades.append(datoEdad)

# Aquí se imprimen los datos de las lista.

print(f"Listda de apredices: {aprendices}")
print(f"Lista edades: {edades}")

