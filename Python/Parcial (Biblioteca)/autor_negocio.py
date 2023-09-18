import pandas as pd
from openpyxl import Workbook
from autor import Autor
from datetime import datetime

class AutorNegocio():
    listado_autor = []
    registros_autor = "listado_autor.xlsx"
    
    def __init__(self):
        self.listado_autor = []
        self.registros_autor = "listado_autor.xlsx"
    
    def obtener_autor(self):
        df = pd.read_excel(self.registros_autor)
        listado_autor = []
        for index, row in df.iterrows():
            autor = Autor(row['ID_Persona'],row['COD_Persona'],row['ID_Autor'],row['Codigo_Autor'],row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'],row['Fecha_de_Nacimiento'],row['Pais'],row['Editorial'],row['Estado_Autor'])
            listado_autor.append(autor)
        return listado_autor
    
    def registrar_autor(self,_id_persona,_cod_persona,_id_autor,_codigo_autor,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_pais,_editorial,_estado_autor):
            print(f'{_id_persona},{_cod_persona},{_id_autor},{_codigo_autor},{_nombre},{_apellido_paterno},{_apellido_materno},{_fecha_nacimiento},{_codigo_autor}, {_pais},{_editorial},{_estado_autor}')
            self.listado_autor = self.obtener_autor()
            autor = Autor(_id_persona,_cod_persona,_id_autor,_codigo_autor,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_pais,_editorial,_estado_autor)
            self.listado_autor.append(autor)
            print(f'se agrego un autor : {len(self.listado_autor)}')
    
    def guardar_autor(self):
            print(f'listado de autor es: {len(self.listado_autor)}')
            if len(self.listado_autor) > 0:
                data =[]
                for autor in self.listado_autor:
                    data.append([autor.id_persona,autor.cod_persona,autor.id_autor,autor.cod_autor,autor.nombre,autor.apellido_paterno,autor.apellido_materno,autor.fecha_nacimiento,autor.pais,autor.editorial,autor.estado_autor])
                columnas = ['ID_Persona','COD_Persona','ID_Autor','Codigo_Autor','Nombre','Apellido_Paterno','Apellido_Materno','Fecha_de_Nacimiento','Pais','Editorial','Estado_Autor']
                df = pd.DataFrame(data, columns=columnas)
                df.to_excel(self.registros_autor, index=False, engine='openpyxl')
                return f'se registro correctamento los datos del autor'
            else:
                return f'se genero un error al registrar el autor'

    def editar_autor(self,_indice,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_pais,_editorial):
        df = pd.read_excel(self.registros_autor)
        #,_codigo_autor,_estado_autor
        df.loc[_indice, 'Nombre'] = _nombre
        df.loc[_indice, 'Apellido_Paterno'] = _apellido_paterno
        df.loc[_indice, 'Apellido_Materno'] = _apellido_materno
        df.loc[_indice, 'Fecha_Nacimiento'] = _fecha_nacimiento
        #df.loc[_indice, 'Codigo_Autor'] = _codigo_autor
        df.loc[_indice, 'Pais'] = _pais
        df.loc[_indice, 'Editorial'] = _editorial
        #df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def eliminar_autor(self,_indice,_estado_autor):
        df = pd.read_excel(self.registros_autor)
        df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def reactivar_autor(self,_indice,_estado_autor):
        df = pd.read_excel(self.registros_autor)
        df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def mostrar_autores_registrados(self):
        listado_autor = self.obtener_autor()
        if listado_autor:
            print("Autores registrados:")
            for i, autor in enumerate(listado_autor):
                print(f"{autor.id_autor}. {autor.nombre} --Apellidos: {autor.apellido_paterno + ' ' + autor.apellido_materno} --,Editorial: {autor.editorial}, Estado: {autor.estado_autor}")
        else:
            print("No hay Autores registrados.")
    
    def generar_reporte(self):
        print("Generando el Reporte de autor")
        lista_autor = self.obtener_autor()
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime("%d_%m_%Y")
        print("Fecha actual en formato 'día_mes_año':", formato)
        nom_reporte = 'reporte_autor'+ formato + '.txt'
        with open(nom_reporte, 'w') as archivo:
            archivo.write("*******Listado de Autores registrados en el Sistema*******************.\n")
            for autor in lista_autor:
                archivo.write(autor.imprimir())
            archivo.write("*************************************************.\n")