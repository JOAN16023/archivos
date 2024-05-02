class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = 0
        
        
    def hacer_deposito(self, cantidad):
        self.balance_cuenta += cantidad
        
        
    def hacer_retiro(self, cantidad):     
        self.balance_cuenta -= cantidad 
        
        
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, balance: ${self.balance_cuenta}")
        
        
    def transferir_dinero(self, otro_usuario, cantidad):
        self.balance_cuenta -= cantidad
        otro_usuario.balance_cuenta += cantidad

#crear usuarios 
persona1 = Usuario("Joan", "joan.tapia@gmail.com")  
persona2 = Usuario("Benjamin", "benjamin.ramirez@gmail.com")  

#hacer deposito y hacer retiro
persona1.hacer_deposito(100)      
print(persona1.balance_cuenta)

persona1.hacer_retiro(50)
print(persona1.balance_cuenta)

#tranferir

persona1.transferir_dinero(persona2, 50)

persona1.mostrar_balance_usuario()
persona2.mostrar_balance_usuario()