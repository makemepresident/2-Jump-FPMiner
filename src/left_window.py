import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (1280, 800)

class left_window(BoxLayout):
    
    def doThing(self):
        print('henlo')

class left_window_app(App):
    
    def build(self):
        return left_window()

left_window_app().run()