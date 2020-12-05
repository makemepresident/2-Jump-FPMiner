import kivy
kivy.require('2.0.0')

import TwoJump

from TwoJump import TwoJump

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserController
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

class PatternSearchWidget(BoxLayout):
    text_input = ObjectProperty(None)
    data_text = StringProperty('ACGTCTGAG')

    def search_string(self):
        two_jump = TwoJump(self.data_text.text)
        results = two_jump.match_pattern(self.text_input.text)
        for i in results:
            print(str(i))



Builder.load_file('PatternSearchWidget.kv')
     
class DnaViewer(App):

    def build(self):
        main_layout = PatternSearchWidget()

        return main_layout