# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_advGWRDialog(object):
    def setupUi(self, advDialog):
        advDialog.setObjectName("advDialog")
        advDialog.setWindowModality(QtCore.Qt.WindowModal)
        advDialog.resize(372, 124)
        advDialog.setModal(True)
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setGeometry(QtCore.QRect(250, 20, 110, 32))
        self.applyBTN.setObjectName("applyBTN")
        self.resetBTN = QtWidgets.QPushButton(advDialog)
        self.resetBTN.setGeometry(QtCore.QRect(250, 60, 110, 32))
        self.resetBTN.setObjectName("resetBTN")
        self.groupBox_4 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 221, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.mcComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.mcComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.mcComboBox.setObjectName("mcComboBox")
        self.mcComboBox.addItem("")
        self.mcComboBox.addItem("")
        self.groupBox_5 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 60, 221, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.locollinearComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.locollinearComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.locollinearComboBox.setObjectName("locollinearComboBox")
        self.locollinearComboBox.addItem("")
        self.locollinearComboBox.addItem("")
        
        
        self.advDialog = advDialog
        self.mcTest = "Off"
        self.locollinear = "Off"
        
        self.retranslateUi(advDialog)
        QtCore.QMetaObject.connectSlotsByName(advDialog)
    
    def retranslateUi(self, advDialog):
        _translate = QtCore.QCoreApplication.translate
        advDialog.setWindowTitle(_translate("advDialog", "Advanced Options"))
        self.applyBTN.setText(_translate("advDialog", "Apply"))
        self.resetBTN.setText(_translate("advDialog", "Reset"))
        self.groupBox_4.setTitle(_translate("advDialog", "Monte Carlo test for spatial variability"))
        self.mcComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.mcComboBox.setItemText(1, _translate("advDialog", "On (Slow)"))
        self.groupBox_5.setTitle(_translate("advDialog", "Local collinearity diagnostics"))
        self.locollinearComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.locollinearComboBox.setItemText(1, _translate("advDialog", "On"))

    
    def loadSettings(self):
        
        if self.locollinear == "Off":
            self.locollinearComboBox.setCurrentIndex(0)
        else:
            self.locollinearComboBox.setCurrentIndex(1)
        
        if self.mcTest == "Off":
            self.mcComboBox.setCurrentIndex(0)
        else:
            self.mcComboBox.setCurrentIndex(1)


    def addActionsToUI(self):
        self.applyBTN.clicked.connect(self.applyOnClick)
        self.resetBTN.clicked.connect(self.resetOnClick)

    def applyOnClick(self):
        self.locollinear = self.locollinearComboBox.currentText()
        self.mcTest = self.mcComboBox.currentText()
        self.advDialog.close()
    
    def resetOnClick(self):
        self.locollinearComboBox.setCurrentIndex(0)
        self.mcComboBox.setCurrentIndex(0)


