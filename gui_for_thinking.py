# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_for_thinking.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 429)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        self.inpuy_data = QtWidgets.QLineEdit(Form)
        self.inpuy_data.setGeometry(QtCore.QRect(10, 20, 340, 30))
        self.inpuy_data.setObjectName("inpuy_data")
        self.start_brt = QtWidgets.QPushButton(Form)
        self.start_brt.setGeometry(QtCore.QRect(10, 60, 160, 50))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(22)
        self.start_brt.setFont(font)
        self.start_brt.setObjectName("start_brt")
        self.stop_brt = QtWidgets.QPushButton(Form)
        self.stop_brt.setGeometry(QtCore.QRect(190, 60, 160, 50))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.stop_brt.setFont(font)
        self.stop_brt.setObjectName("stop_brt")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(10, 330, 340, 90))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.img_label = QtWidgets.QLabel(Form)
        self.img_label.setGeometry(QtCore.QRect(10, 110, 340, 211))
        font = QtGui.QFont()
        font.setFamily("한컴산뜻돋움")
        font.setPointSize(20)
        self.img_label.setFont(font)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start_brt.setText(_translate("Form", "시작"))
        self.stop_brt.setText(_translate("Form", "멈춤"))
        self.name_label.setText(_translate("Form", "name"))
        self.img_label.setText(_translate("Form", "img"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())