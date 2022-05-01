import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.student_full_name = []
        self.student_group = []
        self.student_valid_reason=[]
        self.student_invalid_reason = []
        self.parser = xml.sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == "students":
            pass

    def characters(self, content):
        if self.current == 'student_full_name':
            self.name = content
        elif self.current == "student_group":
            self.group = content
        elif self.current == "student_valid_reason":
            self.reason = content
        elif self.current == "student_invalid_reason":
            self.inreason = content



    def endElement(self, name):
        if self.current == "student_full_name":
            self.student_full_name.append(self.name)
        elif self.current == "student_group":
            self.student_group.append(self.group)
        elif self.current == "student_valid_reason":
            self.student_valid_reason.append(self.reason)
        elif self.current == "student_invalid_reason":
            self.student_invalid_reason.append(self.inreason)

        self.current = ""






