from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen



class Gerenciador(ScreenManager):
    pass

class MenuSuperior(FloatLayout):
    pass


class TelaEntrada(Screen):
    pass

class Pesquisa(Screen):
    pass


class MainApp(App):
    gerenciador = Gerenciador()
    def build(self):
        self.gerenciador.add_widget(TelaEntrada(name='TelaEntrada'))
        self.gerenciador.add_widget(Pesquisa(name='Pesquisa'))
        return self.gerenciador

MainApp().run()