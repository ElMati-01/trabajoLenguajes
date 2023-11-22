import time

class Equipo:

    def __init__(self, ID, dispositivo,):
        self.ID= ID
        self.dispositivo=dispositivo
        self.novedad=[]

    def agregarNovedades(self, fecha, descripcion):
        self.novedad.append({"fecha": fecha, "descripcion": descripcion})

    def buscar(self):
        return f"ID: {self.ID}, Dispositivo: {self.dispositivo}, Novedades: {self.novedad}"


class Novedad:

    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

    def __repr__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}"



#Agregar dispositivos

equipos= {}

#Agregar equipo

def agregarEquipo():
  ID = int(input("Ingrese un ID: "))
  dispositivo = input("Ingrese dispositivo: ")

  if ID not in equipos or dispositivo not in equipos:

    equipos[ID] =  Equipo(ID, dispositivo)

    print ("Dispositivo agregado")
  
  else:
    print("Ya se encuentra en la base de datos")

# Agregar novedad

def novedad():
  ID= int(input("Selecione ID: "))
  
  if ID in equipos:
    fecha = input("Registrar fecha por YYYY/MM/DD")
    descripcion = input("Agregar un comentario: ")
    
    novedad = Novedad(fecha, descripcion)
    equipos[ID].novedad(novedad)


  else:
    ("No aparece")

# Buscar producto
def buscar():
    ID= int(input("Selecione ID: "))
    
    equipo = equipos[ID]

    if ID in equipos:
        print(f"dispositivo y su infomación: {equipo.buscar()}")
    
    else:
       print("No aparece")

# Buscar productos con novedades

def consultarNovedad():
   novedades= [ID for ID in equipos if ID.novedades]
   if novedades:
        
        for ID in novedades:
            equipos = equipos[ID]
            print(f"{equipos.buscar()}")

            for novedad in equipos['novedad']:
                print(novedad)

# Eliminar equipo

def eliminar():
    ID = input("Ingresa ID delequipo que desea eliminar: ")
    if ID in equipos:
        del equipos[ID]
        print("Se ha eliminado")
    else:
        print("Equipo no encontrado")


# Abrir bucle para ejecutar un menú

confirmacion = input("¿Desea iniciar?: ")

# Se confirma si se quiere iniciar
if confirmacion.upper() == "SI":

    # Si se digita "SI" el programa se ejecuta y se da a elegir la opción que se desea ejecutar

    while confirmacion.upper() == "SI":
        
        time.sleep(1)

        x= int(input("¡Bienvenido! Digite '1' para agregar un producto\n '2' para agregar una novedad\n '3' para buscar un producto\n '4' para buscar productos con novedades\n '5' para eliminar un producton\n Digite numero: "))

        if x == 1:
            agregarEquipo()

        elif x == 2:
            novedad()

        elif x == 3:
            buscar()

        elif x == 4:
            consultarNovedad()

        elif x == 5:
            eliminar()

        else:
            print("Opción no valida")
        

        confirmacion = input("¿Desea continuar?: ")

# Si la confirmación es diferente a "SI" se termina el programa
elif confirmacion != "SI":

    print("\n Hasta la proxima")











    
        