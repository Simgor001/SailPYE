# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\simgor\Desktop\SailPYE\aboutWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutWin(object):
    def setupUi(self, aboutWin):
        aboutWin.setObjectName("aboutWin")
        aboutWin.setWindowModality(QtCore.Qt.ApplicationModal)
        aboutWin.setEnabled(True)
        aboutWin.resize(566, 375)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutWin.sizePolicy().hasHeightForWidth())
        aboutWin.setSizePolicy(sizePolicy)
        aboutWin.setMouseTracking(False)
        aboutWin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        aboutWin.setStyleSheet("")
        aboutWin.setModal(True)
        self.label = QtWidgets.QLabel(aboutWin)
        self.label.setGeometry(QtCore.QRect(200, 40, 291, 50))
        font = QtGui.QFont()
        font.setFamily("文泉驿正黑")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 28pt \"文泉驿正黑\";\n"
"\n"
"color: rgb(85, 87, 83);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(aboutWin)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 91, 109))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(aboutWin)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 491, 41))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 57 13pt \"文泉驿微米黑\";\n"
"\n"
"color: rgb(85, 87, 83);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(aboutWin)
        self.label_4.setGeometry(QtCore.QRect(260, 92, 161, 40))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 57 13pt \"文泉驿微米黑\";\n"
"\n"
"color: rgb(136, 138, 133);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(aboutWin)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 490, 71))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setStyleSheet("font: 57 10.5pt \"文泉驿微米黑\";\n"
"\n"
"color: rgb(136, 138, 133);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(aboutWin)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 271, 16))
        self.label_7.setStyleSheet("color: rgb(136, 138, 133);\n"
"font: 11pt \"文泉驿微米黑\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(aboutWin)
        self.label_8.setGeometry(QtCore.QRect(40, 310, 271, 30))
        self.label_8.setStyleSheet("color: rgb(136, 138, 133);\n"
"font: 11pt \"文泉驿微米黑\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(aboutWin)
        self.label_9.setGeometry(QtCore.QRect(40, 340, 271, 30))
        self.label_9.setStyleSheet("color: rgb(136, 138, 133);\n"
"font: 10pt \"文泉驿微米黑\";")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(aboutWin)
        self.pushButton.setGeometry(QtCore.QRect(444, 330, 81, 31))
        self.pushButton.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(aboutWin)
        self.pushButton.clicked.connect(aboutWin.close)
        QtCore.QMetaObject.connectSlotsByName(aboutWin)

    def retranslateUi(self, aboutWin):
        _translate = QtCore.QCoreApplication.translate
        aboutWin.setWindowTitle(_translate("aboutWin", "关于Sail Python Editor"))
        self.label.setText(_translate("aboutWin", "Sail Python Editor"))
        self.label_3.setText(_translate("aboutWin", "Sail Python Editor 是一款开源、简洁的Python源代码编辑器，教育版为精简功能版。"))
        self.label_4.setText(_translate("aboutWin", "EDU 教育版 rev1.0.0"))
        self.label_5.setText(_translate("aboutWin", "Sail Python Editor是自由软件，基于GUN GPL2.0开源许可协议发布,意味着您可以自由运行、复制、分发、修改并且改进这款软件；本计算机程序受著作权法和国际公约的保护，并且本软件不提供任何形式的担保，使用时请严格遵守当地法律规章制度。"))
        self.label_7.setText(_translate("aboutWin", "<html><head/><body><p>作者：某不明生物</p></body></html>"))
        self.label_8.setText(_translate("aboutWin", "<html><head/><body><p>维护：化州市第一中学信息技术协会</p></body></html>"))
        self.label_9.setText(_translate("aboutWin", "<html><head/><body><p>Copyright © 2020 某不明生物。保留所有权利。</p></body></html>"))
        self.pushButton.setText(_translate("aboutWin", "确定"))
