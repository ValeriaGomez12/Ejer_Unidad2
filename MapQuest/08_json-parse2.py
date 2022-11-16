'''
Descripción:Documentacion del las diapositivas 
Autor: Cinthia Valeria Gomez Luna 
Fecha: 15 de noviembre del 2022
'''
#Se deberan importar los modulos existentes
import urllib.parse

#main_api esta debera ser la url a la cual estara accediendo
import requests

#este debera ser el  parámetro para punto de origen
main_api = "http://www.mapquestapi.com/directions/v2/route?"

#Dependera el origen del creador
orig = "Washington"

#Se debera escribir el destino dependera del usuario
dest = "Baltimaore"

#nuestra llave  que sera clave del consumidor de la API 
key  = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"

#se debera crear una variable que usando el método get
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Se debera imprimir el json
json_data = requests.get(url).json()
print(json_data)

#Se imprimira la url y se utlizo un print
print("URL: " + (url))

# se debera Cree una variable que usando el método get para solicitar datos JSON de la URL enviada
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

# Se debera crear una ins if que debera imprir el estado de la solicitud si la clave del código de estado se establece en el valor 0
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")