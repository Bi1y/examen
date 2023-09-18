from persona import Persona

class Autor(Persona):
    id_autor = 0
    cod_autor = ""
    pais = ""
    editorial = ""
    estado_autor = False
    Libro = []

    def __init__(self, id_persona,cod_persona,id_autor,cod_autor,nombre, apellido_paterno, apellido_materno,fecha_nacimiento,pais,editorial,estado_autor):
        super().__init__(id_persona,cod_persona,nombre,apellido_paterno, apellido_materno,fecha_nacimiento)
        self.cod_autor = cod_autor
        self.id_autor = id_autor
        self.pais = pais
        self.editorial = editorial
        self.estado_autor = estado_autor
    
    def get_id_autor(self):
        return self.id_autor
    
    def set_id_autor(self, id_autor):
        self.id_autor = id_autor
    
    def get_cod_autor(self):
        return self.cod_autor
    
    def set_cod_autor(self, cod_autor):
        self.cod_autor = cod_autor
    
    def get_pais(self):
        return self.pais
    
    def set_pais(self, pais):
        self.pais = pais
    
    def get_editorial(self):
        return self.editorial
    
    def set_editorial(self, editorial):
        self.editorial = editorial
    
    def get_estado_autor(self):
        return self.estado_autor
    
    def set_estado_autor(self, estado_autor):
        self.estado_autor = estado_autor
    
    def agregar_libro(self, libros):
        self.Libro.append(libros)
        
    def imprimir(self):
        super_data = super().imprimir()
        id_autor = self.id_autor
        codigo = self.cod_autor
        pais= self.pais
        editorial = self.editorial
        return f'Datos del autor: {super_data}, ID: {id_autor},el codigo del autor es: {codigo}, {pais=}, la editorial es: {editorial}\n'
    
    