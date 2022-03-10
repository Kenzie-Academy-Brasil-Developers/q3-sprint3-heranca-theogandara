# Desenvolva sua classe Recipiente aqui.

class Recipiente:
    def __init__(self, tamanho: float, conteudo: float, limpo: bool) -> None:
        self.tamanho = tamanho
        if tamanho < 0:
            self.tamanho = 0
        self.conteudo = conteudo
        self.limpo = True

    def esvaziar(self) -> None:
        self.conteudo = 0

    def esta_vazio(self) -> bool:
        if self.conteudo <= 0:
            return True
        else:
            return False

    def esta_limpo(self) -> bool:
        if self.limpo:
            return True
        else:
            return False

    def estado(self) -> str:
        if self.limpo:
            return "limpo"
        else:
            return "sujo"

    def sujar(self) -> None:
        self.limpo = False

    def __repr__(self) -> str:
        self.estado = "sujo"
        if self.limpo:
            self.estado = "limpo"

        return f"Um recipiente <{self.estado}> não especificado"

    def __str__(self) -> str:
        self.estado = "sujo"
        if self.limpo:
            self.estado = "limpo"

        return f"Um recipiente <{self.estado}> não especificado"
