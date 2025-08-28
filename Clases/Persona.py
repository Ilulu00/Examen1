class Persona:
    
    def __init__(self, nombre: str, apellido: str, direccion: str, correo:str, contraseña:str): #Constructor de la clase persona
        self.nombre = nombre
        self.apellido = apellido
        self.nombre = direccion
        self._correo = correo
        self._contraseña = contraseña
    
    def autenticador(self, correo: str, contraseña: str):
        return self.correo == correo and self._contraseña == contraseña #Verifica si el correo y la contraseña que digito el usuario es la que ingreso, la correcta