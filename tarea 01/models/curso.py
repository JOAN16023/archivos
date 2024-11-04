from config.db import connectToMySQL

class Cursos:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.id_colegio = data["id_colegio"]

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM cursos"
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
    def insert(cls, name):
        query = f"INSERT INTO curso (name) VALUES  ('{name}')"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result

    @classmethod
    def update(cls, id, name):
        query = f"UPDATE cursos SET name='{name}' WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result
    
    @classmethod
    def delete_one(cls, id):
        query = f"DELETE FROM cursos WHERE id={id}"
        result = connectToMySQL('sist_educativo').query_db(query)
        return result