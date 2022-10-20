'''
Autor: Cinthia Valeria Gomez Luna
Fecha: 20 de octubre del 2022
'''

file = open("devices.txt", "r")
dispo = input ("Debes ingresar el dispositivo que deseas ")
isFound = False


for line in file:
    line = line.strip()
    if dispo in line and len(dispo) > 3:
        isFound = True
        print(line)
        
  if isFound == False
        print("tu dispositivo no se encontro")
        
file.close()
