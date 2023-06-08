import re
from os import path
from os import listdir
from sys import argv
from getpass import getuser

# Comprobamos si el numero de parametros es correcto
if len(argv) != 2:
    print("Use example: pycolor theme.json")
    exit(1)
# Ruta de qtile
directory_path = "/home/" + getuser() + "/.config/qtile"
# Comprobamos si el tema existe
if argv[1] not in listdir(path.join(directory_path, "themes")):
    print("El tema no existe")
    exit(1)
# Ruta del archivo de configuración de qtile
file_name = "config.py"
file_path = path.join(directory_path, file_name)
try:
    # Abrimos el archivo
    with open(file_path, "r") as file:
        contenido = file.read()
    # Buscamos el .json de los temas y lo sustituimos
    pattern = r'([\w\-]+\.json)'
    contenido_modificado = re.sub(pattern, argv[1], contenido)
    with open(file_path, "w") as archivo:
        archivo.write(contenido_modificado)
except Exception as e:
    print(str(e))
