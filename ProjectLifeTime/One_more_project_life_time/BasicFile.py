# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectLifeTime.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LifeTime(object):
    def setupUi(self, LifeTime):
        LifeTime.setObjectName("LifeTime")
        LifeTime.setWindowModality(QtCore.Qt.NonModal)
        LifeTime.resize(681, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LifeTime.sizePolicy().hasHeightForWidth())
        LifeTime.setSizePolicy(sizePolicy)
        LifeTime.setMaximumSize(QtCore.QSize(681, 539))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        LifeTime.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/hours.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LifeTime.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LifeTime)
        self.centralwidget.setObjectName("centralwidget")
        self.MainPage = QtWidgets.QFrame(self.centralwidget)
        self.MainPage.setGeometry(QtCore.QRect(0, 0, 681, 561))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.MainPage.setFont(font)
        self.MainPage.setStyleSheet("background-color: rgb(221, 254, 255);")
        self.MainPage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainPage.setObjectName("MainPage")
        self.Picture = QtWidgets.QLabel(self.MainPage)
        self.Picture.setGeometry(QtCore.QRect(460, 10, 200, 200))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("../../../Downloads/hours.png"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")
        self.Info = QtWidgets.QLabel(self.MainPage)
        self.Info.setGeometry(QtCore.QRect(30, 30, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Info.setFont(font)
        self.Info.setStyleSheet("color: rgb(255, 85, 0);")
        self.Info.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Info.setWordWrap(True)
        self.Info.setObjectName("Info")
        self.Details = QtWidgets.QGroupBox(self.MainPage)
        self.Details.setGeometry(QtCore.QRect(20, 230, 641, 201))
        self.Details.setStyleSheet("border: 2px solid #00ff00;")
        self.Details.setTitle("")
        self.Details.setFlat(False)
        self.Details.setObjectName("Details")
        self.titleMonth = QtWidgets.QLabel(self.Details)
        self.titleMonth.setGeometry(QtCore.QRect(30, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleMonth.setFont(font)
        self.titleMonth.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleMonth.setAlignment(QtCore.Qt.AlignCenter)
        self.titleMonth.setObjectName("titleMonth")
        self.titleYear = QtWidgets.QLabel(self.Details)
        self.titleYear.setGeometry(QtCore.QRect(30, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleYear.setFont(font)
        self.titleYear.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleYear.setAlignment(QtCore.Qt.AlignCenter)
        self.titleYear.setObjectName("titleYear")
        self.titleDay = QtWidgets.QLabel(self.Details)
        self.titleDay.setGeometry(QtCore.QRect(30, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleDay.setFont(font)
        self.titleDay.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleDay.setAlignment(QtCore.Qt.AlignCenter)
        self.titleDay.setObjectName("titleDay")
        self.titleHour = QtWidgets.QLabel(self.Details)
        self.titleHour.setGeometry(QtCore.QRect(340, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleHour.setFont(font)
        self.titleHour.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleHour.setAlignment(QtCore.Qt.AlignCenter)
        self.titleHour.setObjectName("titleHour")
        self.titleMinute = QtWidgets.QLabel(self.Details)
        self.titleMinute.setGeometry(QtCore.QRect(330, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleMinute.setFont(font)
        self.titleMinute.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleMinute.setAlignment(QtCore.Qt.AlignCenter)
        self.titleMinute.setObjectName("titleMinute")
        self.titleSecond = QtWidgets.QLabel(self.Details)
        self.titleSecond.setGeometry(QtCore.QRect(330, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleSecond.setFont(font)
        self.titleSecond.setStyleSheet("border: 0px;\n"
"color: rgb(255, 85, 0);")
        self.titleSecond.setAlignment(QtCore.Qt.AlignCenter)
        self.titleSecond.setObjectName("titleSecond")
        self.Month = QtWidgets.QComboBox(self.Details)
        self.Month.setGeometry(QtCore.QRect(140, 20, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Month.setFont(font)
        self.Month.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;")
        self.Month.setEditable(False)
        self.Month.setMaxVisibleItems(12)
        self.Month.setObjectName("Month")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Month.addItem("")
        self.Year = QtWidgets.QSpinBox(self.Details)
        self.Year.setGeometry(QtCore.QRect(140, 70, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Year.setFont(font)
        self.Year.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;\n"
"text-decoration: bold;")
        self.Year.setAlignment(QtCore.Qt.AlignCenter)
        self.Year.setMinimum(1900)
        self.Year.setMaximum(2025)
        self.Year.setProperty("value", 2000)
        self.Year.setObjectName("Year")
        self.Day = QtWidgets.QSpinBox(self.Details)
        self.Day.setGeometry(QtCore.QRect(140, 120, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Day.setFont(font)
        self.Day.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;\n"
"text-decoration: bold;")
        self.Day.setAlignment(QtCore.Qt.AlignCenter)
        self.Day.setMinimum(1)
        self.Day.setMaximum(31)
        self.Day.setProperty("value", 15)
        self.Day.setObjectName("Day")
        self.Hour = QtWidgets.QSpinBox(self.Details)
        self.Hour.setGeometry(QtCore.QRect(510, 20, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Hour.setFont(font)
        self.Hour.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;\n"
"text-decoration: bold;")
        self.Hour.setAlignment(QtCore.Qt.AlignCenter)
        self.Hour.setMinimum(0)
        self.Hour.setMaximum(23)
        self.Hour.setProperty("value", 14)
        self.Hour.setObjectName("Hour")
        self.Minute = QtWidgets.QSpinBox(self.Details)
        self.Minute.setGeometry(QtCore.QRect(510, 70, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Minute.setFont(font)
        self.Minute.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;\n"
"text-decoration: bold;")
        self.Minute.setAlignment(QtCore.Qt.AlignCenter)
        self.Minute.setMinimum(0)
        self.Minute.setMaximum(59)
        self.Minute.setProperty("value", 30)
        self.Minute.setObjectName("Minute")
        self.Second = QtWidgets.QSpinBox(self.Details)
        self.Second.setGeometry(QtCore.QRect(510, 120, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Second.setFont(font)
        self.Second.setStyleSheet("border: 2px solid #008dd4;\n"
"text-align: center;\n"
"text-decoration: bold;")
        self.Second.setAlignment(QtCore.Qt.AlignCenter)
        self.Second.setMinimum(0)
        self.Second.setMaximum(59)
        self.Second.setProperty("value", 30)
        self.Second.setObjectName("Second")
        self.checkBox = QtWidgets.QCheckBox(self.Details)
        self.checkBox.setGeometry(QtCore.QRect(310, 170, 321, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("border: 0px;\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.getResult = QtWidgets.QPushButton(self.MainPage)
        self.getResult.setGeometry(QtCore.QRect(200, 450, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.getResult.setFont(font)
        self.getResult.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.getResult.setStyleSheet("QPushButton::hover {\n"
"color: rgb(255, 170, 0);\n"
"text-decoration: underline;\n"
"}\n"
"QPushButton::focus {\n"
"color: rgb(0, 170, 0);\n"
"}")
        self.getResult.setFlat(True)
        self.getResult.setObjectName("getResult")
        LifeTime.setCentralWidget(self.centralwidget)

        self.retranslateUi(LifeTime)
        self.Month.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(LifeTime)

    def retranslateUi(self, LifeTime):
        _translate = QtCore.QCoreApplication.translate
        LifeTime.setWindowTitle(_translate("LifeTime", "Life Time"))
        self.Info.setText(_translate("LifeTime", "????????????????, ???????????? ???????? ????????????, ?????????????? ???? ???????????? ?????????????? ???? ?????? ???????????? ???? ???????????? ????????????. ?????? ?????????????????? ???????????????????? ?????????????????????? ???????????? ?????????????? ????????????:"))
        self.titleMonth.setText(_translate("LifeTime", "??????????:"))
        self.titleYear.setText(_translate("LifeTime", "??????:"))
        self.titleDay.setText(_translate("LifeTime", "????????:"))
        self.titleHour.setText(_translate("LifeTime", "?????? (????????????.):"))
        self.titleMinute.setText(_translate("LifeTime", "???????????? (????????????.):"))
        self.titleSecond.setText(_translate("LifeTime", "?????????????? (????????????.):"))
        self.Month.setCurrentText(_translate("LifeTime", "????????????"))
        self.Month.setItemText(0, _translate("LifeTime", "????????????"))
        self.Month.setItemText(1, _translate("LifeTime", "??????????????"))
        self.Month.setItemText(2, _translate("LifeTime", "????????"))
        self.Month.setItemText(3, _translate("LifeTime", "????????????"))
        self.Month.setItemText(4, _translate("LifeTime", "??????"))
        self.Month.setItemText(5, _translate("LifeTime", "????????"))
        self.Month.setItemText(6, _translate("LifeTime", "????????"))
        self.Month.setItemText(7, _translate("LifeTime", "????????????"))
        self.Month.setItemText(8, _translate("LifeTime", "????????????????"))
        self.Month.setItemText(9, _translate("LifeTime", "??????????????"))
        self.Month.setItemText(10, _translate("LifeTime", "????????????"))
        self.Month.setItemText(11, _translate("LifeTime", "??????????????"))
        self.checkBox.setText(_translate("LifeTime", "?????????????????? ??????, ????????????, ??????????????"))
        self.getResult.setText(_translate("LifeTime", "???????????? >>>"))
