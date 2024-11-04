from config.db import connectToMySQL

class Producto:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.price = data["price"]


    @classmethod
    def select_all(cls):
        query = "SELECT * FROM products"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            productos.append(cls(producto))
        return productos