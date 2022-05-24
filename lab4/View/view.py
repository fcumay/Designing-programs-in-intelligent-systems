import math
import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from View.ui import KV


Builder.load_string(KV)


class MenuScreen(Screen):
    pass

class TestApp(App):
    Window.clearcolor = (.45, .76, .76, 1)

    def build(self):
        self.title = "Attendance"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))

        return sm
