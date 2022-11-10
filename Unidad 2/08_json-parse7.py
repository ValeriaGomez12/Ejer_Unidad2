'''
Autor: Cinthia Valeria Gomez Luna
Fecha: 25 de octubre del 2022
'''

import json
#08_parse-json1.py
import urllib.parse
import requests
from pip import main

#create variables for API request 
main_api = "http://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "YrYI0yjA7ocl5gcgBEB551g3lqynmnHh"
url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to": dest})

#create the json request 
json_data = requests.get (url).json()
print(json_data)

#08_json.parse2.py print the url
print("url":  + (url))
json_data = requests.get(url).json()
json_status = json_data["info"] ["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + "= A successful route call.\n")

#add user input for adress 08:json-parse3.py
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("url" + (url))

# add quit funtionality 08_json-parse4.py
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    # 08_jsonparse5.py. parse and display trip data 
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
    print("Miles:           " + str(json_data["route"]["distance"]))
    print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
    print("=============================================")

#Convert imperial to metric
print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))

# Format to 2 decimal places 
print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

#08_json-parse6.py lterate through the directions data 08_json-parse6.py
print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")

#08_json-parse7.py Check for invalid user input 
if json_status == 0:{
    
}

      
elif json_status == 402:
        print("**********************************************")
        print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print("=============================================")
        
#json_status
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

