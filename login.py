# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1312, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMaximumSize(QtCore.QSize(1980, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1331, 761))
        self.frame.setMinimumSize(QtCore.QSize(1280, 720))
        self.frame.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(33, 4, 163), stop:1 rgb(17, 2, 87));\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(290, 60, 3, 621))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(1040, 60, 3, 621))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(270, 120, 3, 500))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setEnabled(True)
        self.line_5.setGeometry(QtCore.QRect(1060, 90, 3, 500))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(330, 50, 681, 631))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgb(135, 189, 255), stop: 0  rgb(170, 170, 255));\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setTabletTracking(True)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    background-position:center;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_4.setIconSize(QtCore.QSize(5, 5))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(75, 45, 26, 25))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-image: url(:/Icons/imagens/profile-user.png);\n"
"    border-radius:25px;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.line_6 = QtWidgets.QFrame(self.frame_3)
        self.line_6.setGeometry(QtCore.QRect(10, 100, 671, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(200, 30, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(40, 80, 101, 16))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(630, 570, 35, 35))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-image: url(:/Icons/imagens/botton_engine.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius:16px;\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(300, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(60, 240, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 369, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 255, 255);  \n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(30, 310, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(320, 380, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(70, 380, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 299, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 255, 255);  \n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(390, 370, 171, 41))
        self.lineEdit_7.setStyleSheet("QLineEdit:focus{\n"
"    border: 2px solid;\n"
"    \n"
"}\n"
"")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 550, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 229, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 255, 255);  \n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setTabletTracking(True)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 85, 255);\n"
"    background-position:center;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_5.setIconSize(QtCore.QSize(5, 5))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "?"))
        self.label_7.setText(_translate("MainWindow", "Storage Control "))
        self.label_9.setText(_translate("MainWindow", " VC Não esta logado"))
        self.label_10.setText(_translate("MainWindow", "Login"))
        self.label_11.setText(_translate("MainWindow", "Nome"))
        self.label_12.setText(_translate("MainWindow", "Ocupação"))
        self.label_13.setText(_translate("MainWindow", "Senha"))
        self.label_14.setText(_translate("MainWindow", "CPF"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Digite Cliente, caso não for funcionario"))
        self.pushButton_8.setText(_translate("MainWindow", "Confirmar"))
        self.pushButton_5.setText(_translate("MainWindow", "←"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
