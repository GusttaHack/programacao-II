# 1. Suponha que você está desenvolvendo um sistema de biblioteca. Crie a
# classe Livro com as seguintes características:
# ○ Atributos: titulo, autor, ano_publicacao.
# ○ Métodos: exibir_detalhes.

class livro():
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def exibir_detalhes(self):
        return self.titulo, self.autor, self.ano_publicacao

livro = livro("Harry potter","JJK","1997")

livro.exibir_detalhes()