from config.db import connectToMySQL

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
        result = connectToMySQL('sist_educativo').query_db(query)
        return result

    @classmethod
    def update(cls, id, nombre):
        query = f"UPDATE colegios SET nombre='{nombre}' WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result

    @classmethod
    def delete_one(cls, id):
        query = f"DELETE FROM colegios WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result