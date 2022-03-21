import datetime


class Pessoa():
    def __init__(self, nome: str, sobrenome: str, data_nascimento: datetime, sexo: str) -> None:
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__data_nascimento: datetime = data_nascimento
        self.__sexo: str = sexo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome: str) -> None:
        self.__sobrenome = sobrenome

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: datetime) -> None:
        self.__data_nascimento = data_nascimento
        
    @property
    def sexo(self):
        return self.__sexo
