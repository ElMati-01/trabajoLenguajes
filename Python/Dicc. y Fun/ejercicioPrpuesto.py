
# equipos= {}

# class tienda:
#   def __init__(self, ID, dispositivo, novedad):
#     self.ID= ID
#     self.dispositivo=dispositivo
#     self.novedad=novedad

#   #Agregar equipo

#   def agregarEquipo(self):
#     ID = int(input("Ingrese un ID: "))
#     dispositivo = input("Ingrese dispositivo: ")

#     if ID not in equipos or dispositivo not in equipos:

#       equipos[ID] = {"id": ID, "dispositivo":dispositivo, "novedad": []}
#       return
    
#     else:
#       print("Ya se encuentra en la base de datos")
#       return
    

#   # Agregar novedad   
   
#   def novedad():
#     ID= int(input("Selecione ID: "))
    
#     if ID in equipos:
#       fecha = input("Registrar fecha por YYYY/MM/DD")
#       descripcion = input("Agregar un comentario: ")
#       equipos[ID]["novedad"].append({"fecha": fecha, "descripcion": descripcion})
#       print ("Se agregó la novedad")
#       return

#     else:
#       ("No aparece")
#       return
    
#   # Buscar producto

#   def buscar():
#       ID= int(input("Selecione ID: "))
    
#       if ID in equipos:
#           print(f"dispositivo y su infomación: {equipos}")
#           return
      
#       else:
#         print("No aparece")
#         return

#   # Buscar productos con novedades

#   def consultarNovedad():
#     novedades= [ID for ID, equipos in equipos.items() if equipos['novedad']]
#     if novedades:
          
#           for ID in novedades:
#               equipos = equipos[ID]
#               print(f"{equipos}")

#               for novedad in equipos['novedad']:
#                   print(f"Fecha: {novedad['fecha']}, Descripción: {novedad['descripcion']}")
#                   return
#   # Eliminar equipo

#   def eliminar():
#       ID = input("Ingresa ID delequipo que desea eliminar: ")
#       if ID in equipos:
#           del equipos[ID]
#           print("Se ha eliminado")
#           return
      
#       else:
#           print("Equipo no encontrado")
#           return
        

#Agregar dispositivos

equipos= {}

#Agregar equipo

def agregarEquipo():
  ID = int(input("Ingrese un ID: "))
  dispositivo = input("Ingrese dispositivo: ")

  if ID not in equipos or dispositivo not in equipos:

    equipos[ID] = {"id": ID, "dispositivo":dispositivo, "novedad": []}
  
  else:
    print("Ya se encuentra en la base de datos")

# Agregar novedad

def novedad():
  ID= int(input("Selecione ID: "))
  
  if ID in equipos:
    fecha = input("Registrar fecha por YYYY/MM/DD")
    descripcion = input("Agregar un comentario: ")
    equipos[ID]["novedad"].append({"fecha": fecha, "descripcion": descripcion})
    print ("Se agregó la novedad")

  else:
    ("No aparece")

# Buscar producto
def buscar():
    ID= int(input("Selecione ID: "))
  
    if ID in equipos:
        print(f"dispositivo y su infomación: {equipos}")
    
    else:
       print("No aparece")

# Buscar productos con novedades

def consultarNovedad():
   novedades= [ID for ID, equipos in equipos.items() if equipos['novedad']]
   if novedades:
        
        for ID in novedades:
            equipos = equipos[ID]
            print(f"{equipos}")

            for novedad in equipos['novedad']:
                print(f"Fecha: {novedad['fecha']}, Descripción: {novedad['descripcion']}")

# Eliminar equipo

def eliminar():
    ID = input("Ingresa ID delequipo que desea eliminar: ")
    if ID in equipos:
        del equipos[ID]
        print("Se ha eliminado")
    else:
        print("Equipo no encontrado")














