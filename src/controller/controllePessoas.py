
from src.models.pessoas import Pessoa


class ControllerPessoas:
    def adiciona(self, nome, sobrenome, idade):
        pessoa = Pessoa(nome, sobrenome, idade)
