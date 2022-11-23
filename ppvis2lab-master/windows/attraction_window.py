# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attraction_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_information_about_attraction(object):
    def setupUi(self, information_about_attraction):
        information_about_attraction.setObjectName("information_about_attraction")
        information_about_attraction.resize(660, 472)
        information_about_attraction.setStyleSheet("background-color: rgb(203, 250, 172);")
        self.info_about_attraction_textBrowser = QtWidgets.QTextBrowser(information_about_attraction)
        self.info_about_attraction_textBrowser.setGeometry(QtCore.QRect(20, 10, 271, 31))
        self.info_about_attraction_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_about_attraction_textBrowser.setObjectName("info_about_attraction_textBrowser")
        self.attraction_name_textBrowser = QtWidgets.QTextBrowser(information_about_attraction)
        self.attraction_name_textBrowser.setGeometry(QtCore.QRect(20, 50, 341, 31))
        self.attraction_name_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.attraction_name_textBrowser.setObjectName("attraction_name_textBrowser")
        self.session_time_textBrowser = QtWidgets.QTextBrowser(information_about_attraction)
        self.session_time_textBrowser.setGeometry(QtCore.QRect(20, 80, 341, 31))
        self.session_time_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.session_time_textBrowser.setObjectName("session_time_textBrowser")
        self.capacity_textBrowser = QtWidgets.QTextBrowser(information_about_attraction)
        self.capacity_textBrowser.setGeometry(QtCore.QRect(20, 110, 341, 31))
        self.capacity_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.capacity_textBrowser.setObjectName("capacity_textBrowser")
        self.button_sell = QtWidgets.QPushButton(information_about_attraction)
        self.button_sell.setGeometry(QtCore.QRect(10, 390, 141, 71))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.button_sell.setFont(font)
        self.button_sell.setMouseTracking(False)
        self.button_sell.setTabletTracking(False)
        self.button_sell.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_sell.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_sell.setStyleSheet("\n"
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
        self.button_sell.setIconSize(QtCore.QSize(16, 16))
        self.button_sell.setFlat(False)
        self.button_sell.setObjectName("button_sell")
        self.queue_textBrowser = QtWidgets.QTextBrowser(information_about_attraction)
        self.queue_textBrowser.setGeometry(QtCore.QRect(20, 140, 341, 31))
        self.queue_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.queue_textBrowser.setObjectName("queue_textBrowser")

        self.retranslateUi(information_about_attraction)
        QtCore.QMetaObject.connectSlotsByName(information_about_attraction)

    def retranslateUi(self, information_about_attraction):
        _translate = QtCore.QCoreApplication.translate
        information_about_attraction.setWindowTitle(_translate("information_about_attraction", "Информация об аттракционе"))
        self.info_about_attraction_textBrowser.setHtml(_translate("information_about_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Информация об аттракционе</span></p></body></html>"))
        self.attraction_name_textBrowser.setHtml(_translate("information_about_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Аттракцион</span></p></body></html>"))
        self.session_time_textBrowser.setHtml(_translate("information_about_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Время сессии: 0:05/2.30</span></p></body></html>"))
        self.capacity_textBrowser.setHtml(_translate("information_about_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Вместимость: 16 человек</span></p></body></html>"))
        self.button_sell.setText(_translate("information_about_attraction", "Продать"))
        self.queue_textBrowser.setHtml(_translate("information_about_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Очередь: 7/16</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_about_attraction = QtWidgets.QDialog()
    ui = Ui_information_about_attraction()
    ui.setupUi(information_about_attraction)
    information_about_attraction.show()
    sys.exit(app.exec_())