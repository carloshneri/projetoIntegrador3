from kivymd.app import MDApp


from kivy.metrics import dp

from kivy.network.urlrequest import UrlRequest

from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable

# Layout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
#from kivy.properties import StringProperty

# Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from kivy_garden.mapview import MapMarkerPopup, MapView, MapMarker


class TelaInicial(MDScreen):
    def pesquisa_lista(self, municipio, medicamento):
        #print(municipio.text)
        #print(medicamento.text)
        mainapp.tela.ids.municipio.text = municipio.text
        mainapp.tela.ids.remedio.text = medicamento.text
        mainapp.sm.current = "tela"

    def abrir_mapa(self):
        
        mainapp.sm.current = "mapa"


class Tela(MDScreen):
    municipio = ""
    remedio = ""

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
            column_data=[("Remedio", dp(40)), ("posto", dp(50))],
            row_data=resultado,
            rows_num=len(resultado),
        )
        mainapp.tela.ids.spinner.active = False
        self.add_widget(self.data_table)
        

class Mapa(MDScreen):

    def on_enter(self):
        self.map = MapView()
        self.map.lat = -23.66708
        self.map.lon = -46.46421
        self.map.zoom = 15
        self.marker = MapMarker()
        self.marker.lat = -23.66708
        self.marker.lon = -46.46421
        self.map.add_marker(self.marker)

        self.add_widget(self.map)
        


class MainApp(MDApp):
    def build(self):
        self.sm = MDScreenManager()
        self.telainicial = TelaInicial()
        self.tela = Tela()
        self.mapa = Mapa()
        self.sm.add_widget(TelaInicial(name="telainicial"))
        self.sm.add_widget(Tela(name="tela"))
        self.sm.add_widget(Mapa(name="mapa"))

        return self.sm


if __name__ == "__main__":
    mainapp = MainApp()
    mainapp.run()

