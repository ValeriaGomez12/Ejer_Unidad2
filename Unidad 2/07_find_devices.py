'''
Autor: Cinthia Valeria Gomez Luna
Fecha: 20 de octubre del 2022
'''

file = open("devices.txt", "r")
dispo = input ("Debes ingresar el dispositivo que deseas ")


for line in file:
    line = line.strip()
    if "Switch" in line:
        print(line)
    else:
        
        print("tu dispositivo no se encontro")
        
file.close()
