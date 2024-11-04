from config.db import connectToMySQL

#colegios
class Colegios:
    def __init__(self, data):
        self.id_colegio = data["id_colegio"]
        self.nombre = data["nombre"]
        
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM colegios"
        
    @classmethod
    def insert(cls, nombre, id_colegio):
        query = f"INSERT INTO colegios (nombre, id_colegio) VALUES  ('{nombre}', {id_colegio})"    
        
#CURSOS   
class Cursos:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre = data["nombre"] 
        self.id_colegio = data["id_colegio"] 
    
    @classmethod 
    def select_all(cls):
        query = f"SELECT * FROM cursos"
    
    @classmethod
    def select_one(cls, id_curso):
        query = f"SELECT * FROM cursos WHERE id = {id_curso}"
          
    @classmethod
    def insert(cls, nombre, id_colegio):
        query = f"INSERT INTO cursos (nombre, id_colegio) VALUES  ('{nombre}', {id_colegio})"
        
#ALUMNOS
class Alumnos:
    def __init__(self, data):
        self.idalumnos = data["idalumnos"]
        self.nombre = data["nombre"]
        self.rut = data["rut"] 
        self.edad = data["edad"] 
        self.id_curso = data["id_curso"]     
        
    @classmethod
    def select_all(cls):
        query = f"SELECT * FROM alumnos"  

    @classmethod
    def select_one(cls, idalumnos):
        query = f"SELECT * FROM alumnos WHERE id = {idalumnos}"
          
    @classmethod
    def insert(cls, nombre, rut, edad, id_curso):
        query = f"INSERT INTO alumnos (nombre, apellido, id_curso) VALUES  ('{nombre}', {rut}, {edad}, {id_curso})"
        
        
#PROFESORES

class Profesores:
    def __init__(self, data):
        self.id_profesores = data["id_profesores"]
        self.nombre = data["nombre"]
        self.rut = data["rut"]
        self.colegio_idcolegio = data["colegio_idcolegio"]
        
    @classmethod
    def select_all(cls):
        query = f"SELECT * FROM profesores"
        
    @classmethod
    def select_one(cls, id_profesores):
        query = f"SELECT * FROM profesores WHERE id = {id_profesores}"
        
    @classmethod
    def insert(cls, nombre, rut, colegio_idcolegio):
        query = f"INSERT INTO profesores (nombre, apellido, id_colegio) VALUES ('{nombre}', '{rut}', {colegio_idcolegio})"


#MATERIAS
class Materias:
    def __init__(self, data):
        self.id_materias = data["id_materias"]
        self.nombre = data["nombre"]
        self.notas = data["notas"]
        
    @classmethod
    def select_all(cls):
        query = f"SELECT * FROM materias"  

    @classmethod
    def select_one(cls, id_materias):
        query = f"SELECT * FROM materias WHERE id = {id_materias}"
        
    @classmethod
    def insert(cls, nombre, notas):
        query = f"INSERT INTO materias (nombre) VALUES ('{nombre}', {notas})"