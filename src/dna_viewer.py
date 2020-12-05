import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel

class dna_viewer(App):
    def __init__(self):
        pass

    def build(self):
        main_layout = BoxLayout()

        main_layout.add_widget(control_panel())

class control_panel(Widget):
    def __init__(self):
        tab_panel = TabbedPanel()

