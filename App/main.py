from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.network.urlrequest import UrlRequest
from plyer import gps

# UIX
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase, MDTabs


# Mapview
from kivy_garden.mapview import MapMarkerPopup, MapView, MapMarker


class TabMapa(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""

    pass


class TabResultado(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""

    pass


class TelaTab(MDScreen):
    municipio = ''
    medicamento =  ''
    
    
    def on_pre_enter(self):

        self.tabmapa = TabMapa()
        self.tabresultado = TabResultado()
        self.ids.tabs.add_widget(self.tabresultado)
        self.ids.tabs.add_widget(self.tabmapa)
        self.tabmapa.ids.telamapa.add_widget(Mapa())
        self.tabresultado.ids.telaresultado.add_widget(PesquisaLista())
        

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass

    def on_leave(self):
        self.ids.tabs.remove_widget(self.tabresultado)
        self.ids.tabs.remove_widget(self.tabmapa)

    

class TelaInicial(MDScreen):

    def pesquisa_lista(self, municipio, medicamento):
        mainapp.tela_tab.ids.municipio.text = municipio.text
        mainapp.tela_tab.ids.medicamento.text = medicamento.text
        mainapp.sm.current = "tela_tab"

    def abrir_mapa(self):
        mainapp.sm.current = "mapa"


class PesquisaLista(MDScreen):
    municipio = ""
    medicamento = ""
    def __init__(self, **kwargs,):
        super().__init__(**kwargs)
        
        self.municipio = mainapp.tela_tab.ids.municipio.text
        self.medicamento = mainapp.tela_tab.ids.medicamento.text
        
        def got_json(req, result):
            resultado = []
            
            for l in req.result:
                linha = (l["nome"], l["local"])
                resultado.append(linha)
            if len(resultado) == 0:
                resultado.append(("medicamento não encontrado", "VERIFIQUE O NOME DIGITADO"))
            self.lista_tabela(resultado)

        url = f"http://app-bucamedi.herokuapp.com/main/?nome__contains={self.medicamento}&local__contains={self.municipio}"
        
        # url = "http://sus-tem.herokuapp.com/medicamentos/"
        
        req = UrlRequest(url, got_json)

    def lista_tabela(self, resultado):
        self.lista_dados = MDList()
        for res in resultado:
            self.lista_dados.add_widget(
                TwoLineListItem(text=res[0], secondary_text=res[1])
            )
        self.add_widget(MDScrollView(self.lista_dados))


class Mapa(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.marker = MapMarker()
        self.marker.lat = -23.66708
        self.marker.lon = -46.46421
        ubs = {
            "vila Assis": {"lat": -23.68371, "lon": -46.46304},
            "Parque São Vicente": {"lat": -23.66956, "lon": -46.47426},
            "Vila Margini": {"lat": -23.66148, "lon": -46.45978},
        }
        markers = []
        for i in ubs:
            i = MapMarker(lat=ubs[i]["lat"], lon=ubs[i]["lon"])
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
        self.tela_tab=TelaTab(name="tela_tab")
        self.sm.add_widget(TelaInicial(name="telainicial"))
        self.sm.add_widget(self.tela_tab)
               
        return self.sm

'''
## parte de implementação para o GPS

    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start(minTime=1000, minDistance=1)

    def on_gps_location(self, **kwargs):
        kwargs['lat']=10.0
        kwargs['lon']=10.0
        print(kwargs)
'''        


if __name__ == "__main__":
    mainapp = MainApp()
    mainapp.run()
