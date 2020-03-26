# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\simgor\Desktop\SailPYE\toolsWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_toolsWin(object):
    def setupUi(self, toolsWin):
        toolsWin.setObjectName("toolsWin")
        toolsWin.setWindowModality(QtCore.Qt.ApplicationModal)
        toolsWin.resize(396, 175)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toolsWin.sizePolicy().hasHeightForWidth())
        toolsWin.setSizePolicy(sizePolicy)
        toolsWin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        toolsWin.setModal(True)
        self.formLayoutWidget = QtWidgets.QWidget(toolsWin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.formLayoutWidget)
        self.keySequenceEdit.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.keySequenceEdit)
        self.T_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T_name.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.T_name.setObjectName("T_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.T_name)
        self.T_win32 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T_win32.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.T_win32.setObjectName("T_win32")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.T_win32)
        self.T_linux = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T_linux.setStyleSheet("font: 11pt \"文泉驿微米黑\";")
        self.T_linux.setObjectName("T_linux")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.T_linux)
        self.buttonBox = QtWidgets.QDialogButtonBox(toolsWin)
        self.buttonBox.setGeometry(QtCore.QRect(210, 140, 166, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(toolsWin)
        self.buttonBox.rejected.connect(toolsWin.close)
        QtCore.QMetaObject.connectSlotsByName(toolsWin)
        toolsWin.setTabOrder(self.T_name, self.T_win32)
        toolsWin.setTabOrder(self.T_win32, self.T_linux)
        toolsWin.setTabOrder(self.T_linux, self.keySequenceEdit)

    def retranslateUi(self, toolsWin):
        _translate = QtCore.QCoreApplication.translate
        toolsWin.setWindowTitle(_translate("toolsWin", "添加工具..."))
        self.label.setText(_translate("toolsWin", "名称："))
        self.label_2.setText(_translate("toolsWin", "命令(win32)："))
        self.label_3.setText(_translate("toolsWin", "命令(linux)："))
        self.label_4.setText(_translate("toolsWin", "快捷键："))
