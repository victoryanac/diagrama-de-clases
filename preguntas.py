

class Pregunta:
    def __init__(self, enunciado, requerida, ayuda=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = []

    def agregar_alternativa(self, alternativa):
        self.alternativas.append(alternativa)

    def mostrar(self):
        ayuda = f", Ayuda: {self.ayuda}" if self.ayuda else ""
        preg_info = f"Enunciado: {self.enunciado}{ayuda}\nAlternativas:\n"
        for alt in self.alternativas:
            preg_info += alt.mostrar() + "\n"
        return preg_info
