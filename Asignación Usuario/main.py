class Usuario:
    def __init__(self, usuario, hacer_deposito, hacer_retiro, mostrar_balance_usuario):
        self.usuario = usuario
        self.hacer_deposito = hacer_deposito
        self.hacer_retiro = hacer_retiro
        self.mostrar_balance_usuario = mostrar_balance_usuario

user1 = Usuario("adrien", 1000, -300, 700)
print(user1.usuario)

user2 = Usuario("vicente", 2000, -1000, 1000)
print(user2.usuario)




user3 = Usuario("papita", 10500, -4500, 6000)
print(user3)
