from Persona import Persona
class Registro:
    
    def __init__(self, id_reg: int, Persona: Persona, estado: str = "Pendiente" ):
        self.id_reg = id_reg
        self.Persona = Persona 
        self.estado = "Pendiente"
        
        
    def confirmacion(self):
        self.confirmacion = "Confirmado"
        
    def Cancelacion(self):
        self.Cancelacion = "Cancelado"
        
    

        
