from config.db import connectToMySQL

class Alumnos:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.id_curso = data["id_curso"]

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM alumnos"
        results = connectToMySQL('sist_educativo').query_db(query)
        alumnos = []
        for alumno in results:
            alumnos.append(cls(alumno))
        return alumnos
        

    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM alumnos WHERE id = {id}"
        results = connectToMySQL('sist_educativo').query_db(query)
        alumnos = []
        for alumno in results:
            alumnos.append(cls(alumno))
        return alumnos

    @classmethod
    def insert(cls, nombre):
        query = f"INSERT INTO alumnos (nombre) VALUES  ('{nombre}')"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result

    @classmethod
    def update(cls, id, nombre, apellido):
        query = f"UPDATE alumnos SET nombre='{nombre}', apellido='{apellido}'  WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result
    
    @classmethod
    def delete_one(cls, id):
        query = f"DELETE FROM alumnos WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result
