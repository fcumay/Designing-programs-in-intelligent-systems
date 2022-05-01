import read
import write

class Model():
    information = {'full_name': [], 'group': [], 'valid_reason': [], 'invalid_reason': []}

    def __init__(self, file_input="students.xml", file_output="new.xml"):
        self.file_input = file_input
        self.file_output = file_output


    def upload(self):
        handler = read.Reader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse(self.file_input)

        self.information['full_name'] = handler.student_full_name
        self.information['group'] = handler.student_group
        self.information['valid_reason'] = handler.student_valid_reason
        self.information['invalid_reason'] = handler.student_invalid_reason

    def save(self):
        write.make_xml(self.information).writexml(open(self.file_output, 'w', encoding='utf-8'),
                                                  indent="   ",
                                                  addindent="    ",
                                                  newl='\n'
                                                  )
