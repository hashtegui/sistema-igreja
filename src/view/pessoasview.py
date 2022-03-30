from datetime import datetime
import re
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from src.models.pessoas import Pessoa
from src.controller.controllePessoas import ControllerPessoas


class CadastroPessoas(MDScreen):

    dialog = MDDialog

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data: datetime.strftime = ''
        self.nome: str = None
        self.sobrenome: str = None
        self.con = ControllerPessoas()
    #tratar data
    def on_save(self, instancia: MDDatePicker, valor: datetime, date_range):
        print(valor)
        data_formatada = valor.strftime('%d/%m/%Y')
        self.ids.dt_nascimento.text = data_formatada
        self.data = data_formatada

    # def on_cancel(self, instacia, valor,):
    #     pass
    def adiciona(self, nome: str, sobrenome: str, dt_nascimento: str):
        try:
            self.nome = nome
            self.sobrenome = sobrenome
            # self.data = dt_nascimento
            pessoa = Pessoa(self.nome, self.sobrenome, self.data, 'F')
            self.con.adiciona(pessoa)
        except ValueError as er:
            print(er)

    def show_date(self):
        date_dialog = MDDatePicker(
            min_year=1950,
            max_year=int(datetime.today().year) + 1
        )
        date_dialog.bind(on_save=self.on_save,)
        date_dialog.open()


class TextFieldData(MDTextField):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ListarPessoas(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.list = ControllerPessoas().lista()


    def on_enter(self, *args):
        for item in self.list[1]:
            self.ids.container.add_widget(
                OneLineListItem(text=f'{item}')
            )
