

class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
        self.respuestas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def agregar_respuestas(self, listado_respuestas):
        self.respuestas.append(listado_respuestas)

    def mostrar(self):
        info = f"Encuesta: {self.nombre}\n"
        for preg in self.preguntas:
            info += preg.mostrar() + "\n"
        return info

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_min, edad_max):
        super().__init__(nombre)
        self.edad_min = edad_min
        self.edad_max = edad_max

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones_permitidas):
        super().__init__(nombre)
        self.regiones_permitidas = regiones_permitidas
