import pandas as pd
from openpyxl import Workbook
from libro_negocio import LibroNegocio

##########################
listado_libros=[]
registros_libros = 'listado_libros.xlsx'
#Region
negocio2 = LibroNegocio()

def registrar_libros():
    lista_libro_temporal= negocio2.obtener_libro()
    id_libro = len(lista_libro_temporal) + 1
    titulo = input('Ingrese titulo: ')
    codigo_libro = f"B00{len(lista_libro_temporal)+1}"
    anyo = int(input('Ingrese fecha de publicacion: '))
    tomo = input('Ingrese tomo: ')
    estado_libro = True
    negocio2.registrar_libro(id_libro, codigo_libro,titulo,anyo,tomo,estado_libro)
    negocio2.guardar_libro()
    print(f'registro correctamente de los libros')

def obtener_libros():
    listado_libros = negocio2.obtener_libro()
    for libro in listado_libros:
        print(libro.imprimir())

def editar_libro():
    negocio2.mostrar_libros_registrados()
    id_libro = int(input('Ingrese el indice del libro a editar: '))-1
    titulo = input('Ingrese titulo: ')
    anyo = int(input('Ingrese fecha de publicacion: '))
    tomo = input('Ingrese tomo: ')
    codigo_libro = input('Ingrese codigo del libro: ')
    #estado_libro = True
    #,estado_libro
    print(negocio2.editar_libro(id_libro,codigo_libro,titulo,anyo,tomo))

def eliminar_libro():
    id_libro = int(input('Ingrese el indice del libro: ')) - 1
    estado_libro = False
    print(negocio2.eliminar_libro(id_libro,estado_libro))

def reactivar_libro():
    id_libro = int(input('Ingrese el indice del libro inactivo: ')) - 1
    estado_libro = True
    print(negocio2.reactivar_libro(id_libro,estado_libro))

def reporte():
    negocio2.generar_reporte()

# def mostrar():
#     negocio2.mostrar_libros_registrados()
#End Region

##diccionario
opciones = {
    "1": registrar_libros,
    "2": obtener_libros,
    "3": editar_libro,
    "4": eliminar_libro,
    "5": reactivar_libro,
    "6": reporte
    ,"7": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar libros")
    print("2. Listar libros")
    print("3. Editar libros")
    print("4. Eliminar libro")
    print("5. Reactivar libro")
    print("6. Generar Reporte")
    print("7. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
