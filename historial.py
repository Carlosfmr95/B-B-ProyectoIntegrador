import json
import os
from datetime import datetime, timedelta
import menu_inicio

def guardar_consulta(diccionario_clima, FILENAME):
    try:
        with open(FILENAME, "r") as file:
            historial = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []


    ciudad_encontrada = False
    for entrada in historial:
        if entrada['name'] == diccionario_clima['name']:
            entrada['consultas'].append(diccionario_clima)
            ciudad_encontrada = True
            if len(entrada['consultas']) > 5:
                entrada['consultas'] = entrada['consultas'][-5:]
            break


    if not ciudad_encontrada:
        historial.append({
            'name': diccionario_clima['name'],
            'consultas': [diccionario_clima]
        })


    with open(FILENAME, "w") as file:
        json.dump(historial, file, indent=4)


def seleccionar_ciudad(FILENAME):
    limpiar_consola()
    leer_historial_filtrado(FILENAME)
    try:
        print("""
    ----------------------------------------------------------
    Seleccione el número de la ciudad que desea consultar: """)
        seleccion = int(input("""
    >>>""")) - 1
        with open(FILENAME, "r") as file:
            historial = json.load(file)
            if 0 <= seleccion < len(historial):
                consulta = historial[seleccion]
                limpiar_consola()
                print(f"""
    Ciudad seleccionada: {consulta['name']}""")
                print("---------------------------------------------")
                for i, c in enumerate(consulta['consultas']):
                    print(f""" 
    Consulta {i+1}:
            
    Temperatura mínima: {c['main']['temp_min']}
    Temperatura máxima: {c['main']['temp_max']}
    Descripción:        {c['weather'][0]['description'].capitalize()}{icono_clima(c['weather'][0]['description'])}
    Fecha:              {c['fecha']}
                            """)
                    print("---------------------------------------------")
            else:
                limpiar_consola()
                print("""
    Selección inválida.""")
                reintento_seleccion(FILENAME)
    except (ValueError, IndexError):
        limpiar_consola()
        print("""
    Entrada inválida.""")
        reintento_seleccion(FILENAME)
 



def leer_historial_filtrado(FILENAME, dias=5):
    try:
        with open(FILENAME, "r") as file:
            historial = json.load(file)
            print("""\n
    Historial de las últimas 5 ciudades consultadas:
    ----------------------------------------------------------""")
            for i, consulta in enumerate(historial):
                print(f"""
    {i+1}.  Ciudad: {consulta['name']}
        Consultado por última vez: {consulta['consultas'][-1]['fecha']}
                            """)
    except (FileNotFoundError, json.JSONDecodeError):
        print("""
    No hay historial de consultas.""")

        
# -----------------------------------------------------------------------------------
def reintento_seleccion(FILENAME):
    while(True):
        print("""
        Desea intentar de nuevo?
        
        [1] Si ✅
        [0] Salir al menu 🚪
              """)
        reintentar = input("    >> ")
        if(reintentar == "1"):
            limpiar_consola()
            seleccionar_ciudad(FILENAME)
        elif(reintentar == "0"):
            limpiar_consola()
            menu_inicio.menu_principal()              
        else:
            limpiar_consola()
            print("""
    Opción inválida""")

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