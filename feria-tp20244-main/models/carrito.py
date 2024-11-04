from config.db import connectToMySQL
from models.productos import Productos

class Carrito_builer:
    def __init__(self, data):
        self.idcarrito = data["idcarrito"]
        self.cantidad =data["cantidad"]
        self.usuario_idusuario = data["usuario_idusuario"]
        self.productos_idproductos = data["productos_idproductos"]
        
