import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import datetime
from categoria_negocio import CategoriaNegocio
from libro_negocio import LibroNegocio
from autor_negocio import AutorNegocio

class Completo():
    #listado_completo = []
    registros_completos = "listado_completo.xlsx"
    #data = []
    
    def __init__(self):
        self.listado_completo = []
        self.registros_completos = "listado_completo.xlsx"
        self.data = []
    
    def asignacion_categoria_a_libro(self):
        # Mostrar las listas 
        
        categoria_negocio = CategoriaNegocio()
        libro_negocio = LibroNegocio()
        autor_negocio = AutorNegocio()
        #guardar datos de los registros de excel en un arreglo
        lista_libro = libro_negocio.obtener_libro()
        lista_categoria = categoria_negocio.obtener_categorias()
        lista_autor = autor_negocio.obtener_autor()
        
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Lista de Autores")
        autor_negocio.mostrar_autores_registrados()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        
        
        indice_autor = int(input("Ingrese el indice del autor al que desea agregarle el libro: ")) - 1
        
        if 0<=indice_autor<len(lista_autor):
            autor = lista_autor[indice_autor]
            
            print("#############################")
            print("Lista de Libros")
            libro_negocio.mostrar_libros_registrados()
            print("#############################")
            
            indice_libro = int(input("Ingrese el indice del libro al que desea asignar categoria: ")) - 1
            
            if 0 <= indice_libro < len(lista_libro):
                libro = lista_libro[indice_libro]

                print("******************************")
                print("Lista de Categorias")
                categoria_negocio.mostrar_categorias_registradas()
                print("******************************")
                
                categorias_a_asignar = input("Ingrese los números de las categorias que desea asignar (separado por comas): ") 
                categorias_a_asignar = [int(i) for i in categorias_a_asignar.split(',')]
               
                for indice_categoria in categorias_a_asignar:
                    if 0<= indice_categoria - 1< len(lista_categoria):
                        categoria = lista_categoria[indice_categoria - 1]
                        
                        self.data.append([autor.id_autor,autor.cod_autor,libro.id_libro,libro.codigo_libro,categoria.cod_categoria,autor.nombre,autor.apellido_paterno,autor.apellido_materno,libro.titulo,categoria.categoria])
   
                    else:
                        print('Indice de categoria no valido')
                        
                columnas = ['ID_AUTOR','COD_AUTOR','ID_LIBRO', 'COD_LIBRO', 'COD_CATEGORIA','NOMBRE_AUTOR','APELLIDO_PATERNO','APELLIDO_MATERNO','TITULO','CATEGORIA']
                df = pd.DataFrame(self.data, columns=columnas)
                df.to_excel(self.registros_completos, index=False, engine='openpyxl')
                        
            else:
                print('Índice de libro no válido.')
        else:
            print('Indice de Autor no valido')
            
    def obtener_registro_completo(self):
            df = pd.read_excel(self.registros_completos)
            listado_completo = []
            for index, row in df.iterrows():
                completo = (row['ID_AUTOR'],row['COD_AUTOR'],row['ID_LIBRO'],row['COD_LIBRO'],row['COD_CATEGORIA'],row['NOMBRE_AUTOR'], row['APELLIDO_PATERNO'], row['APELLIDO_MATERNO'], row['TITULO'], row['CATEGORIA'])
                listado_completo.append(completo)
            return listado_completo
    
    def generar_reporte_txt(self):
        print("Generando el Reporte Completo")
        try:
            listado_completo = self.obtener_registro_completo()
            fecha_actual = datetime.now()
            formato = fecha_actual.strftime("%d_%m_%Y")
            print("Fecha actual en formato 'día_mes_año':", formato)
            nom_reporte = 'reporte_completo'+ formato + '.txt'
            if listado_completo:
                with open(nom_reporte, 'w') as archivo:
                    archivo.write("*******Listado de Autores registrados en el Sistema*******************.\n\n")
                    archivo.write("{:<15} {:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<20} {:<20} {:<20}\n".format(
                        "ID_AUTOR", "COD_AUTOR", "ID_LIBRO", "COD_LIBRO", "COD_CATEGORIA", "NOMBRE_AUTOR", "APELLIDO_PATERNO", "APELLIDO_MATERNO", "TITULO", "CATEGORIA"))
                    for completo in listado_completo:
                        archivo.write("{:<15} {:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<20} {:<20} {:<20}\n".format(*completo))
                    archivo.write("*************************************************.\n")
                print("Reporte generado exitosamente en", nom_reporte)
            else:
                    print("No hay datos para generar el reporte.")
        except Exception as e:
            print("Error al generar el reporte:", str(e))