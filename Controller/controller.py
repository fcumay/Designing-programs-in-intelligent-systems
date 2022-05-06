import write
from Model.model import Model


class Controller:

    def upload_file(self, file_name):
        if Model.file_name_validation(Model, file_name):
            Model.upload_file(Model, file_name)
        return Model.file_name_validation(Model, file_name)

    def save_file(self, file_name="new.xml"):
        Model.save_file(Model, file_name)

    def update(self, navigation):
        information = Model.update(Model, navigation)
        self.save_file(self)
        return information

    def add(self, full_name, group, valid_reason, invalid_reason):
        Model.add(Model, full_name, group, valid_reason, invalid_reason)

    def find(self, full_name, group, valid_reason, invalid_reason):
        list_of_index = Model.searching(Model, full_name, group, valid_reason, invalid_reason)
        return 'Matches have not been found!' if len(list_of_index) == 0 else Model.find(Model, list_of_index)
