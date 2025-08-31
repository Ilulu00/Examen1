class Descuento:
    
    def descuentos(totalPagar: float) -> float: #Función para aplicar descuentos al momento de pagar
        if(totalPagar > 200000 and totalPagar <= 600000): #Descuenta el 20%
            reduccion = totalPagar*0.1
            totalPagar = totalPagar - reduccion
            return totalPagar
    
        elif(totalPagar > 50000 and totalPagar <= 200000): #Descuenta el 15%
            reduccion = totalPagar*0.05
            totalPagar = totalPagar - reduccion
            return totalPagar
    
        else:
            return totalPagar #Como no aplica ningún descuento retorna el valor original
    
    totalPagar_str:str = input("Ingrese total a pagar: ")
    totalPagar:float = float(totalPagar_str)
    resultado = descuentos(totalPagar)
   