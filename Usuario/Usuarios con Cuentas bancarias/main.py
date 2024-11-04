class CuentaBancaria:
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés,
        self.balance = balance 
        
    def depósito(self, cantidad):
        self.balance += cantidad  
               
    def retiro(self, cantidad):
        if self.balance > cantidad:
            self.balance -= cantidad
        else:
            print("fondos insuficientes: cobrando una tarifa de $5") 
            self.balance -= 5 
            return self

    def mostrar_info_cuenta(self):
        print(f"tu cuenta tiene: {self.balance}")
        return self 

    def generar_interés(self):
       if self.balance > 0: 
           self.balance += self.balance * self.tasa_interés 
           return self
       
       
class Usuario:
    def __init__(self, nombre, ):
        self.nombre = nombre 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

persona = CuentaBancaria("Joan")
persona2 = CuentaBancaria("Matias")