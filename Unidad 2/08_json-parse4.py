'''
Autor: Cinthia Valeria Gomez Luna
Fecha: 25 de octubre del 2022
'''

import json
import urllib.parse
from pip import main
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?"

orig = "Washington"
dest = "Baltimaore"
key = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"
url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to": dest})


json_data = requests.get (url).json()
print(json_data)

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"] ["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + "= A successful route call.\n")

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to":dest})
print("URL: " + (url))    


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
