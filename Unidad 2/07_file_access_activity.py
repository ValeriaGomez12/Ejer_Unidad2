'''
Autor: Cinthia Valeria Gomez Luna
Fecha: 20 de octubre del 2022
'''

devices=[]
file=open("devices.txt","a")
while True:
    newItem= input("Se debera ingresar el nuevo newitem: ")
    if newItem == "exit":
        print("All done!")
        newItem=newItem.strip()
        break
    else:
        file.write(newItem +"\n")
    
file.close()
print(devices)


