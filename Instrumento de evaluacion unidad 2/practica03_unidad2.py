import urllib.parse
import requests


main_api = 'https://api.disneyapi.dev/character?'
key = "90bcdcff6daf4589a32a79c5adc61719"

while True:
    personaje = input("Ingresa el nombre de tu personaje favorito de Disney: ")
    if personaje == "salir" or personaje == "s":
        break

    url = main_api + urllib.parse.urlencode({ "name": str(personaje)})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["count"]

    if json_status > 0:
        data = json_data["data"][0]
        films = data["films"]
        print ("****************")
        print("Personaje: " + (data["name"]) )
        print("Películas y/o participaciones: ")
        for film in films:
            print(" * " + film)

    else:
        print("Sin información")
