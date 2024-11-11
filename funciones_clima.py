import menu_inicio
import requests
import os
from dotenv import load_dotenv 
from colorama import Back
from datetime import datetime
import historial

global unidad
unidad = "metric"
global signoTemp
signoTemp = "°"
FILENAME = "historial_clima.txt"
dias_semana = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

def consulta_clima():
    global unidad
    global signoTemp
    load_dotenv()
    APPID = os.getenv('APIKEY')
    limpiar_consola()
    try:
        print(Back.CYAN + """
    + Ingrese la ciudad de la que desee consultar el clima: 
              """)
        ciudad = input("""
    >> """)
        ciudad = ciudad.lower()
        if not ciudad:
            raise ValueError("""
    No se ha ingresado ninguna ciudad.""")
        
        if ciudad.isdigit():
            raise ValueError("""
    El nombre de la ciudad no puede ser un número.""")


        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={APPID}&lang=es&units={unidad}')
        if r.status_code == 200:
            diccionario_clima = r.json()
            fecha_consulta = datetime.now()
            fecha_formateada = fecha_consulta.strftime("%Y-%m-%d %H:%M:%S")
            diccionario_clima['fecha'] = fecha_formateada
            historial.guardar_consulta(diccionario_clima, FILENAME) 
            limpiar_consola()
            print(Back.CYAN +f"""
    ##############################################
                  
    + En {ciudad.capitalize()}:

        ■ Temperatura Actual:   {diccionario_clima['main']['temp']}{signoTemp}
        ■ Descripción:          {diccionario_clima['weather'][0]['description'].capitalize()}{icono_clima(diccionario_clima['weather'][0]['description'])}
        ■ Temperatura Mínima:   {(diccionario_clima['main']['temp_min'])}{signoTemp}
        ■ Temperatura Máxima:   {(diccionario_clima['main']['temp_max'])}{signoTemp}
        ■ Humedad(%):           {diccionario_clima['main']['humidity']}%

    ##############################################
                """)
            reintento()
        else:
            if r.status_code == 404:
                print(f"""
    Error: No se encontró la ciudad '{ciudad}'.""") 
                reintento()                 
            else:
                print(f"""
    Error: No se pudo realizar la consulta (Código de estado: {r.status_code}).""")
                reintento()
    except requests.exceptions.RequestException as e:
        print(f"""
    Error: Ocurrió un problema con la conexión. Detalles: {e}""")
        reintento()
    except Exception as e:
        print(f"""
    Error inesperado: {e}""")
        reintento()


def cambiar_unidad():
    limpiar_consola()
    global unidad
    global signoTemp
    while(True):
        print("""
    -----------------
              
    Para cambiar a:

    [1] Celsius 
    [2] Fahrenheit 
              
    -----------------
            """)
        opcion_unidad=input("""
    >>""")
        if (opcion_unidad == "1"):
            unidad = "metric"
            signoTemp = "°"
            limpiar_consola()
            print("""
    --------------------------------------
    La unidad ha sido cambiada a 'Celsius'
    --------------------------------------""")
            break    
        elif(opcion_unidad == "2"):
            unidad = "imperial"
            signoTemp = "°F"
            limpiar_consola()
            print("""
    -----------------------------------------
    La unidad ha sido cambiada a 'Fahrenheit'
    -----------------------------------------""")
            break
        else:
            limpiar_consola()
            print("""
    Opción inválida""")
    while(True):
        print("""
    [1] Cambiar unidad ⚙️
    [0] Volver al Menú 🚪
        """)
        reintentar = input("""
    >>""")
        if(reintentar == "0"):
            limpiar_consola()
            menu_inicio.menu_principal()
        elif(reintentar == "1"):
            limpiar_consola()
            cambiar_unidad()             
        else:
            limpiar_consola()
            print("""
    Opción inválida""")
            
