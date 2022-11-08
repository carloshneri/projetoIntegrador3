import json
from kivy_garden.mapview import MapMarkerPopup, MapView, MapMarker


class Marcadores(MapMarker):
    def __init__(self,nome, lat, lon):
        self.nome = nome
        self.lat = lat
        self.lon = lon


file = open("App/ubs.json")
ubs = json.load(file)
lista = []
for i in ubs:
    lista.append(i)
    print(i.nome)
    print('latitude'+ str(i.lat))
    print('longitude'+ str(i.lon))

print(lista[0])


