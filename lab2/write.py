from xml.dom.minidom import Document


def make_xml(lst):
    doc = Document()
    data = doc.createElement("data")
    doc.appendChild(data)
    for i in range(len(lst['full_name'])):
        students = doc.createElement("students")

        node_full_name = doc.createElement('student_full_name')
        students.appendChild(node_full_name)
        node_full_name.appendChild(doc.createTextNode(lst['full_name'][i]))

        node_group = doc.createElement('student_group')
        students.appendChild(node_group)
        node_group.appendChild(doc.createTextNode(lst['group'][i]))

        node_valid_reason = doc.createElement('student_valid_reason')
        students.appendChild(node_valid_reason)
        node_valid_reason.appendChild(doc.createTextNode(str(lst['valid_reason'][i])))

        node_invalid_reason = doc.createElement('student_invalid_reason')
        students.appendChild(node_invalid_reason)
        node_invalid_reason.appendChild(doc.createTextNode(str(lst['invalid_reason'][i])))

        data.appendChild(students)

    return doc
