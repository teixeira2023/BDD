# A calculadora
class Calculadora:
    def __init__(self):
        self.resultado = 0

    def somar(self, a, b):
        self.resultado = a + b
    
    def subtrair(self, x, y):
        self.resultado = x - y

    def obter_resultado(self):
        return self.resultado