def consulta_extendida():
    global unidad
    global signoTemp
    load_dotenv()
    APPID_EXT = os.getenv('APIKEY_EXT')
    CANTDIAS = "5"
    limpiar_consola()
    try:
        print(Back.CYAN + """
    + Ingrese la ciudad de la que desee consultar el clima extendido: 
              """)
        ciudad = input("""
    >>""")
        print() 
        ciudad = ciudad.lower()
        if not ciudad:
            raise ValueError("""
    No se ha ingresado ninguna ciudad.""")
        
        if ciudad.isdigit():
            raise ValueError("""
    El nombre de la ciudad no puede ser un número.""")
        
        r2 = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={APPID_EXT}&units={unidad}&lang=es')
        if r2.status_code == 200:
            dicc_consulta_ext = r2.json()
            pronostico_diario = {}
        
            for dia in dicc_consulta_ext['list']:
                fecha_hora = dia['dt_txt']
                fecha = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S").date()
                nombre_dia = dias_semana[fecha.strftime("%A")]
                temperatura = dia['main']['temp']
                temp_max = dia['main']['temp_max']
                temp_min = dia['main']['temp_min']
                descripcion = dia['weather'][0]['description']
                # Agrupar por fecha
                if fecha not in pronostico_diario:
                    pronostico_diario[fecha] = {
                        'nombre_dia' : nombre_dia,
                        'temperaturas': [],
                        'temp_max': temp_max,
                        'temp_min': temp_min,
                        'descripciones': []
                    }  
                else: 
                    pronostico_diario[fecha]['temp_max'] = max(pronostico_diario[fecha]['temp_max'], temp_max)
                    pronostico_diario[fecha]['temp_min'] = min(pronostico_diario[fecha]['temp_min'], temp_min)

                pronostico_diario[fecha]['temperaturas'].append(temperatura)
                pronostico_diario[fecha]['descripciones'].append(descripcion)
            
            limpiar_consola()

            print("############################################################")
            print()
            print(f"""{'':<5}El pronóstico extendido de {ciudad.capitalize()} es :""")
            print("""
     Día          Máx      Mín      Descripción
                                                """)
            
            contador_dias = 0
            for fecha, info in pronostico_diario.items():
                temp_max = info['temp_max']
                temp_min = info['temp_min']
                descripcion = info['descripciones'][0]
                nombre_dia = info['nombre_dia']
                #Ver si ponemos poder el dia //  
                #print(f"{col1:<20} {col2:<20} {col3:<20}")
                print(f"{'':<5}{nombre_dia:<12} {temp_max:>5.2f}{signoTemp:<3} {temp_min:>5.2f}{signoTemp:<3} {descripcion.capitalize():<15} {icono_clima(info['descripciones'][0]):<5} ")
                contador_dias += 1
                if contador_dias == 5:
                    break
            print()
            print("############################################################")
            reintento_ext()
        else:
            if r2.status_code == 404:
                print(f"""
    Error: No se encontró la ciudad '{ciudad}'.""") 
                reintento_ext()                 
            else:
                print(f"""
    Error: No se pudo realizar la consulta (Código de estado: {r2.status_code}).""")
                reintento_ext()
    except requests.exceptions.RequestException as e:
        print(f"""
    Error: Ocurrió un problema con la conexión. Detalles: {e}""")
        reintento_ext()
    except Exception as e:
        print(f"""
    Error inesperado: {e}""")
        reintento_ext()

def ver_historial():
    limpiar_consola()
    historial.seleccionar_ciudad(FILENAME)
    print()
    reintento_historial()

    
#   ZONA DE FUNCIONES GENRALES
def limpiar_consola():
   
    os.system('clear' if os.name == 'posix' else 'cls')

def icono_clima(descripcion):
    iconos = {
        "cielo claro": " ☀️",
        "algo de nubes": " 🌥️",
        "nubes dispersas": " ⛅",
        "nubes": " ☁️",
        "muy nuboso": "  ☁️☁️☁️",
        "lluvia ligera": " 🌦️",
        "lluvia": " 🌧️",
        "lluvia de gran intensidad": " 🌧️🌧️",
        "llovizna": " 🌦️",
        "tormenta": " 🌧️⚡",
        "nieve": " ❄️",
        "neblina": " 🌫️ ",
        "bruma": " 🌫️🌫️"
    }
    return iconos.get(descripcion, " 🌍")

#   ZONA DE REINTENTOS
def reintento():
    while(True):
        print("""
        Desea intentar de nuevo?
        
        [1] Si ✅
        [0] Salir al menu 🚪
              """)
        reintentar = input("""
    >>""")
        if(reintentar == "1"):
            limpiar_consola()
            consulta_clima()
        elif(reintentar == "0"):
            limpiar_consola()
            menu_inicio.menu_principal()              
        else:
            limpiar_consola()
            print("""
    Opción inválida""")

def reintento_ext():
    while(True):
        print("""
        Desea intentar de nuevo?
        
        [1] Si ✅
        [0] Salir al menu 🚪
                """)
        reintentar = input("""
    >>""")
        if(reintentar == "1"):
            limpiar_consola()
            consulta_extendida()
        elif(reintentar == "0"):
            limpiar_consola()
            menu_inicio.menu_principal()              
        else:
            limpiar_consola()
            print("""
    Opción inválida""")

def reintento_historial():
    while(True):
        print("""
        Desea intentar de nuevo?
        
        [1] Si ✅
        [0] Salir al menu 🚪
                """)
        reintentar = input("""
    >>""")
        if(reintentar == "1"):
            limpiar_consola()
            ver_historial()
        elif(reintentar == "0"):
            limpiar_consola()
            menu_inicio.menu_principal()              
        else:
            limpiar_consola()
            print("""
    Opción inválida""")
    
 