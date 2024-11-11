import os 
import sys
import funciones_clima
from colorama import Back


def menu_principal():

    while(True):
        print(Back.CYAN +"""

    ######## ☀️ APP DEL CLIMA ☀️ ########

    Opciones: 

    1- Consultar el clima ⛅
    2- Consultar el clima extendido 📅
    3- Ver el historial de consultas ❓
    4- Cambiar la unidad de medida ⚙️
    5- Salir 🚪
    

    ######################################""")
        print("""
    Ingrese una opcion:""")
        opcion = input("""
    >>""")
        if(opcion == "1"):
            funciones_clima.consulta_clima()
        elif(opcion == "2"):    
            funciones_clima.consulta_extendida()
        elif(opcion == "3"):
            funciones_clima.ver_historial()
        elif(opcion == "4"):    
            funciones_clima.cambiar_unidad()
        elif(opcion == "5"):
            sys.exit("""
    Finalizando
                     """)
        else:
            funciones_clima.limpiar_consola()
            print("""

    Numero invalido. Intente de nuevo
                  
                  """)
                                


    
