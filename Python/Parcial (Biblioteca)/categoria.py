class Categoria():
    cod_categoria = ""
    categoria = ""
    estado_categoria =  False
    
    def __init__(self, cod_categoria, categoria,estado_categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria
        self.estado_categoria = estado_categoria
    
    def get_cod_categoria(self):
        return self.cod_categoria
    
    def set_cod_categoria(self, cod_categoria):
        self.cod_categoria = cod_categoria
    
    def get_categoria(self):
        return self.categoria
    
    def set_categoria(self, categoria):
        self.categoria = categoria
        
    def get_estado_categoria(self):
        return self.estado_categoria
    
    def set_estado_categoria(self, estado_categoria):
        self.estado_categoria = estado_categoria
    
    def imprimir(self):
        codigo = self.cod_categoria
        categoria = self.categoria
        return f'CODIGO: {codigo}, CATEGORIA: {categoria}\n'