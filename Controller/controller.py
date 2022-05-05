import write

from Model.model import Model


class Controller:

    def save(self, file_output="new.xml"):
        write.make_xml(Model.information).writexml(open(file_output, 'w', encoding='utf-8'),
                                                   indent="   ",
                                                   addindent="    ",
                                                   newl='\n'
                                                   )
    def upload_file(self,file_name):
        return(Model.upload_file(self,file_name))

