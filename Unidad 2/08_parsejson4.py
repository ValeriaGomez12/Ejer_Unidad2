import urllib.parse
#Se deberan importar los modulos existentes

import requests
#main_api esta debera ser la url a la cual estara accediendo

main_api = "http://www.mapquestapi.com/directions/v2/route?"
# este debera ser el  parámetro para punto de origen'''

key  = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

print("URL: " + (url))
#se debera crear una variable que usando el método get '''

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
#debra imprimir el estado de la solicitud 
 
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

#ciclo while 
 
# The "while true" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    '''declaración if después de la variable de dirección para verificar si el usuario ingresa o quit.'''
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
    print("Miles:           " + str(json_data["route"]["distance"]))
    print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
    print("======================")
