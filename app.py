import requests
import os
from dotenv import load_dotenv

load_dotenv()

print("###### APP DEL CLIMA ######")

city = input("+ Ingrese la ciudad de la que desee consultar el clima: ")

APPID = os.getenv('APIKEY')

lang = 'es'

medida = 'metric'

r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&lang={lang}&units={medida}')
diccionarioClima = r.json()

print(diccionarioClima)

print(diccionarioClima['weather'][0]['main'])

print(diccionarioClima['weather'][0]['description'])
                                                               
    

print("Algo fallo (XoX)")