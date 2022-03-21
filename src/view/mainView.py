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

    async def on_enter(self):
        for i in await self.con.lista():
            self.ids.container.add_widget(
                OneLineListItem(
                    text=str(i),
                    secondary_text=str(i)

                )
            )

    def listar(self):
        lista = self.con.lista()
        self.atualiza()
        print(lista)


CadastroPessoas()
