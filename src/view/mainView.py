from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.icon_definitions import md_icons
from src.controller.controllePessoas import ControllerPessoas
from src.view.pessoasview import CadastroPessoas

from kivy.lang.builder import Builder


class TelaInicial(MDScreen,):
   def __init__(self, **kw):
       super().__init__(**kw)
       self.con = ControllerPessoas()
       
   def listar(self):
      lista = self.con.lista()
      print(lista)


CadastroPessoas()
