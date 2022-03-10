# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente


class Copo(Recipiente):
    def __init__(self, tamanho: float, conteudo: float, limpo: bool):
        super().__init__(self, tamanho, conteudo, limpo)
        self.tamanho = tamanho

    def encher(self, bebida: str = "água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        else:
            self.sujar()
            self.conteudo += self.tamanho
            self.bebida = bebida
        
    def beber(self, quantidade):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self) -> str:
        if self.conteudo <= 0:
            return f"Um copo vazio de <{self.tamanho}>ml"
        else:
            return f"Um copo de <{self.tamanho}>ml contendo <{self.conteudo}>ml de <{self.bebida}>"

    def __str__(self) -> str:
        if self.conteudo <= 0:
            return f"Um copo vazio de <{self.tamanho}>ml"
        else:
            return f"Um copo de <{self.tamanho}>ml contendo <{self.conteudo}>ml de <{self.bebida}>"
