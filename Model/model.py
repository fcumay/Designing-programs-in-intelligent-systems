import read
import write

import os.path
import math

class Model:
    curr_page=0
    information = {'full_name': [], 'group': [], 'valid_reason': [], 'invalid_reason': [], 'totall': []}
    def upload_file(self,file_name):
        if os.path.exists(file_name):
            handler = read.Reader()
            handler.parser.setContentHandler(handler)
            handler.parser.parse(file_name)

            self.information['full_name'] = handler.student_full_name
            self.information['group'] = handler.student_group
            self.information['valid_reason'] = [int(x) for x in handler.student_valid_reason]
            self.information['invalid_reason'] = [int(x) for x in handler.student_invalid_reason]
            self.information['totall'] = list(map(sum, zip(Model.information['valid_reason'], Model.information['invalid_reason'])))
            return True
        else:
            return False
    def save_file(self,file_name):
        write.make_xml(self.information).writexml(open(file_name, 'w', encoding='utf-8'),
                                                   indent="   ",
                                                   addindent="    ",
                                                   newl='\n'
                                                   )
    def update(self,navigation):
        if navigation == -1:
            self.curr_page -= 1
        elif navigation == 1:
            self.curr_page += 1
        return self.next_page(self)

    def next_page(self):
        number_of_strings = 10
        information = ''
        start = self.curr_page * number_of_strings
        for i in range(start, start + number_of_strings):
            if len(Model.information['full_name']) <= i:
                self.curr_page = -1
                break
            elif start < 0:
                self.curr_page = math.floor(len(Model.information['full_name']) / number_of_strings)
                break
            else:
                information += f"{i + 1}){Model.information['full_name'][i]} {Model.information['group'][i]} [{Model.information['valid_reason'][i]}, {Model.information['invalid_reason'][i]}] ({Model.information['totall'][i]}) \n"
        print(information)
        return information