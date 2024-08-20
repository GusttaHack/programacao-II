class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            return "Erro: Não é possível dividir por zero!"
        else:
            return a / b
        
    def potenciacao(self, a, b):
        return a ** b
    
    def raiz_quadrada(self, a):
        if a < 0:
            return "Erro: Não é possível calcular a raiz quadrada de um número negativo!"
        else:
            return a ** (1/2)
