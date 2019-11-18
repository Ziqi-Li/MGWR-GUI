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
        advDialog.resize(385, 221)
        advDialog.setModal(True)
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setGeometry(QtCore.QRect(250, 20, 110, 32))
        self.applyBTN.setObjectName("applyBTN")
        self.resetBTN = QtWidgets.QPushButton(advDialog)
        self.resetBTN.setGeometry(QtCore.QRect(250, 50, 110, 32))
        self.resetBTN.setObjectName("resetBTN")
        self.groupBox_4 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 60, 221, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.mcComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.mcComboBox.setGeometry(QtCore.QRect(10, 20, 201, 26))
        self.mcComboBox.setObjectName("mcComboBox")
        self.mcComboBox.addItem("")
        self.mcComboBox.addItem("")
        self.groupBox_5 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 110, 221, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.locollinearComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.locollinearComboBox.setGeometry(QtCore.QRect(10, 20, 201, 26))
        self.locollinearComboBox.setObjectName("locollinearComboBox")
        self.locollinearComboBox.addItem("")
        self.locollinearComboBox.addItem("")
        self.SOCBox_2 = QtWidgets.QGroupBox(advDialog)
        self.SOCBox_2.setGeometry(QtCore.QRect(10, 10, 221, 51))
        self.SOCBox_2.setObjectName("SOCBox_2")
        self.varSTDComboBox = QtWidgets.QComboBox(self.SOCBox_2)
        self.varSTDComboBox.setGeometry(QtCore.QRect(10, 20, 201, 26))
        self.varSTDComboBox.setObjectName("varSTDComboBox")
        self.varSTDComboBox.addItem("")
        self.varSTDComboBox.addItem("")
        self.groupBox_6 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 221, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.bwciComboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.bwciComboBox.setGeometry(QtCore.QRect(10, 20, 201, 26))
        self.bwciComboBox.setObjectName("bwciComboBox")
        self.bwciComboBox.addItem("")
        self.bwciComboBox.addItem("")
        
        '''
        self.groupBox_6 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 221, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.mccComboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.mccComboBox.setGeometry(QtCore.QRect(10, 20, 201, 26))
        self.mccComboBox.setObjectName("mccComboBox")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        '''
        
        
        self.advDialog = advDialog
        self.mcTest = "Off"
        self.varSTD = "On"
        self.locollinear = "Off"
        self.bw_ci = "Off"
        #self.mcc = "None"
        
        self.retranslateUi(advDialog)
        QtCore.QMetaObject.connectSlotsByName(advDialog)
    
    def retranslateUi(self, advDialog):
        _translate = QtCore.QCoreApplication.translate
        advDialog.setWindowTitle(_translate("advDialog", "Advanced Options"))
        self.applyBTN.setText(_translate("advDialog", "Apply"))
        self.resetBTN.setText(_translate("advDialog", "Reset"))
        self.groupBox_4.setTitle(_translate("advDialog", "Monte Carlo test for spatial variability"))
        self.mcComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.mcComboBox.setItemText(1, _translate("advDialog", "On (Very Slow)"))
        self.groupBox_5.setTitle(_translate("advDialog", "Local collinearity diagnostics"))
        self.locollinearComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.locollinearComboBox.setItemText(1, _translate("advDialog", "On"))
        self.SOCBox_2.setTitle(_translate("advDialog", "Variable standardization"))
        self.varSTDComboBox.setItemText(0, _translate("advDialog", "On"))
        self.varSTDComboBox.setItemText(1, _translate("advDialog", "Off"))
        self.groupBox_6.setTitle(_translate("advDialog", "Bandwidth confidence interval"))
        self.bwciComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.bwciComboBox.setItemText(1, _translate("advDialog", "On"))
        '''
        self.groupBox_6.setTitle(_translate("advDialog", "Multiple comparison correction"))
        self.mccComboBox.setItemText(0, _translate("advDialog", "None"))
        self.mccComboBox.setItemText(1, _translate("advDialog", "Bonferroni"))
        self.mccComboBox.setItemText(2, _translate("advDialog", "Sidak"))
        self.mccComboBox.setItemText(3, _translate("advDialog", "FDR"))
        '''

    
    def loadSettings(self):
        
        if self.locollinear == "Off":
            self.locollinearComboBox.setCurrentIndex(0)
        else:
            self.locollinearComboBox.setCurrentIndex(1)
        
        if self.mcTest == "Off":
            self.mcComboBox.setCurrentIndex(0)
        else:
            self.mcComboBox.setCurrentIndex(1)
        
        if self.varSTD == "On":
            self.varSTDComboBox.setCurrentIndex(0)
        else:
            self.varSTDComboBox.setCurrentIndex(1)
        
        if self.bw_ci == "Off":
            self.bwciComboBox.setCurrentIndex(0)
        else:
            self.bwciComboBox.setCurrentIndex(1)
        
        '''
        if self.mcc == "None":
            self.mccComboBox.setCurrentIndex(0)
        elif self.mcc == "Bonferroni":
            self.mccComboBox.setCurrentIndex(1)
        elif self.mcc == "Sidak":
            self.mccComboBox.setCurrentIndex(2)
        elif self.mcc == "FDR":
            self.mccComboBox.setCurrentIndex(3)
        '''

    def addActionsToUI(self):
        self.applyBTN.clicked.connect(self.applyOnClick)
        self.resetBTN.clicked.connect(self.resetOnClick)

    def applyOnClick(self):
        self.varSTD = self.varSTDComboBox.currentText()
        self.locollinear = self.locollinearComboBox.currentText()
        self.mcTest = self.mcComboBox.currentText()
        self.bw_ci = self.bwciComboBox.currentText()
        #self.mcc = self.mccComboBox.currentText()
        self.advDialog.close()
    
    def resetOnClick(self):
        self.varSTDComboBox.setCurrentIndex(0)
        self.locollinearComboBox.setCurrentIndex(0)
        self.mcComboBox.setCurrentIndex(0)
        self.bwciComboBox.setCurrentIndex(0)
        #self.mccComboBox.setCurrentIndex(0)


