from bs4 import BeautifulSoup##Importar Beatiful Soup
import requests 
from googlesearch import search
import re

def BuscarGoogle():
    # importar la funcion de busqueda
    from googlesearch import search
# esta variable contiene el paramentro o consulta de busqueda
    q = "palabras"
# ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta
    results = search(q)
# hacemos un recorrido de los resultados, cada resultado es una URL
    for r in results:
	    print(r)


url = "https://es.wikipedia.org/wiki/Coco_(película)"
req = requests.get(url)

status_code = req.status_code
if status_code == 200:
    html = BeautifulSoup(req.text, "html.parser")
    entradas = html.find_all('div',{'id': 'mw-content-text' })

    for i, entrada in enumerate(entradas):
        texto = entrada.getText()
        print(texto)
        text_file = open("Output.txt", "w",encoding="utf-8")

        text_file.write(texto)
    
        text_file.close()

else:
    print ("Status Code %d" % status_code)
