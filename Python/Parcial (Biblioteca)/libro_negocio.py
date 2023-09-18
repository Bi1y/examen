import pandas as pd
from openpyxl import Workbook
from libro import Libro
from datetime import datetime

class LibroNegocio():
    listado_libros = []
    registros_libros = "listado_libros.xlsx"
    
    def __init__(self):
        self.listado_libros = []
        self.registros_libros = "listado_libros.xlsx"
    
    def obtener_libro(self):
        df = pd.read_excel(self.registros_libros)
        listado_libros = []
        for index, row in df.iterrows():
            libro = Libro(row['Indice'],row['Codigo_Libro'],row['Titulo'], row['Fecha_de_Publicacion'], row['Tomo'],row['Estado_Libro'])
            listado_libros.append(libro)
        return listado_libros
    
    def registrar_libro(self,_id_libro,_codigo_libro,_titulo,_anyo,_tomo,_estado_libro):
            print(f'{_id_libro},{_codigo_libro},{_titulo},{_anyo},{_tomo},{_estado_libro}')
            self.listado_libros = self.obtener_libro()
            libro = Libro(_id_libro,_codigo_libro,_titulo,_anyo,_tomo,_estado_libro)
            self.listado_libros.append(libro)
            print(f'se agrego un libro : {len(self.listado_libros)}')
    
    def guardar_libro(self):
            print(f'listado de libros es: {len(self.listado_libros)}')
            if len(self.listado_libros) > 0:
                data =[]
                for libro in self.listado_libros:
                    data.append([libro.id_libro,libro.codigo_libro,libro.titulo,libro.anyo,libro.tomo,libro.estado_libro])
                columnas = ['Indice','Codigo_Libro','Titulo','Fecha_de_Publicacion','Tomo','Estado_Libro']
                df = pd.DataFrame(data, columns=columnas)
                df.to_excel(self.registros_libros, index=False, engine='openpyxl')
                return f'se registro correctamento los datos del libro'
            else:
                return f'se genero un error al registrar el libro'

    def editar_libro(self,_id_libro,_codigo_libro,_titulo,_anyo,_tomo):
        df = pd.read_excel(self.registros_libros)
        #,_estado_libro
        df.loc[_id_libro, 'Titulo'] = _titulo
        df.loc[_id_libro,'Fecha_de_Publicacion'] = _anyo
        df.loc[_id_libro, 'Tomo'] = _tomo
        df.loc[_id_libro, 'Codigo_Libro'] = _codigo_libro
        #df.loc[_id_libro, 'Estado_libro'] = _estado_libro
        df.to_excel(self.registros_libros, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def eliminar_libro(self,_id_libro,_estado_libro):
        df = pd.read_excel(self.registros_libros)
        df.loc[_id_libro, 'Estado_Libro'] = _estado_libro
        df.to_excel(self.registros_libros, index=False, engine='openpyxl')
        return f'Eliminacion correcta'
    
    def reactivar_libro(self,_id_libro,_estado_libro):
        df = pd.read_excel(self.registros_libros)
        df.loc[_id_libro, 'Estado_Libro'] = _estado_libro
        df.to_excel(self.registros_libros, index=False, engine='openpyxl')
        return f'Actualización correcta'
    
    def mostrar_libros_registrados(self):
        listado_libros = self.obtener_libro()
        if listado_libros:
            print("Autores registrados:")
            for i, libro in enumerate(listado_libros):
                print(f"{libro.id_libro}., {libro.codigo_libro}, TITULO: {libro.titulo}, AÑO: {libro.anyo}, TOMO: {libro.tomo}, Estado: {libro.estado_libro}")
        else:
            print("No hay Categorias registradas.")
    
    def generar_reporte(self):
        print("Generando el Reporte de Libro")
        lista_libros = self.obtener_libro()
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime("%d_%m_%Y")
        print("Fecha actual en formato 'día_mes_año':", formato)
        nom_reporte = 'reporte_libros_'+ formato + '.txt'
        with open(nom_reporte, 'w') as archivo:
            archivo.write("*******Listado de Libros registrados en el Sistema*******************.\n")
            for libro in lista_libros:
                archivo.write(libro.imprimir())
            archivo.write("*************************************************.\n")