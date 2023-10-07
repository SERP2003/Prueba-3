from PyQt5 import QtCore, QtGui, QtWidgets
from add_paciente import Ui_Dialog2

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 510)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 101, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 511))
        self.frame.setStyleSheet("background-color: rgb(157, 222, 253);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_anadir_citas = QtWidgets.QPushButton(self.frame)
        self.bt_anadir_citas.setGeometry(QtCore.QRect(20, 20, 171, 211))
        self.bt_anadir_citas.setStyleSheet("background-color: rgb(240, 158, 47);\n"
"QPushButton{\n"
"border:0px;\n"
"\n"
"padding-top:16px;\n"
"image-position:top;\n"
"\n"
"text-align:bottom;\n"
"padding-bottom:10px;\n"
"}")
        self.bt_anadir_citas.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("5980048.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_anadir_citas.setIcon(icon)
        self.bt_anadir_citas.setIconSize(QtCore.QSize(100, 100))
        self.bt_anadir_citas.setObjectName("bt_anadir_citas")
        self.bt_paciente = QtWidgets.QPushButton(self.frame)
        self.bt_paciente.setGeometry(QtCore.QRect(210, 20, 171, 211))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.bt_paciente.setFont(font)
        self.bt_paciente.setStyleSheet("background-color: rgb(240, 158, 47);\n"
"")
        self.bt_paciente.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("3845289 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_paciente.setIcon(icon1)
        self.bt_paciente.setIconSize(QtCore.QSize(100, 100))
        self.bt_paciente.setObjectName("bt_paciente")

        self.bt_citas_hoy = QtWidgets.QPushButton(self.frame)
        self.bt_citas_hoy.setGeometry(QtCore.QRect(20, 260, 171, 231))
        self.bt_citas_hoy.setStyleSheet("background-color: rgb(240, 158, 47);")
        self.bt_citas_hoy.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("4228731.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_citas_hoy.setIcon(icon2)
        self.bt_citas_hoy.setIconSize(QtCore.QSize(120, 120))
        self.bt_citas_hoy.setObjectName("bt_citas_hoy")
        self.bt_enviar = QtWidgets.QPushButton(self.frame)
        self.bt_enviar.setGeometry(QtCore.QRect(210, 260, 171, 231))
        self.bt_enviar.setStyleSheet("background-color: rgb(240, 158, 47);")
        self.bt_enviar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("7914672.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_enviar.setIcon(icon3)
        self.bt_enviar.setIconSize(QtCore.QSize(100, 100))
        self.bt_enviar.setObjectName("bt_enviar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 440, 91, 41))
        self.label_2.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(240, 158, 47);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 190, 141, 31))
        self.label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(240, 158, 47);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 121, 31))
        self.label_4.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(240, 158, 47);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(250, 440, 91, 31))
        self.label_5.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(240, 158, 47);\n"
"")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Citas de hoy"))
        self.label.setText(_translate("Dialog", "Añadir un paciente"))
        self.label_4.setText(_translate("Dialog", "Añadir una cita"))
        self.label_5.setText(_translate("Dialog", "Enviar todo"))

