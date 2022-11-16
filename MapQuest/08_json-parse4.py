'''
Descripción:Documentacion del las diapositivas 
Autor: Gomez Luna Cinthia Valeria
Fecha: 15 de Noviembre del 2022
'''
#Se deberan importar los modulos existentes
import urllib.parse

#main_api esta debera ser la url a la cual estara accediendo
import requests

#este debera ser el  parámetro para punto de origen
main_api = "http://www.mapquestapi.com/directions/v2/route?"

#nuestra llave  que sera clave del consumidor de la API 
key  = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"

# Beberas escribir el origen y el destino para asi poderlos agregar a un ciclo
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
 #Se debera agregar una declaración if esta debera ser despues de la variable  
dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
