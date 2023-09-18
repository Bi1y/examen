import pandas as pd
from openpyxl import Workbook
from libro_negocio import LibroNegocio
from autor_negocio import AutorNegocio
from categoria_negocio import CategoriaNegocio 
from completo import Completo


def menu_autor():
    #################################################################################
    listado_autor = []
    registros_autor = "Python\Parcial (Biblioteca)\listado_autor.xlsx"

    #RegionAutor
    negocio1 = AutorNegocio()

    def registrar_autor():
        lista_autor_temporal=negocio1.obtener_autor()
        print(len(lista_autor_temporal))
        id_persona = len(lista_autor_temporal)+1
        cod_persona = f"P00{len(lista_autor_temporal)+1}"
        id_autor = len(lista_autor_temporal)+1
        cod_autor = f"A00{len(lista_autor_temporal)+1}"
        nombre = input('Ingrese nombre: ')
        apellido_paterno = input('Ingrese ap_paterno: ')
        apellido_materno = input('Ingrese ap_materno: ')
        print('Ingrese fecha de nacimiento: ')
        dia = input('Ingresa el dia en el formato: dd --> ')
        mes = input('Ingrese el mes en el formato: MM --> ')
        anyo_temp = input('Ingrese el año en el formato: yyyy --> ')
        fecha_nacimiento = f'{dia}/{mes}/{anyo_temp}'
        pais = input('Ingrese pais: ')
        editorial = input('Ingrese la editorial a la que pertenece el autor: ')
        estado_autor = True
        negocio1.registrar_autor(id_persona,cod_persona,id_autor,cod_autor,nombre,apellido_paterno,apellido_materno,fecha_nacimiento,pais,editorial,estado_autor)
        negocio1.guardar_autor()
        print(f'registro correcto del autor')

    def obtener_autor():
        listado_autor = negocio1.obtener_autor()
        for autor in listado_autor:
            print(autor.imprimir())

    def editar_autor():
        indice = int(input('Ingrese un valor numerico: '))-1
        nombre = input('Ingrese nombre: ')
        ap_paterno = input('Ingrese ap_paterno: ')
        ap_materno = input('Ingrese ap_materno: ')
        print('Ingrese fecha de nacimiento: ')
        dia = input('Ingresa el dia en el formato: dd --> ')
        mes = input('Ingrese el mes en el formato: MM --> ')
        anyo_temp = input('Ingrese el año en el formato: yyyy --> ')
        fecha_nacimiento = f'{dia}/{mes}/{anyo_temp}'
        pais= input('Ingrese el pais:   ')
        editorial = input('Ingrese la editorial a la que pertenece el autor: ')
        print(negocio1.editar_autor(indice,nombre,ap_paterno, ap_materno,fecha_nacimiento,pais,editorial))

    def eliminar_autor():
        indice = int(input('Ingrese un valor numerico: ')) - 1
        estado_autor = False
        print(negocio1.eliminar_autor(indice,estado_autor))

    def reactivar_autor():
        indice = int(input('Ingrese un valor numerico: ')) - 1
        estado_autor = True
        print(negocio1.reactivar_autor(indice,estado_autor))

    def reporte_autor():
        negocio1.generar_reporte()
    #endRegion
    
    #DICCIONARIO DE AUTOR
    opciones = {
    "1": registrar_autor,
    "2": obtener_autor,
    "3": editar_autor,
    "4": eliminar_autor,
    "5": reactivar_autor,
    "6": reporte_autor,
    "7": menu_principal,
    "8": exit
    
    }

    while True:
        print("##########################")
        print("Menú:")
        print("1. Registrar Autor")
        print("2. Listar Autor")
        print("3. Editar Autor")
        print("4. Eliminar Autor")
        print("5. Reactivar Autor")
        print("6. Generar Reporte")
        print("7. Volver al menu principal")
        print("8. Salir")
        print("##########################")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion in opciones:
            opciones[seleccion]()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_libro():
    #############################################################################################################

    listado_libros=[]
    registros_libros = 'listado_libros.xlsx'

    #RegionLibros
    negocio2 = LibroNegocio()

    def registrar_libros():
        lista_libro_temporal= negocio2.obtener_libro()
        id_libro = len(lista_libro_temporal) + 1
        titulo = input('Ingrese titulo: ')
        codigo_libro = f"L00{len(lista_libro_temporal)+1}"
        print('Ingrese fecha de publicacion: ')
        dia = input('Ingresa el dia en el formato: dd --> ')
        mes = input('Ingrese el mes en el formato: MM --> ')
        anyo_temp = input('Ingrese el año en el formato: yyyy --> ')
        anyo = f'{dia}/{mes}/{anyo_temp}'
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
        id_libro = int(input('Ingrese id libro: '))-1
        titulo = input('Ingrese titulo: ')
        print('Ingrese fecha de publicacion: ')
        dia = input('Ingresa el dia en el formato: dd --> ')
        mes = input('Ingrese el mes en el formato: MM --> ')
        anyo_temp = input('Ingrese el año en el formato: yyyy --> ')
        anyo = f'{dia}/{mes}/{anyo_temp}'
        tomo = input('Ingrese tomo: ')
        print(negocio2.editar_libro(id_libro,titulo,anyo,tomo))

    def eliminar_libro():
        id_libro = int(input('Ingrese id del libro: ')) - 1
        estado_libro = False
        print(negocio2.eliminar_libro(id_libro,estado_libro))

    def reactivar_libro():
        id_libro = int(input('Ingrese id del libro inactivo: '))
        estado_libro = True
        print(negocio2.reactivar_libro(id_libro,estado_libro)) - 1

    def reporte_libro():
        negocio2.generar_reporte()
    #End Region
    
    #DICCIONARIO DE LIBRO
    opciones = {
    "1": registrar_libros,
    "2": obtener_libros,
    "3": editar_libro,
    "4": eliminar_libro,
    "5": reactivar_libro,
    "6": reporte_libro,
    "7": menu_principal,
    "8": exit
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
        print("7. Volver al menu principal")
        print("8. Salir")
        print("##########################")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion in opciones:
            opciones[seleccion]()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_categoria():
    #############################################################################################################

    listado_categorias = []
    registros_categorias = 'Python\Parcial (Biblioteca)\listado_categorias.xlsx'

    #RegionCategorias
    negocio = CategoriaNegocio()

    def registrar_categorias():
        lista_categoria_temporal=negocio.obtener_categorias()
        cod_categoria = f"C00{len(lista_categoria_temporal)+1}"
        categoria = input('Nombre de la categoría: ')
        estado_categoria = True
        negocio.registrar_categoria(cod_categoria, categoria, estado_categoria)
        negocio.guardar_categorias()
        print(f'Registro correctamente de la categoría')

    def obtener_categorias():
        listado_categorias = negocio.obtener_categorias()
        for categoria in listado_categorias:
            print(categoria.imprimir())

    def editar_categoria():
        indice = int(input('Ingrese un valor numerico: '))-1
        nueva_categoria = input('Ingrese nuevo nombre de la categoría: ')
        print(negocio.editar_categoria(indice, nueva_categoria))

    def eliminar_categoria():
        indice = int(input('Ingrese un valor numerico: ')) - 1
        estado_categoria = False
        print(negocio.eliminar_categoria(indice, estado_categoria))

    def reactivar_categoria():
        indice = int(input('Ingrese un valor numerico: ')) - 1
        estado_categoria = True
        print(negocio.reactivar_categoria(indice, estado_categoria))

    def reporte_categoria():
        negocio.generar_reporte()
    #endRegion
    #DICCIONARIO DE CATEGORIA
    opciones = {
    "1": registrar_categorias,
    "2": obtener_categorias,
    "3": editar_categoria,
    "4": eliminar_categoria,
    "5": reactivar_categoria,
    "6": reporte_categoria,
    "7": menu_principal,
    "8": exit
    }

    while True:
        print("##########################")
        print("Menú:")
        print("1. Registrar categorías")
        print("2. Listar categorías")
        print("3. Editar categoría")
        print("4. Eliminar categoría")
        print("5. Reactivar categoría")
        print("6. Generar Reporte")
        print("7. Volver al menu principal")
        print("8. Salir")
        print("##########################")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion in opciones:
            opciones[seleccion]()  
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_asignacion():
    ######################################################################################
    
    #RegionRegistrosCompletos
    completo = Completo()
    
    def asignacion():
        completo.asignacion_categoria_a_libro()

    def reporte():
        completo.generar_reporte_txt()

    def obtener():
        listado_completo = completo.obtener_registro_completo()
        for categoria in listado_completo:
            print(categoria)
    #EndRegion

    #DICCIONARIO
    opciones = {
        "1": asignacion,
        "2": reporte,
        "3": obtener,
        "4": exit
    }

    while True:
        print("##########################")
        print("Menú:")
        print("1. Asignacion")
        print("2. Generar Reporte")
        print("3. Obtener")
        print("4. Salir")
        print("##########################")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion in opciones:
            opciones[seleccion]()  
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_principal():
    #DICCIONARIO GENERAL
    opciones = {
        "1": menu_autor,
        "2": menu_libro,
        "3": menu_categoria,
        "4": menu_asignacion,
        "5": exit
        }

    while True:
            print("##########################")
            print("Menú:")
            print("1. Visualizar el menu de Autores")
            print("2. Visualizar el menu de Libros")
            print("3. Visualizar el menu de Categorias")
            print("4. Visualizar el menu de Asignacion")
            print("5. Salir")
            print("##########################")
            
            seleccion = input("Seleccione una opción: ")

            if seleccion in opciones:
                opciones[seleccion]()  
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

menu_principal()