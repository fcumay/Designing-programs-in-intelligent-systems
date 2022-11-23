# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_information_about_visitor(object):
    def setupUi(self, information_about_visitor):
        information_about_visitor.setObjectName("information_about_visitor")
        information_about_visitor.resize(660, 473)
        information_about_visitor.setStyleSheet("background-color: rgb(203, 250, 172);")
        self.info_about_visitor_textBrowser = QtWidgets.QTextBrowser(information_about_visitor)
        self.info_about_visitor_textBrowser.setGeometry(QtCore.QRect(20, 10, 271, 31))
        self.info_about_visitor_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_about_visitor_textBrowser.setObjectName("info_about_visitor_textBrowser")
        self.visitor_name_textBrowser = QtWidgets.QTextBrowser(information_about_visitor)
        self.visitor_name_textBrowser.setGeometry(QtCore.QRect(20, 50, 341, 31))
        self.visitor_name_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visitor_name_textBrowser.setObjectName("visitor_name_textBrowser")
        self.visitor_money_textBrowser = QtWidgets.QTextBrowser(information_about_visitor)
        self.visitor_money_textBrowser.setGeometry(QtCore.QRect(20, 80, 341, 31))
        self.visitor_money_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visitor_money_textBrowser.setObjectName("visitor_money_textBrowser")
        self.visitor_is_buisnesmen_textBrowser = QtWidgets.QTextBrowser(information_about_visitor)
        self.visitor_is_buisnesmen_textBrowser.setGeometry(QtCore.QRect(20, 110, 341, 31))
        self.visitor_is_buisnesmen_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visitor_is_buisnesmen_textBrowser.setObjectName("visitor_is_buisnesmen_textBrowser")
        self.button_let_in_park = QtWidgets.QPushButton(information_about_visitor)
        self.button_let_in_park.setGeometry(QtCore.QRect(10, 390, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.button_let_in_park.setFont(font)
        self.button_let_in_park.setMouseTracking(False)
        self.button_let_in_park.setTabletTracking(False)
        self.button_let_in_park.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_let_in_park.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_let_in_park.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"\n"
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
        self.button_let_in_park.setIconSize(QtCore.QSize(16, 16))
        self.button_let_in_park.setFlat(False)
        self.button_let_in_park.setObjectName("button_let_in_park")
        self.button_delete_from_park = QtWidgets.QPushButton(information_about_visitor)
        self.button_delete_from_park.setGeometry(QtCore.QRect(260, 390, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.button_delete_from_park.setFont(font)
        self.button_delete_from_park.setMouseTracking(False)
        self.button_delete_from_park.setTabletTracking(False)
        self.button_delete_from_park.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_delete_from_park.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_delete_from_park.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"\n"
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
        self.button_delete_from_park.setIconSize(QtCore.QSize(16, 16))
        self.button_delete_from_park.setFlat(False)
        self.button_delete_from_park.setObjectName("button_delete_from_park")
        self.button_put_in_queue = QtWidgets.QPushButton(information_about_visitor)
        self.button_put_in_queue.setGeometry(QtCore.QRect(510, 390, 141, 71))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.button_put_in_queue.setFont(font)
        self.button_put_in_queue.setMouseTracking(False)
        self.button_put_in_queue.setTabletTracking(False)
        self.button_put_in_queue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_put_in_queue.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_put_in_queue.setStyleSheet("\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border: 2px solid #111;\n"
"    border-color: rgb(167, 167, 167);\n"
"    background-color: rgb(190, 250, 134);\n"
"\n"
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
        self.button_put_in_queue.setIconSize(QtCore.QSize(16, 16))
        self.button_put_in_queue.setFlat(False)
        self.button_put_in_queue.setObjectName("button_put_in_queue")

        self.retranslateUi(information_about_visitor)
        QtCore.QMetaObject.connectSlotsByName(information_about_visitor)

    def retranslateUi(self, information_about_visitor):
        _translate = QtCore.QCoreApplication.translate
        information_about_visitor.setWindowTitle(_translate("information_about_visitor", "Информация о посетителе"))
        self.info_about_visitor_textBrowser.setHtml(_translate("information_about_visitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Информация о посетителе</span></p></body></html>"))
        self.visitor_name_textBrowser.setHtml(_translate("information_about_visitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Имя: Райан Гослинг</span></p></body></html>"))
        self.visitor_money_textBrowser.setHtml(_translate("information_about_visitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Денег: 25$</span></p></body></html>"))
        self.visitor_is_buisnesmen_textBrowser.setHtml(_translate("information_about_visitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Бизнесмен: нет</span></p></body></html>"))
        self.button_let_in_park.setText(_translate("information_about_visitor", "Впустить в\n"
" парк"))
        self.button_delete_from_park.setText(_translate("information_about_visitor", "Удалить с\n"
" парка"))
        self.button_put_in_queue.setText(_translate("information_about_visitor", "Поставить в\n"
" очередь"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_about_visitor = QtWidgets.QDialog()
    ui = Ui_information_about_visitor()
    ui.setupUi(information_about_visitor)
    information_about_visitor.show()
    sys.exit(app.exec_())