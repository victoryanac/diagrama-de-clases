

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas
