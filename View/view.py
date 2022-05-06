import math
import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from View.ui import KV

from Model.model import Model
from Controller.controller import Controller

Builder.load_string(KV)


class MenuScreen(Screen):
    pass


class BaseScreen(Screen):
    def update(self,navigation=0):
        self.ids['base_label_id'].text = Controller.update(Controller,navigation)


class AddScreen(Screen):
    def add(self, full_name, group, valid_reason, invalid_reason):
        Model.information['full_name'].append(full_name)
        Model.information['group'].append(group)
        Model.information['valid_reason'].append(int(valid_reason))
        Model.information['invalid_reason'].append(int(invalid_reason))
        Model.information['totall'].append(int(valid_reason) + int(invalid_reason))

    def input_validation(self, full_name, group, valid_reason, invalid_reason):
        if full_name == '' or not full_name.replace(' ', '').isalpha():
            self.ids['full_name'].text = 'Invalid input!'
        elif group == '':
            self.ids['group'].text = 'Invalid input!'
        elif not valid_reason.isdigit() or valid_reason == '':
            self.ids['valid_reason'].text = 'Invalid input!'
        elif not invalid_reason.isdigit() or invalid_reason == '':
            self.ids['invalid_reason'].text = 'Invalid input!'
        else:
            self.add(full_name, group, valid_reason, invalid_reason)


class SearchScreen(Screen):
    found_string = ''

    def search(self, full_name, group, valid_reason, invalid_reason):
        list_of_index = []
        if full_name != '':
            list_of_index = [i for i in range(len(Model.information['full_name'])) if
                             full_name.lower() in Model.information['full_name'][i].lower()]
        elif group != '':
            list_of_index = [i for i in range(len(Model.information['group'])) if
                             group in Model.information['group'][i]]
        elif valid_reason != '':
            list_of_index = [i for i in range(len(Model.information['valid_reason'])) if
                             int(valid_reason) == Model.information['valid_reason'][i]]
        elif invalid_reason != '':
            list_of_index = [i for i in range(len(Model.information['invalid_reason'])) if
                             int(invalid_reason) == Model.information['invalid_reason'][i]]
        if (len(list_of_index) == 0):
            self.found_string = 'Matches have not been found!'
            return 'Matches have not been found!'
        else:
            self.found_string = ''.join([
                f"{Model.information['full_name'][index]} {Model.information['group'][index]} [{Model.information['valid_reason'][index]}, {Model.information['invalid_reason'][index]}] ({Model.information['totall'][index]}) \n"
                for index in list_of_index])
            return list_of_index

    def find(self, full_name, group, valid_reason, invalid_reason):
        self.search(full_name, group, valid_reason, invalid_reason)
        self.ids['search_label_id'].text = self.found_string


class DeleteScreen(Screen):
    deleted_string = ''

    def delete(self, full_name, group, valid_reason, invalid_reason):
        if SearchScreen.search(self, full_name, group, valid_reason, invalid_reason) == 'Matches have not been found!':
            self.deleted_string = 'Matches have not been found'
        else:
            self.deleted_string = ''
            for index in reversed(SearchScreen.search(self, full_name, group, valid_reason, invalid_reason)):
                self.deleted_string += f"{Model.information['full_name'][index]} {Model.information['group'][index]} [{Model.information['valid_reason'][index]}, {Model.information['invalid_reason'][index]}] ({Model.information['totall'][index]}) \n"
                del Model.information['full_name'][index]
                del Model.information['group'][index]
                del Model.information['valid_reason'][index]
                del Model.information['invalid_reason'][index]
                del Model.information['totall'][index]

    def upd(self):
        self.ids['delete_label_id'].text = self.deleted_string


class UploadScreen(Screen):
    def upload_file(self,file_name):
        if Controller.upload_file(Controller,file_name):
            self.manager.current = 'menu'
        else:
            self.ids['file'].text = 'No such file!'

class TestApp(App):
    Window.clearcolor = (.81, .77, .87, 1)

    def build(self):
        self.title = "Attendance"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(BaseScreen(name='base'))
        sm.add_widget(AddScreen(name='add'))
        sm.add_widget(SearchScreen(name='search'))
        sm.add_widget(DeleteScreen(name='delete'))
        sm.add_widget(UploadScreen(name='upload'))

        return sm
