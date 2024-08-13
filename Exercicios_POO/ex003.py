# 3. Desenvolva um sistema de estoque que possui a Classe produtos com as
# seguintes características:
# ○ Atributos: nome, preco, quantidade e codigo.
# ○ Métodos: calcular_total, atualizar_preco e verificar_disponibilidade.

class produtos:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo
    
    def calcular_total(self):
        valor = self.preco * self.quantidade
        print(f"O valor total do produto {self.nome} é: {valor}")
    
    def atualizar_preco(self):
        print(f"O {self.nome} custa {self.preco}")
        valor = float(input("Quanto você quer que custe? "))
        self.preco = valor
        print(f"O valor atual do produto {self.nome} é: {self.preco}")
    
    def verificar_disponibilidade(self):
        print(f"tem {self.quantidade} unidades de {self.nome} disponíveis")

estoque = produtos("Whey protein",120,32,"001")

estoque.verificar_disponibilidade()