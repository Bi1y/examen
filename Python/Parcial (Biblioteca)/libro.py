class Libro():
    id_libro = 0
    codigo_libro = ""
    titulo = ""
    anyo = ""
    tomo = ""
    indice = ""
    estado_libro = False
    Categoria = []
    
    def __init__(self, id_libro, codigo_libro, titulo, anyo, tomo,estado_libro):
        self.id_libro = id_libro
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.anyo = anyo
        self.tomo = tomo
        self.estado_libro = estado_libro

    def get_id_libro(self):
        return self.id_libro
    
    def set_id_libro(self, id_libro):
        self.id_libro = id_libro
    
    def get_codigo_libro(self):
        return self.codigo_libro
    
    def set_codigo_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro
    
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    def get_anyo(self):
        return self.anyo
    
    def set_anyo(self, anyo):
        self.anyo = anyo
    
    def get_tomo(self):
        return self.anyo
    
    def set_anyo(self, tomo):
        self.tomo = tomo
    
    def get_estado_libro(self):
        return self.estado_libro
    
    def set_estado_libro(self, estado_libro):
        self.estado_libro = estado_libro
    
    def asignar_genero(self, categorias):
        self.Categoria.append(categorias)
        
    def imprimir(self):
        codigo = self.codigo_libro
        titulo = self.titulo
        anyo = self.anyo
        tomo = self.tomo
        
        return f'{codigo=}, titulo del libro: {titulo}, Año de publicacion: {anyo}, Tomo: {tomo}\n'