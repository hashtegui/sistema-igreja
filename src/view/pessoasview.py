from datetime import datetime
import re
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from src.models.pessoas import Pessoa
from src.controller.controllePessoas import ControllerPessoas


class CadastroPessoas(MDScreen):

    dialog = MDDialog

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data: datetime.strftime = '1'
        self.nome: str = None
        self.sobrenome: str = None
        self.con = ControllerPessoas()

    def on_save(self, instancia: MDDatePicker, valor: datetime, date_range):
        print(valor)
        data_formatada = valor.strftime('%d/%m/%Y')
        self.ids.dt_nascimento.text = data_formatada
        self.data = data_formatada
        print(self.data)

    def on_cancel(self, instancia: MDDatePicker, valor: datetime):
        pass

    def adiciona(self, nome: str, sobrenome: str, dt_nascimento: str):
        try:
            self.nome = nome
            self.sobrenome = sobrenome
            print(dt_nascimento)
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
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


class TextFieldData(MDTextField):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_text(self, instance, value):
        print(value)
