# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'running_now.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_runningDialog(object):
    def setupUi(self, runningDialog):
        runningDialog.setObjectName("runningDialog")
        runningDialog.resize(292, 104)
        runningDialog.setModal(True)
        self.lineEdit = QtWidgets.QLineEdit(runningDialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 101, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(runningDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(runningDialog)
        self.progressBar.setGeometry(QtCore.QRect(60, 60, 161, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(runningDialog)
        QtCore.QMetaObject.connectSlotsByName(runningDialog)

    def retranslateUi(self, runningDialog):
        _translate = QtCore.QCoreApplication.translate
        runningDialog.setWindowTitle(_translate("runningDialog", "Dialog"))
        self.label.setText(_translate("runningDialog", "Time Elapsed:"))

