# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_select_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_save_select_window(object):
    def setupUi(self, save_select_window):
        save_select_window.setObjectName("save_select_window")
        save_select_window.resize(720, 420)
        save_select_window.setStyleSheet("background-color: rgb(234, 254, 217);")
        self.button_upload_save = QtWidgets.QPushButton(save_select_window)
        self.button_upload_save.setGeometry(QtCore.QRect(510, 300, 201, 111))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_upload_save.setFont(font)
        self.button_upload_save.setMouseTracking(False)
        self.button_upload_save.setTabletTracking(False)
        self.button_upload_save.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_upload_save.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_upload_save.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"    padding: 4px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(163, 250, 92);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(170, 223, 120);\n"
"    }")
        self.button_upload_save.setIconSize(QtCore.QSize(16, 16))
        self.button_upload_save.setFlat(False)
        self.button_upload_save.setObjectName("button_upload_save")
##########################################################################

        self.frame_of_saves = QtWidgets.QFrame(save_select_window)
        self.frame_of_saves.setGeometry(QtCore.QRect(10, 10, 491, 401))
        self.frame_of_saves.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(152, 152, 152);")
        self.frame_of_saves.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_of_saves.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_of_saves.setObjectName("frame_of_saves")
        self.button_save_1 = QtWidgets.QPushButton(self.frame_of_saves)
        self.button_save_1.setGeometry(QtCore.QRect(10, 10, 471, 41))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_save_1.setFont(font)
        self.button_save_1.setMouseTracking(False)
        self.button_save_1.setTabletTracking(False)
        self.button_save_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_save_1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_save_1.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"    padding: 4px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(163, 250, 92);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(170, 223, 120);\n"
"    }")
        self.button_save_1.setIconSize(QtCore.QSize(16, 16))
        self.button_save_1.setFlat(False)
        self.button_save_1.setObjectName("button_save_1")
        self.button_save_2 = QtWidgets.QPushButton(self.frame_of_saves)
        self.button_save_2.setGeometry(QtCore.QRect(10, 60, 471, 41))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_save_2.setFont(font)
        self.button_save_2.setMouseTracking(False)
        self.button_save_2.setTabletTracking(False)
        self.button_save_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_save_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_save_2.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"    padding: 4px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(163, 250, 92);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(170, 223, 120);\n"
"    }")
        self.button_save_2.setIconSize(QtCore.QSize(16, 16))
        self.button_save_2.setFlat(False)
        self.button_save_2.setObjectName("button_save_2")
        self.button_save_3 = QtWidgets.QPushButton(self.frame_of_saves)
        self.button_save_3.setGeometry(QtCore.QRect(10, 110, 471, 41))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_save_3.setFont(font)
        self.button_save_3.setMouseTracking(False)
        self.button_save_3.setTabletTracking(False)
        self.button_save_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_save_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_save_3.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"    padding: 4px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(163, 250, 92);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(170, 223, 120);\n"
"    }")
        self.button_save_3.setIconSize(QtCore.QSize(16, 16))
        self.button_save_3.setFlat(False)
        self.button_save_3.setObjectName("button_save_3")
        self.button_save_4 = QtWidgets.QPushButton(self.frame_of_saves)
        self.button_save_4.setGeometry(QtCore.QRect(10, 160, 471, 41))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_save_4.setFont(font)
        self.button_save_4.setMouseTracking(False)
        self.button_save_4.setTabletTracking(False)
        self.button_save_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_save_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_save_4.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"    padding: 4px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(163, 250, 92);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(170, 223, 120);\n"
"    }")
        self.button_save_4.setIconSize(QtCore.QSize(16, 16))
        self.button_save_4.setFlat(False)
        self.button_save_4.setObjectName("button_save_4")
        self.choose_save_text = QtWidgets.QLabel(save_select_window)
        self.choose_save_text.setGeometry(QtCore.QRect(510, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_save_text.setFont(font)
        self.choose_save_text.setObjectName("choose_save_text")
        self.choosed_save_data_text = QtWidgets.QLabel(save_select_window)
        self.choosed_save_data_text.setGeometry(QtCore.QRect(510, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choosed_save_data_text.setFont(font)
        self.choosed_save_data_text.setObjectName("choosed_save_data_text")
        self.is_choosed_text = QtWidgets.QLabel(save_select_window)
        self.is_choosed_text.setGeometry(QtCore.QRect(510, 237, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.is_choosed_text.setFont(font)
        self.is_choosed_text.setObjectName("is_choosed_text")

        self.retranslateUi(save_select_window)
        QtCore.QMetaObject.connectSlotsByName(save_select_window)

    def retranslateUi(self, save_select_window):
        _translate = QtCore.QCoreApplication.translate
        save_select_window.setWindowTitle(_translate("save_select_window", "Парк развлечений"))
        self.button_upload_save.setText(_translate("save_select_window", "Загрузить"))
        self.button_save_1.setText(_translate("save_select_window", "Сохранение...................22.11.2022"))
        self.button_save_2.setText(_translate("save_select_window", "Сохранение...................18.11.2022"))
        self.button_save_3.setText(_translate("save_select_window", "Сохранение...................02.10.2022"))
        self.button_save_4.setText(_translate("save_select_window", "Сохранение...................01.09.1970"))
        self.choose_save_text.setText(_translate("save_select_window", "Выберите сохранение"))
        self.choosed_save_data_text.setText(_translate("save_select_window", "Сохранение 22.11.2022"))
        self.is_choosed_text.setText(_translate("save_select_window", "Выбрано:"))
