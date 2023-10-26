

# Aquí se almacenan los datos en estas listas

x = input("Ingrese el nombre que desea buscar: ")
y = int(input("Ingrese la edad que desea buscar: "))

aprendices = ['Adriana Rincón','Sebastian Tovar', 'Juan Mahecha', 'Maria Buenaventura', 'Mathew Guarnizo', 'Kevin Hernan', 'Melissa Lopez', 'Vanesa Ladino', 'Stiven Ramirez', 'Esteban Prada', 'Kevin Botero', 'Sebastian Pinzon', 'Camila Alape', 'Kevin Londoño', 'Nicolas Fierro', 'Santiago Gomez', 'Marlon Lopez ', 'Stiwar Perez', 'Miguel Bernal', 'Maria Molano', 'Nicolas Paulo', 'Laura Benavides', 'Wilfrank', 'Dahiana', 'Nataly', 'Maria José', 'Cristian Peña', 'Paula', 'Kevin Eduardo', 'Yency', 'Matias Guzman']
edades = [17, 17, 17, 17, 17, 17, 17, 18, 17, 17, 17, 18, 23, 18, 18, 19, 18, 17, 18, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18]



if x in aprendices:
    print(f"Si se encuentra el nombre seleccionado: {x}")

    if y in edades:
        print(f"Si se encuentra el numero seleccionado: {y}")

else:
    print("No se encuentra la persona a quien busca")