# Importas el módulo 'os', que proporciona funciones para interactuar con el sistema operativo.
import os

# Definiste una constante 'CARPETA' que contiene el nombre del directorio que quieres crear.
CARPETA = 'contactos/'

# Definiste la función principal de tu aplicación, llamada 'app'.
def app():
    # Dentro de esta función, llamas a otra función llamada 'crear_directorio'.
    crear_directorio()

    # Muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar

    preguntar =True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        #ejecutar las opciones
        if opcion == 1:
            print('Agregar contacto')
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    

# Aquí defines la función 'crear_directorio'.
def crear_directorio():
    # Usas 'os.path.exists' para verificar si el directorio especificado por 'CARPETA' ya existe.
    if not os.path.exists(CARPETA):
        # Si el directorio no existe, usas 'os.makedirs' para crearlo.
        os.makedirs(CARPETA)
    else:
        # Si el directorio ya existe, imprimes un mensaje informando al usuario.
        print('La carpeta ya existe')

# Finalmente, llamas a la función principal 'app' para iniciar tu aplicación.
app()
