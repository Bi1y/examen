from openpyxl import Workbook
import pandas as pd
from autor_negocio import AutorNegocio

######################################
listado_autor = []
registros_autor = "listado_autor.xlsx"

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
    fecha_nacimiento = input('Ingrese fecha de nacimiento---> dd/mm/aa: ')
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
    negocio1.mostrar_autores_registrados()
    indice = int(input('Ingrese un valor numerico: ')) - 1
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    fecha_nacimiento = input('Ingrese fecha de nacimiento---> dd/mm/aa: ')
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

def reporte():
    negocio1.generar_reporte()
    
# def mostrar():
#     negocio1.mostrar_autores_registrados()
#endRegion

#Diccionario
opciones = {
    "1": registrar_autor,
    "2": obtener_autor,
    "3": editar_autor,
    "4": eliminar_autor,
    "5": reactivar_autor,
    "6": reporte
    ,"7": exit
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
    print("7. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
