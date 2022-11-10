import urllib.parse
#Se deberan importar los modulos existentes

import requests
#main_api esta debera ser la url a la cual estara accediendo

main_api = "http://www.mapquestapi.com/directions/v2/route?"

# este debera ser el  parámetro para punto de origen'''

orig = "Washington"
#tiene que ser el parametro que especifique el destino'''

dest = "Baltimaore"
#nuestra llave  que sera clave del consumidor de la API 
key  =  "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"

url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))

#se debera crear una variable que usando el método get '''

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
#debra imprimir el estado de la solicitud 
 
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
