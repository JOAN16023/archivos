from comida import Comida 

class Persona:
    def __init__(self):
        self.estado_animo = "Neutro"
        self.distancia = 0
        self.calorias = 0
        
    def correr(self, distancia):
        self.distancia += distancia
        if (distancia < 1000):
            self.estado_animo = "FELIZ"
        else:
            self.estado_animo = "CANSADO"
            
    def caminar(self, distancia):
        if (distancia < 1000):
            self.estado_animo = "NEUTRO"
            
        elif distancia < 5000:
            self.estado_animo = "conteto"
        
    
    def comer(self):
        self.calorias += comida.calorias 