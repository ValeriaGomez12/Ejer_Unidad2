'''
Nombre de la api Random facts api 
Descripción de la API
API Portal / Home Page
'''
from urllib.parse import urlparse
import requests
import json
main_api = requests.get('https://api.fungenerators.com')
print("¿Quiere que le diga un dato curioso?/n")
print("1 = Si o 2 = No")
r = input()
data =  main_api.json()

