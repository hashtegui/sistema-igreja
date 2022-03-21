
from src.models.pessoas import Pessoa


class ControllerPessoas:
    lista_Pessoas: list = []
    
    lista_Pessoas.append(1)
    lista_Pessoas.append(2)

    def adiciona(self, pessoa: Pessoa):
        self.lista_Pessoas.append(pessoa)

    def lista(self):
        return [..., self.lista_Pessoas]
