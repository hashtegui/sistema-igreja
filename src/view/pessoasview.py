from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker


class CadastroPessoas(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = ''
        
    def oi(self):
        print('oi')
        
    def on_save(self, instancia, valor, date_range):
        self.data =  valor
        print(instancia, type(valor), date_range)
    
    def on_cancel(self, instancia, valor):
        pass
    
    def show_date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        
