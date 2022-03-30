from kivymd.app import MDApp
from src.view.mainView import Builder


class Program(MDApp):
    
    def build(self):
#        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('./src/view/kv/tela_principal.kv')

if __name__ == '__main__':
    
    Program().run()
