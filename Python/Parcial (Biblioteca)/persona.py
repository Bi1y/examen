class Persona:
    id_persona = 0
    cod_persona = ""
    nombre = ""
    apellido_paterno = ""
    apellido_materno = ""
    fecha_nacimiento = ""

    # constructor
    def __init__(self, id_persona,cod_persona,nombre, apellido_paterno, apellido_materno,fecha_nacimiento):
        self.cod_persona = cod_persona
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
    
    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona

    def get_cod_persona(self):
        return self.cod_persona
    
    def set_cod_persona(self, cod_persona):
        self.cod_persona = cod_persona
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_apellido_paterno(self):
        return self.apellido_paterno
    
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    
    def imprimir(self):
        id_persona = self.id_persona
        codigo = self.cod_persona
        nombres = self.nombre
        apellidos = self.apellido_paterno + ' ' + self.apellido_materno
        fecha_nacimiento = self.fecha_nacimiento
        return f' {id_persona=},{codigo=}, {nombres=},  {apellidos=}, {fecha_nacimiento=}'