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

persona = CuentaBancaria("Joan")
persona2 = CuentaBancaria("Matias")

persona.depósito(100), persona.depósito(200), persona.depósito(300), persona.retiro(450)
persona2.depósito(200), persona2.depósito(3000), persona2.retiro(300),persona2.retiro(400),persona2.retiro(100),persona2.retiro(300), persona2.generar_interés(5) 