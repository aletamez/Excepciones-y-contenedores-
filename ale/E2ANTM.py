import requests
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
import os
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
import sys
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
from bs4 import BeautifulSoup as bs
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
import webbrowser
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
# Lo que se hace en este codigo es buscar noticias sobre la facultad que ingresas al poner sus siglas y tambien te pide poner desde que pagina quieres buscar,
# cuando pones la pagina inicial y la final te pide las siglas de la facultad y lo que hace es buscar en la pagina de la uanl y te abre automaticamente
# las paginas que se encontaron en la red de la uanl 
