from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_play_selection_window(object):
    def setupUi(self, play_selection):
        play_selection.setObjectName("play_selection")
        play_selection.resize(720, 421)
        play_selection.setStyleSheet("background-color: rgb(234, 254, 217);")
        self.button_choose_saves = QtWidgets.QPushButton(play_selection)
        self.button_choose_saves.setGeometry(QtCore.QRect(200, 100, 320, 80))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_choose_saves.setFont(font)
        self.button_choose_saves.setMouseTracking(False)
        self.button_choose_saves.setTabletTracking(False)
        self.button_choose_saves.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_choose_saves.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_choose_saves.setStyleSheet("\n"
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
        self.button_choose_saves.setIconSize(QtCore.QSize(16, 16))
        self.button_choose_saves.setFlat(False)
        self.button_choose_saves.setObjectName("button_choose_saves")
        self.button_start_new_game = QtWidgets.QPushButton(play_selection)
        self.button_start_new_game.setGeometry(QtCore.QRect(200, 210, 320, 80))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.button_start_new_game.setFont(font)
        self.button_start_new_game.setMouseTracking(False)
        self.button_start_new_game.setTabletTracking(False)
        self.button_start_new_game.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_start_new_game.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_start_new_game.setStyleSheet("\n"
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
        self.button_start_new_game.setIconSize(QtCore.QSize(16, 16))
        self.button_start_new_game.setFlat(False)
        self.button_start_new_game.setObjectName("button_start_new_game")

        self.retranslateUi(play_selection)
        QtCore.QMetaObject.connectSlotsByName(play_selection)

    def retranslateUi(self, play_selection):
        _translate = QtCore.QCoreApplication.translate
        play_selection.setWindowTitle(_translate("play_selection", "Парк развлечений"))
        self.button_choose_saves.setText(_translate("play_selection", "Выбрать сохранение"))
        self.button_start_new_game.setText(_translate("play_selection", "Начать новую игру"))

