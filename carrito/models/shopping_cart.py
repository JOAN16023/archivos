from config.db import connectToMySQL
from models.product import Producto

class ShoppingCart:
    def __init__(self, data):
        self.id = data["id"]
        self.prod_id = data["prod_id"]
        self.user_id = data["user_id"]
        self.cant = data["cant"]
        self.product = None

    @classmethod
    def get_element(cls, user_id, prod_id):
        query = f"SELECT * FROM shopping_cart WHERE user_id={user_id} AND prod_id={prod_id}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            productos.append(cls(producto))
        return productos

    @classmethod
    def insert(cls, user_id, prod_id):
        query = f"INSERT INTO shopping_cart (user_id, prod_id, cant) VALUES ({user_id},{prod_id}, 1)"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result

    @classmethod
    def select_all(cls, user_id):
        query = f"""
            SELECT * FROM shopping_cart 
            LEFT JOIN products 
            ON shopping_cart.prod_id=products.id 
            WHERE user_id={user_id}"""
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            tmp = cls(producto)
            tmp.product = Producto(producto)
            productos.append(tmp)
        return productos

    @classmethod
    def update_cant(cls, cant, id):
        query = f"UPDATE shopping_cart SET cant={cant} WHERE id={id}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result

    @classmethod
    def delete_cart(cls, user_id):
        query = f"DELETE FROM shopping_cart WHERE user_id={user_id}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result