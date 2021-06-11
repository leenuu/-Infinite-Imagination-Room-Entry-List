from PyQt5 import QtCore, QtGui, QtWidgets
from main_thinking_class import attend_thinking
import time

class barcode_th(QtCore.QThread):
    user = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        
        self.main = parent
        self.isRun = False
        self.input_data_edit = None

    def run(self):
        while self.isRun:
            # print(self.input_data)
            time.sleep(0.5)
            us = str(self.input_data_edit.text())
            if len(us) == 8:
                self.user.emit(us)
                self.input_data_edit.setText("")
                # time.sleep(0.5)    

class Ui_Form(object):
    def __init__(self):
        self.user_data = barcode_th(self)
        self.user_data.user.connect(self.attend)
        self.att = attend_thinking()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 429)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        self.user_data.input_data_edit = QtWidgets.QLineEdit(Form)
        self.user_data.input_data_edit.setGeometry(QtCore.QRect(10, 20, 340, 30))
        self.user_data.input_data_edit.setObjectName("inpuy_data")
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

        self.start_brt.clicked.connect(self.start_read)
        self.stop_brt.clicked.connect(self.stop_read)
        self.user_data.input_data_edit.setDisabled(True)
        self.stop_brt.setDisabled(True)
        self.start_brt.setDisabled(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "무상실방명록"))
        self.start_brt.setText(_translate("Form", "시작"))
        self.stop_brt.setText(_translate("Form", "멈춤"))
        self.name_label.setText(_translate("Form", ""))
        self.img_label.setText(_translate("Form", ""))

    def start_read(self):
        self.stop_brt.setDisabled(False)
        self.start_brt.setDisabled(True)
        self.user_data.input_data_edit.setDisabled(False)
        self.user_data.isRun = True
        self.user_data.start()
    
    def stop_read(self):
        self.stop_brt.setDisabled(True)
        self.start_brt.setDisabled(False)
        self.user_data.input_data_edit.setDisabled(True)
        self.user_data.isRun = False

    def attend(self, user):
        print(user)
        self.att.find_img_name(user)
        img = self.att.img_path
        user_name = self.att.name
        _translate = QtCore.QCoreApplication.translate

        self.name_label.setText(_translate("Form", user_name))
        pixmap = QtGui.QPixmap(img)
        # print(pixmap.size())
        pixmap = pixmap.scaled(159, 191)
        self.img_label.setPixmap(pixmap)

        self.att.date_add(user)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
