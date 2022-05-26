import math
import os.path
from Controller.controller import Controller

from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 800)
Config.set("graphics", "height", 600)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from View.ui import KV

Builder.load_string(KV)


class FirstPage(Screen):
    def __init__(self, controller):
        super(FirstPage, self).__init__()
        self.controller = controller

    def new_game(self):
        self.controller.new_game()

    def continue_game(self):
        self.controller.continue_game()


class MainPage(Screen):
    def __init__(self, controller):
        super(MainPage, self).__init__(name='main')
        self.controller = controller

    def update(self):
        self.ids['train_goods'].text = f'={self.controller.update()[-1]}= Train: :  {self.controller.update()[-2]}'
        self.ids['st_A_goods'].text = f'Station A:  {self.controller.update()[0]}'
        self.ids['st_B_goods'].text = f'Station B:  {self.controller.update()[1]}'
        self.ids['st_C_goods'].text = f'Station C:  {self.controller.update()[2]}'
        self.ids['st_D_goods'].text = f'Station D:  {self.controller.update()[3]}'
        self.ids['st_E_goods'].text = f'Station E:  {self.controller.update()[4]}'
        self.ids['st_F_goods'].text = f'Station F:  {self.controller.update()[5]}'

    def next_station(self, station):
        if station != '':
            self.controller.next_station(int(station))
        self.update()

    def load(self, num):
        if num != '':
            self.controller.load(int(num))
        self.update()

    def unload(self, num):
        if num != '':
            self.controller.unload(int(num))
        self.update()


class TestApp(App):
    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    Window.clearcolor = (.45, .76, .76, 1)

    def build(self):
        self.title = "Thomas"
        sm = ScreenManager()

        sm.add_widget(FirstPage(self.controller))
        sm.add_widget(MainPage(self.controller))

        return sm
