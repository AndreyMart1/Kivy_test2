from kivy.app import App
from kivy.uix.button import Button
from kivy.extras.highlight import KivyLexer
from kivy.config import Config

Config.set('graphics','resizable','0')
Config.set('graphics','width','470')
Config.set('graphics','height','800')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window

class GetDataWooly(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return GetDataWooly()

MyApp().run()