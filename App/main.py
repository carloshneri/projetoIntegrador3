
from kivymd.app import MDApp


from kivy.metrics import dp

from kivy.network.urlrequest import UrlRequest

from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
#Layout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

#Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen




class TelaInicial(MDScreen):
    def pesquisa_lista(self,municipio, medicamento):
        print(municipio.text)
        print(medicamento.text)
        mainapp.tela.ids.municipio.text = municipio.text
        mainapp.tela.ids.remedio.text = medicamento.text
    
        mainapp.sm.current = 'tela'
        

  
class Tela(MDScreen):
    municipio = ''
    remedio =''
    
    def on_enter(self):
        self.municipio = mainapp.tela.ids.municipio.text
        self.remedio = mainapp.tela.ids.remedio.text
        def got_json(req, result):
            resultado = []
            for l in req.result:
                linha = (l["nome"], l["local"])
                resultado.append(linha)
                
            self.tabela(resultado)

        url = "http://sus-tem.herokuapp.com/medicamentos/"
        req = UrlRequest(url, got_json)
        

    def tabela(self, resultado):
        self.data_table = MDDataTable(
            use_pagination=False,
            column_data=[(self.municipio, dp(60)), (self.remedio, dp(90))],
            row_data=resultado,
            rows_num=len(resultado),
        )
        
        self.add_widget(self.data_table)
        mainapp.tela.ids.spinner.active = False
   
       



     
class MainApp(MDApp):
    def build(self):
        self.sm = MDScreenManager()
        self.telainicial = TelaInicial()
        self.tela = Tela()
        self.sm.add_widget(TelaInicial(name='telainicial'))
        self.sm.add_widget(Tela(name='tela'))

        return self.sm


if __name__ =='__main__':
    mainapp = MainApp()
    mainapp.run()