# Importas el módulo 'os', que proporciona funciones para interactuar con el sistema operativo.
import os

# Definiste una constante 'CARPETA' que contiene el nombre del directorio que quieres crear.
CARPETA = 'contactos/'
EXTENCION = '.txt' #Extencion de archivos

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

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
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
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

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    #Revizar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        print('Puedes editar')
    else:
        print('Ese contacto no existe')
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')

    #Revizar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENCION, 'w') as archivo:
            
            #resto de los campos
            telefono_contacto = input('Agrega el telefono:\r\n')
            categoria_contacto = input('Categoria Contacto:\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Mostrar un mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')
    
    else:
      print('Ese contacto ya existe')

    #Reiniciar la app
    app()

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


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENCION)
# Finalmente, llamas a la función principal 'app' para iniciar tu aplicación.
app()
