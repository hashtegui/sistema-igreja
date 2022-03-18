from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from kivy.lang.builder import Builder


KV = Builder.load_file('./kv_files/tela_principal.kv')


class TelaInicial(MDScreen):
    def build(self):
        return KV

class Program(MDApp):
    def build(self):
        return TelaInicial()

if __name__ == '__main__':
    
    Program().run()
