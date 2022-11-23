# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buy_place_for_attraction.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_information_about_new_place_attraction(object):
    def setupUi(self, information_about_new_place_attraction):
        information_about_new_place_attraction.setObjectName("information_about_new_place_attraction")
        information_about_new_place_attraction.resize(660, 473)
        information_about_new_place_attraction.setStyleSheet("background-color: rgb(203, 250, 172);")
        self.new_place_buy_textBrowser = QtWidgets.QTextBrowser(information_about_new_place_attraction)
        self.new_place_buy_textBrowser.setGeometry(QtCore.QRect(20, 10, 291, 31))
        self.new_place_buy_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.new_place_buy_textBrowser.setObjectName("new_place_buy_textBrowser")
        self.price_textBrowser = QtWidgets.QTextBrowser(information_about_new_place_attraction)
        self.price_textBrowser.setGeometry(QtCore.QRect(20, 50, 341, 31))
        self.price_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.price_textBrowser.setObjectName("price_textBrowser")
        self.button_buy = QtWidgets.QPushButton(information_about_new_place_attraction)
        self.button_buy.setGeometry(QtCore.QRect(10, 390, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.button_buy.setFont(font)
        self.button_buy.setMouseTracking(False)
        self.button_buy.setTabletTracking(False)
        self.button_buy.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_buy.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_buy.setStyleSheet("\n"
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
        self.button_buy.setIconSize(QtCore.QSize(16, 16))
        self.button_buy.setFlat(False)
        self.button_buy.setObjectName("button_buy")

        self.retranslateUi(information_about_new_place_attraction)
        QtCore.QMetaObject.connectSlotsByName(information_about_new_place_attraction)

    def retranslateUi(self, information_about_new_place_attraction):
        _translate = QtCore.QCoreApplication.translate
        information_about_new_place_attraction.setWindowTitle(_translate("information_about_new_place_attraction", "Информация о новом месте для аттракциона"))
        self.new_place_buy_textBrowser.setHtml(_translate("information_about_new_place_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Новое место для аттракциона</span></p></body></html>"))
        self.price_textBrowser.setHtml(_translate("information_about_new_place_attraction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Стоимость: 500$</span></p></body></html>"))
        self.button_buy.setText(_translate("information_about_new_place_attraction", "Купить!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_about_new_place_attraction = QtWidgets.QDialog()
    ui = Ui_information_about_new_place_attraction()
    ui.setupUi(information_about_new_place_attraction)
    information_about_new_place_attraction.show()
    sys.exit(app.exec_())
