import dirt2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from View.ui import KV
import write


Builder.load_string(KV)


class MenuScreen(Screen):
    pass

class BaseScreen(Screen):
    handler = dirt2.Reader()
    handler.parser.setContentHandler(handler)
    handler.parser.parse("students.xml")

    information = {'full_name': [], 'group': [], 'valid_reason': [], 'invalid_reason': []}
    information['full_name'] = handler.student_full_name
    information['group'] = handler.student_group
    information['valid_reason'] = handler.student_valid_reason
    information['invalid_reason'] = handler.student_invalid_reason

    def base(self):
        print(len(self.information['full_name']))
        information_string = ''
        for name in range(len(self.information['full_name'])):
            information_string += f"{name + 1}) {self.information['full_name'][name]}" \
                                  f" {self.information['group'][name]} [ " \
                                  f"{str(self.information['valid_reason'][name])}, " \
                                  f"{str(self.information['invalid_reason'][name])} ] \n"
        print(self.information)
        return information_string

    def upd(self):
        self.ids['base_label_id'].text = BaseScreen.base(self)

        write.make_xml(self.information).writexml(open('new.xml','w',encoding='utf-8'),
                            indent="   ",
                            addindent="    ",
                            newl='\n'
                            )



class StudentsScreen(Screen):
    pass


class AddScreen(Screen):
    def add(self, full_name, group, valid_reason, invalid_reason):
        BaseScreen.information['full_name'].append(full_name)
        BaseScreen.information['group'].append(group)
        BaseScreen.information['valid_reason'].append(int(valid_reason))
        BaseScreen.information['invalid_reason'].append(int(invalid_reason))


class SearchScreen(Screen):
    found_string = ''

    def search(self, full_name, group, valid_reason, invalid_reason):
        list_of_index = []
        if full_name != '':
            list_of_index = [i for i in range(len(BaseScreen.information['full_name'])) if
                             full_name.lower() in BaseScreen.information['full_name'][i].lower()]
        elif group != '':
            list_of_index = [i for i in range(len(BaseScreen.information['group'])) if
                             group in BaseScreen.information['group'][i]]
        elif valid_reason != '':
            list_of_index = [i for i in range(len(BaseScreen.information['valid_reason'])) if
                             int(valid_reason) == BaseScreen.information['valid_reason'][i]]
        elif invalid_reason != '':
            list_of_index = [i for i in range(len(BaseScreen.information['invalid_reason'])) if
                             int(invalid_reason) == BaseScreen.information['invalid_reason'][i]]
        if (len(list_of_index) == 0):
            self.found_string = 'Matches have not been found!'
            return 'Matches have not been found!'
        else:
            self.found_string = ''.join([
                f"{BaseScreen.information['full_name'][index]} {BaseScreen.information['group'][index]} [{BaseScreen.information['valid_reason'][index]}, {BaseScreen.information['invalid_reason'][index]}] \n"
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
                self.deleted_string += f"{BaseScreen.information['full_name'][index]} {BaseScreen.information['group'][index]} [{BaseScreen.information['valid_reason'][index]}, {BaseScreen.information['invalid_reason'][index]}] \n"
                del BaseScreen.information['full_name'][index]
                del BaseScreen.information['group'][index]
                del BaseScreen.information['valid_reason'][index]
                del BaseScreen.information['invalid_reason'][index]

    def upd(self):
        self.ids['delete_label_id'].text = self.deleted_string


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

        return sm


if __name__ == '__main__':
    TestApp().run()
