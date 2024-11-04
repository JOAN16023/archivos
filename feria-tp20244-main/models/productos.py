from config.db import connectToMySQL
from models.

class Productos:
    def __init__(self, data):
        self.idproductos = data["idproductos"]
        self.nombre = data["nombre"]
        self.precios = data["precios"]