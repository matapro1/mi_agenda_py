# Importamos el módulo 'os' que nos permite interactuar con el sistema operativo
import os

CARPETA = 'contactos/'

# Definimos la función principal de nuestra aplicación
def app():
    # Llamamos a la función 'crear_directorio'
    crear_directorio()

# Definimos la función 'crear_directorio'
def crear_directorio():
     # Usas 'os.path.exists' para verificar si el directorio 'contactos/' ya existe.
    if not os.path.exists(CARPETA):
     # Si el directorio no existe, usas 'os.makedirs' para crearlo.
        os.makedirs(CARPETA)
    else:
        print('La  carpeta ya existe')
# Finalmente, llamas a la función principal 'app' para iniciar tu aplicación.
app()