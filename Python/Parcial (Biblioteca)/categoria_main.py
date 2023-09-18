import pandas as pd
from openpyxl import Workbook
from categoria_negocio import CategoriaNegocio 

listado_categorias = []
registros_categorias = 'listado_categorias.xlsx'

negocio3 = CategoriaNegocio()

def registrar_categorias():
    lista_categoria_temporal = negocio3.obtener_categorias()
    cod_categoria = f"C00{len(lista_categoria_temporal)+1}"
    categoria = input('Nombre de la categoría: ')
    estado_categoria = True
    negocio3.registrar_categoria(cod_categoria, categoria, estado_categoria)
    negocio3.guardar_categorias()
    print(f'Registro correctamente de la categoría')

def obtener_categorias():
    listado_categorias = negocio3.obtener_categorias()
    for categoria in listado_categorias:
        print(categoria.imprimir())

def editar_categoria():
    negocio3.mostrar_categorias_registradas()
    indice = int(input('Ingrese un valor numerico: ')) - 1
    nueva_categoria = input('Ingrese nuevo nombre de la categoría: ')
    print(negocio3.editar_categoria(indice, nueva_categoria))

def eliminar_categoria():
    indice = int(input('Ingrese un valor numerico: ')) - 1
    estado_categoria = False
    print(negocio3.eliminar_categoria(indice, estado_categoria))

def reactivar_categoria():
    indice = int(input('Ingrese un valor numerico: ')) - 1
    estado_categoria = True
    print(negocio3.reactivar_categoria(indice, estado_categoria))

# def mostrar():
#     negocio.mostrar_categorias_registradas()
def reporte():
    negocio3.generar_reporte()

opciones = {
    "1": registrar_categorias,
    "2": obtener_categorias,
    "3": editar_categoria,
    "4": eliminar_categoria,
    "5": reactivar_categoria,
    "6": reporte
    ,"7": exit
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
    print("7. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()  
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
