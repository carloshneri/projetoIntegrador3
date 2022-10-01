from kivymd.app import MDApp
from kivy.metrics import dp


from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
#Layout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

#Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen


class Gerenciador(MDScreenManager):
    pass


class Tela(MDFloatLayout):
    pass


class MainApp(MDApp):
    pass



MainApp().run()