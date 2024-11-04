from config.db import connectToMySQL

class Profesores:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.id_colegio = data["id_colegio"]

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM profesores"
        results = connectToMySQL('sist_educativo').query_db(query)
        profesores = []
        for profesor in results:
            profesores.append(cls(profesor))
        return profesores
        

    @classmethod
    def select_one(cls, id):
        query = f"SELECT * FROM profesores WHERE id = {id}"
        results = connectToMySQL('sist_educativo').query_db(query)
        profesores = []
        for profesor in results:
            profesores.append(cls(profesor))
        return profesores

    @classmethod
    def insert(cls, nombre, apellido):
        query = f"INSERT INTO profesores (nombre) VALUES  ('{nombre}')"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result

    @classmethod
    def update(cls, id, nombre, apellido):
        query = f"UPDATE profesores SET nombre='{nombre}', apellido='{apellido}' WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result
    
    @classmethod
    def delete_one(cls, id):
        query = f"DELETE FROM profesores WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result