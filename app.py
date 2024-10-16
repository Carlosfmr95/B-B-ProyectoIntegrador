import requests
import os
from dotenv import load_dotenv

load_dotenv()

APPID = os.getenv('APIKEY')

unit = "metric" 

try:
    print("###### APP DEL CLIMA ######")
    city = input("+ Ingrese la ciudad de la que desee consultar el clima: ")
    city = city.lower()

    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&lang=es&units={unit}')
    weather_dictionary = r.json()
    print(f"""
############################################################
+ En {city.capitalize()}:
    ■ TEMPERATURA ACTUAL: {weather_dictionary['main']['temp']}°
    ■ DESCRIPCION: {(weather_dictionary['weather'][0]['description'].capitalize())}
    ■ TEMPERATURA MÍNIMA: {(weather_dictionary['main']['temp_min'])}° 
    ■ TEMPERATURA MÁXIMA: {(weather_dictionary['main']['temp_max'])}°
    ■ PORCENTAJE DE HUMEDAD: {weather_dictionary['main']['humidity']}% 
############################################################ 
""")
except: 
    print("# Error inesperado. Reinicie para intentar nuevamente")