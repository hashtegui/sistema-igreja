from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.icon_definitions import md_icons
from src.view.pessoasview import CadastroPessoas

from kivy.lang.builder import Builder


class TelaInicial(MDScreen,):
   pass

CadastroPessoas()
