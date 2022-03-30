from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.icon_definitions import md_icons
from src.controller.controllePessoas import ControllerPessoas
from src.view.pessoasview import CadastroPessoas

from kivy.lang.builder import Builder


class TelaInicial(MDScreen,):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.con = ControllerPessoas()

    def on_enter(self):
        pass

    def listar(self):
        lista = self.con.lista()



CadastroPessoas()
