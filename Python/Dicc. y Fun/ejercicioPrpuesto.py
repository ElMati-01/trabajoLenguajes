
#Agregar dispositivos

def agregarEquipo(equipos, ID, dispositivo):


  equipos.setdefault(ID, {})
  equipos[ID] = {"id": ID, "dispositivo":dispositivo, "novedad": []}
  return equipos

equipos = {}

equipo1 = {'id': 1, 'cargador': 'HP', 'mouse': 'Logitech'}
equipo2 = {'id': 2, 'cargador': 'Dell', 'mouse': 'Razer'}

equipos = agregarEquipo(equipos, 1, equipo1)
equipos = agregarEquipo(equipos, 2, equipo2)

for id, dispositivo in equipos.items():

  print(f"dispositivo: {dispositivo}")

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