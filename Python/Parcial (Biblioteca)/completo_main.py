import pandas as pd
from openpyxl import Workbook
from completo import Completo


completo = Completo()

def asignacion():
    completo.asignacion_categoria_a_libro()

def reporte():
    completo.generar_reporte_txt()

def obtener():
    listado_completo = completo.obtener_registro_completo()
    for categoria in listado_completo:
        print(categoria)
    

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