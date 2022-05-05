import read
import write

from Model.model import Model


class Controller:
    def upload(self, file_input="students.xml"):
        handler = read.Reader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse(file_input)

        Model.information['full_name'] = handler.student_full_name
        Model.information['group'] = handler.student_group
        Model.information['valid_reason'] = [int(x) for x in handler.student_valid_reason]
        Model.information['invalid_reason'] = [int(x) for x in handler.student_invalid_reason]

    def save(self, file_output="new.xml"):
        write.make_xml(Model.information).writexml(open(file_output, 'w', encoding='utf-8'),
                                                   indent="   ",
                                                   addindent="    ",
                                                   newl='\n'
                                                   )
