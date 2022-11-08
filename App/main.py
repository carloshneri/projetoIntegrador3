
import json
from kivymd.app import MDApp
from kivy.core.window import Window

from kivy.metrics import dp

from kivy.network.urlrequest import UrlRequest

from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import MDList,TwoLineListItem

# Layout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.scrollview import MDScrollView
#from kivy.properties import StringProperty

# Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from kivy_garden.mapview import MapMarkerPopup, MapView, MapMarker


class TelaInicial(MDScreen):
    def pesquisa_lista(self, municipio, medicamento):
        print(municipio.text)
        print(medicamento.text)
        #mainapp.tela.ids.municipio.text = municipio.text
        #mainapp.tela.ids.remedio.text = medicamento.text
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

            #self.tabela(resultado)
            self.lista_tabela(resultado)
        url = "http://sus-tem.herokuapp.com/medicamentos/"
        req = UrlRequest(url, got_json)

    def lista_tabela(self, resultado):
        self.lista_dados = MDList()
        for res in resultado:
            self.lista_dados.add_widget(TwoLineListItem(text = res[0] , secondary_text=res[1]))
        self.add_widget(MDScrollView(self.lista_dados))
        
class Mapa(MDScreen):
    def pressionado(self, widget):
        print("teste")

    def on_enter(self):
        self.marker = MapMarker()
        self.marker.lat = -23.66708
        self.marker.lon = -46.46421
        
        #file = open("App/ubs.json")
        #ubs = json.load(file)
        ubs = {"vila Assis":{"lat": -23.68371,"lon":-46.46304},
                "Parque São Vicente":{"lat":-23.66956, "lon":-46.47426},
                "Vila Margini":{"lat":-23.66148, "lon":-46.45978}

                }
        markers = []
        for i in ubs:
            i = MapMarker(lat=ubs[i]['lat'],lon=ubs[i]['lon'])
            markers.append(i)
        self.map = MapView()
        self.map.lat = -23.66708
        self.map.lon = -46.46421
        self.map.zoom = 15
        
        for marke in markers:
            self.map.add_marker(marke)

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

