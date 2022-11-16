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
#Se debera imprimir los datos
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
       print("Miles:           " + str(json_data["route"]["distance"]))
       print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
       print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
       print("=============================================\n")
    elif json_status == 402:
       print("****************")
       print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
       print("****************\n")
       print("=============================================")
    else:
       print("************************")
       print("For Staus Code: " + str(json_status) + ", Refer to:")
       print("https://developer.mapquest.com/documentation/directions-api/status-codes")
       print("************************\n")
