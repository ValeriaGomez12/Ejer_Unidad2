import urllib.parse
import requests
import sys

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "YNCIxS3UM46l2drsTYgv9AIQSsvtGJtU"

while True:

    orig = input("Origen: ")
    if orig == "S":
        break

    dest = input("Destino: ")
    if orig == "S":
        break
    
    

    url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estatus de API: "+str(json_status)+"= Se encontro la Ruta.\n")
        print("Instrucciones de :" + str(orig) + "a:" + str(dest))
        print("Duración aproximada: "+str(json_data["route"]["formattedTime"]))
        print("Kilometros aproximados: "+str("{:2f}".format((json_data["route"]["distance"])*1.61))) 
        
        print("Inicios de intrucciones de la ruta")
        contador = 1

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("Paso No. "+str(contador) + ": " + str(each["narrative"]+ "(" + str("{:.2f}".format((each["distance"])*1.61) + "Kms.")))
            contador = contador + 1
            print("Fin de intrucciones de la ruta")
    elif json_status == 402:
        print("No se encontro la ruta")
    else:
        print("Se ha producido un error")