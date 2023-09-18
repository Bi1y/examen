import pandas as pd
from openpyxl import Workbook
from categoria import Categoria
from datetime import datetime

class CategoriaNegocio():
    listado_categoria = []
    registros_categoria = "listado_categorias.xlsx"
    
    def __init__(self):
        self.listado_categoria = []
        self.registros_categoria = "listado_categorias.xlsx"
    
    def obtener_categorias(self):
        df = pd.read_excel(self.registros_categoria)
        listado_categoria = []
        for index, row in df.iterrows():
            categoria = Categoria(row['Cod_Categoria'], row['Categoria'], row['Estado_Categoria'])
            listado_categoria.append(categoria)
        return listado_categoria
    
    def registrar_categoria(self,_cod_categoria,_categoria,_estado_categoria):
        print(f'{_cod_categoria},{_categoria},{_estado_categoria}')
        self.listado_categoria = self.obtener_categorias()
        nueva_categoria = Categoria(_cod_categoria,_categoria,_estado_categoria)
        self.listado_categoria.append(nueva_categoria)
        print(f'se agrego una categoria : {len(self.listado_categoria)}')
  
    def guardar_categorias(self):
        if len(self.listado_categoria) > 0:
            data = []
            for categoria in self.listado_categoria:
                data.append([categoria.cod_categoria, categoria.categoria, categoria.estado_categoria])
            columnas = ['Cod_Categoria', 'Categoria', 'Estado_Categoria']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_categoria, index=False, engine='openpyxl')
            return 'Se registraron correctamente las categorías.'
        else:
            return 'Se generó un error al registrar las categorías.'

    def editar_categoria(self, _indice,_categoria):
        df = pd.read_excel(self.registros_categoria)
        df.loc[_indice, 'Categoria'] = _categoria
        df.to_excel(self.registros_categoria, index=False, engine='openpyxl')
        return 'Actualización correcta'

    def eliminar_categoria(self,_indice,estado_categoria):
        df = pd.read_excel(self.registros_categoria)
        df.loc[_indice, 'Estado_Categoria'] = estado_categoria
        df.to_excel(self.registros_categoria, index=False, engine='openpyxl')
        return 'Eliminacion correcta'

    def reactivar_categoria(self,_indice,estado_categoria):
        df = pd.read_excel(self.registros_categoria)
        df.loc[_indice, 'Estado_Categoria'] = estado_categoria
        df.to_excel(self.registros_categoria, index=False, engine='openpyxl')
        return 'Actualización correcta'
    
    def mostrar_categorias_registradas(self):
        listado_categorias = self.obtener_categorias()
        if listado_categorias:
            print("Autores registrados:")
            for i, categoria in enumerate(listado_categorias):
                print(f"{i+1}., {categoria.cod_categoria}, Categoria: {categoria.categoria}, Estado: {categoria.estado_categoria}")
        else:
            print("No hay Categorias registradas.")

    def generar_reporte(self):
        print("Generando el Reporte de categoria")
        lista_categoria = self.obtener_categorias()
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime("%d_%m_%Y")
        print("Fecha actual en formato 'día_mes_año':", formato)
        nom_reporte = 'reporte_'+ formato + '.txt'
        with open(nom_reporte, 'w') as archivo:
            archivo.write("*******Listado de categoria registrados en el Sistema*******************.\n")
            for categoria in lista_categoria:
                archivo.write(categoria.imprimir())
            archivo.write("*************************************************.\n")