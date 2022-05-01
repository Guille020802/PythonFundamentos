import requests
import zipfile
import os
import shutil


url = 'https://www.sunat.gob.pe/descargaPRR/padron_reducido_local_anexo.zip'
response = requests.get(url)


nombre_archivo= 'file.zip'
with open(nombre_archivo, 'wb') as f:
    f.write(response.content)

# 2. descomprimir archivo
with zipfile.ZipFile(nombre_archivo, mode='r') as zip:
    zip.extractall()
    
# 3. copiar txt
if not os.path.isdir('./data'):
    # si no existe carpeta la genero
    os.mkdir('./data')

# muevo archivos txt
for file in os.listdir():
    if file.split('.')[-1]=='txt':
        shutil.move(file, './data')

    
# 3. elimino zip
os.remove(nombre_archivo)