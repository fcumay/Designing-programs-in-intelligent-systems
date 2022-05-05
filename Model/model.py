import read
import write
import os.path

class Model:
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