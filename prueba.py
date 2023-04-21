import os
import json
import urllib.request
import subprocess

url = "10.220.85.126"
cmd="curl -s -k " + url
# Abrir la conexión y leer los datos
output = 0

while not output:
        result = subprocess.Popen(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = result.communicate() 
        print("esperando datos...")


# Verificar si se han recibido datos
data = json.loads(output)
print("Datos recibidos:", data)
