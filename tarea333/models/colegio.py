from config.db import connectToMySQL

#colegio
class Colegios:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM colegios"
        results = connectToMySQL('sist_educativo').query_db(query)
        colegios = []
        for colegio in results:
            colegios.append(cls(colegio))
        return colegios
        
    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM colegios WHERE id = {id}"
        results = connectToMySQL('sist_educativo').query_db(query)
        colegios = []
        for colegio in results:
            colegios.append(cls(colegio))
        return colegios

    @classmethod
    def insert(cls, nombre):
        query = f"INSERT INTO colegios (nombre) VALUES  ('{nombre}')"
        results = connectToMySQL('sist_educativo').query_db(query)
        return results

#curso
class Cursos:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"] 
        self.id_colegio = data["id_colegio"] 
    
    @classmethod 
    def select_all(cls):
        query = f"SELECT * FROM cursos"
        results = connectToMySQL('sist_educativo').query_db(query)
        cursos = []
        for curso in results:
            cursos.append(cls(curso))
        return cursos
    
    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM cursos WHERE id = {id}"
        results = connectToMySQL('sist_educativo').query_db(query)
        cursos = []
        for curso in results:
            cursos.append(cls(curso))
        return cursos
          
    @classmethod
    def insert(cls, nombre, id_colegio):
        query = f"INSERT INTO cursos ('nombre', id_colegio) VALUES ('{nombre}', {id_colegio})"
        results = connectToMySQL('sist_educativo').query_db(query)
        return results
        
#PROFESORES

class Profesores:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.id_colegio = data["id_colegio"]
        
    @classmethod
    def select_all(cls):
        query = f"SELECT * FROM Profesores"
        results =  connectToMySQL('sist_educativo').query_db(query)
        profesores = []
        for profesore in results:
            profesores.append(cls(profesore))
        return profesores
        
    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM Profesores WHERE id = {id}"
        results =  connectToMySQL('sist_educativo').query_db(query)
        profesores = []
        for profesore in results:
            profesores.append(cls(profesore))
        return profesores
        
    @classmethod
    def insert(cls, nombre, apellido, id_colegio):
        query = f"INSERT INTO Profesores (nombre, apellido, id_colegio) VALUES ('{nombre}', '{apellido}', {id_colegio})"
        results =  connectToMySQL('sist_educativo').query_db(query)
        return results
        
#ALUMNOS
class Alumnos:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"] 
        self.id_curso = data["id_curso"]     
        
    @classmethod
    def select_all(cls):
        query = f"SELECT * FROM Alumnos"  
        results =  connectToMySQL('sist_educativo').query_db(query)
        alumnos = []
        for alumno in results:
            alumnos.append(cls(alumno))
        return alumnos

    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM Alumnos WHERE id = {id}"
        results =  connectToMySQL('sist_educativo').query_db(query)
        alumnos = []
        for alumno in results:
            alumnos.append(cls(alumno))
        return alumnos
          
    @classmethod
    def insert(cls, nombre, apellido, id_curso):
        query = f"INSERT INTO cursos (nombre, apellido, id_curso) VALUES  ('{nombre}', '{apellido}' {id_curso})"
        results =  connectToMySQL('sist_educativo').query_db(query)
        return results