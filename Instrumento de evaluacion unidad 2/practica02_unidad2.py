import urllib.parse
import requests


main_api = "https://newsapi.org/v2/everything?"
key = "90bcdcff6daf4589a32a79c5adc61719"



while True:
     
    q= input("Ariculo: ")
    if q == "salir" or q == "s":
        break
    orig= input("Autor: ")
    if orig == "salir" or orig == "s":
        break

    url = main_api + urllib.parse.urlencode({ "q":q, "apiKey":key, "from":orig})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["status"]
    
   

   
    if json_status == "ok":
        print ("****************")
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Articulo: " + (q) )
        print("Autor: "+ (orig))
        print("Description:   " + str(json_data["articles"][0]["description"]))
        print("Publicación:   " + str(json_data["articles"][0]["publishedAt"]))
        print("****************")
    else:
       print("****************")
       print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
       print("****************\n")
       print("=============================================")
