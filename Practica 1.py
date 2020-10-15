import requests
import json
import re
url = 'https://www.virustotal.com/vtapi/v2/file/scan'


params = {'apikey': '8dc1146093be4a3c8ab45441c6d7af66b75fd8d6bcd83d493d9628d2bbbb7377'}
direccion ="c:\\Users\\juced\\Documents\\LSTI\\Laboratorio de Programacion\\test.txt"
files = {'file': ("text.txt", open(direccion, 'rb'))}

response = requests.post(url, files=files, params=params)

result=response.json()
a = (result['md5'])
print (a)

url1 = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey': '8dc1146093be4a3c8ab45441c6d7af66b75fd8d6bcd83d493d9628d2bbbb7377', 'resource':a }

response = requests.get(url1, params=params)
print (response.json())

