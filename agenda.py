# Importas el módulo 'os', que proporciona funciones para interactuar con el sistema operativo.
import os

# Definiste una constante 'CARPETA' que contiene el nombre del directorio que quieres crear.
CARPETA = 'contactos/'
EXTENSION = '.txt' #Extensión de archivos

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

    

    # Preguntar al usuario la acción a realizar
    while True:
        # Muestra el menu de opciones
        mostrar_menu()

        #Preguntar al usuario la acción a realizar
        opcion = input('Seleccione una opción: \r\n')
        try:
            opcion = int(opcion)
            # Ejecutar las opciones
            if opcion == 1:
                agregar_contacto()
            elif opcion == 2:
                editar_contacto()
            elif opcion == 3:
                mostrar_contactos()
            elif opcion == 4:
                buscar_contacto()
            elif opcion == 5:
                eliminar_contacto()
            elif opcion == 6:
                print("Saliendo de la aplicación.")
                break  # Salir del bucle while
            else:
                print('Opción no válida, intente de nuevo')
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para seleccionar una opción del menú.")  # Mensaje de error más descriptivo


def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n').lower()
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except FileNotFoundError:
        print('No existe ese contacto')
    # No es necesario reiniciar la aplicación

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n').lower()
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except FileNotFoundError:
        print('El archivo no existe')
    # No es necesario reiniciar la aplicación

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print('\r\n')
    # No es necesario reiniciar la aplicación

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n').lower()
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input('Agrega la nueva categoria: \r\n')

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar un mensaje de éxito
            print('\r\n Contacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')
    # No es necesario reiniciar la aplicación

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n').lower()
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Agrega el telefono:\r\n')
            categoria_contacto = input('Categoria Contacto:\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mostrar un mensaje de éxito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')
    # No es necesario reiniciar la aplicación

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    print('6) Salir de la aplicación')

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
    return os.path.isfile(CARPETA + nombre.lower() + EXTENSION)

# Finalmente, llamas a la función principal 'app' para iniciar tu aplicación.
app()