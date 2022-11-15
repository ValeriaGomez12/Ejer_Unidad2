import urllib.parse
#Se deberan importar los modulos existentes
import requests
#main_api esta debera ser la url a la cual estara accediendo

import json
#se importara el json 

main_api = "http://www.mapquestapi.com/directions/v2/route?"
# este debera ser el  parámetro para punto de origen'''
address = ''
key = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"
#la llave que creamos 

url = main_api + urllib.parse.urlencode({'address':address}) + '&key=' + key
#se debera crear una variable que usando el método get

json_data = requests.get(url).json()
print(json_data)
#deber imprimir los datos del json 
 

print("URL: " + (url))
#tendra que imprimir la url 


json_data = requests.get(url).json()
json_status = json_data["info"] ["statuscode"]
#debra imprimir el estado de la solicitud 

#Se imprimira la api Status
if json_status == 0:
    print("API Status: " + str(json_status) + "= A successful route call.\n")
  
# se debera utilizar el while para las funciones 
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
    print("Miles:           " + str(json_data["route"]["distance"]))
    print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
    print("=============================================")

print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))

print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")


if json_status == 0:{
    
}

      
elif json_status == 402:
        print("**********************************************")
        print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print("=============================================")

elif json_status == 402:
        print("**********************************************")
        print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print("=============================================")
else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + ", Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
