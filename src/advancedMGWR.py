# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advOptMGWR.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_advMGWRDialog(object):
    def setupUi(self, advDialog):
        advDialog.setObjectName("advDialog")
        advDialog.setWindowModality(QtCore.Qt.WindowModal)
        advDialog.resize(480, 231)
        advDialog.setModal(True)
        self.SOCBox = QtWidgets.QGroupBox(advDialog)
        self.SOCBox.setGeometry(QtCore.QRect(250, 10, 221, 51))
        self.SOCBox.setObjectName("SOCBox")
        self.SOCComboBox = QtWidgets.QComboBox(self.SOCBox)
        self.SOCComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.SOCComboBox.setObjectName("SOCComboBox")
        self.SOCComboBox.addItem("")
        self.SOCComboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 221, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.initComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.initComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.initComboBox.setObjectName("initComboBox")
        self.initComboBox.addItem("")
        self.initComboBox.addItem("")
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setGeometry(QtCore.QRect(250, 180, 101, 32))
        self.applyBTN.setObjectName("applyBTN")
        self.resetBTN = QtWidgets.QPushButton(advDialog)
        self.resetBTN.setGeometry(QtCore.QRect(369, 180, 101, 32))
        self.resetBTN.setObjectName("resetBTN")
        self.groupBox_3 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 60, 221, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.convComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.convComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.convComboBox.setObjectName("convComboBox")
        self.convComboBox.addItem("")
        self.convComboBox.addItem("")
        self.SOCBox_2 = QtWidgets.QGroupBox(advDialog)
        self.SOCBox_2.setGeometry(QtCore.QRect(10, 10, 221, 51))
        self.SOCBox_2.setObjectName("SOCBox_2")
        self.varSTDComboBox = QtWidgets.QComboBox(self.SOCBox_2)
        self.varSTDComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.varSTDComboBox.setObjectName("varSTDComboBox")
        self.varSTDComboBox.addItem("")
        self.varSTDComboBox.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 221, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.mcComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.mcComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.mcComboBox.setObjectName("mcComboBox")
        self.mcComboBox.addItem("")
        self.mcComboBox.addItem("")
        self.groupBox_5 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 110, 221, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.locollinearComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.locollinearComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.locollinearComboBox.setObjectName("locollinearComboBox")
        self.locollinearComboBox.addItem("")
        self.locollinearComboBox.addItem("")
        self.groupBox_6 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 221, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.mccComboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.mccComboBox.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.mccComboBox.setObjectName("mccComboBox")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        self.mccComboBox.addItem("")
        
        self.advDialog = advDialog
        self.varSTD = "On"
        self.mcTest = "Off"
        self.locollinear = "Off"
        self.soc = "SOC-f"
        self.init = "GWR estimates"
        self.converg = "1e-5"
        self.mcc = "None"
        
        self.retranslateUi(advDialog)
        QtCore.QMetaObject.connectSlotsByName(advDialog)
    
    def retranslateUi(self, advDialog):
        _translate = QtCore.QCoreApplication.translate
        advDialog.setWindowTitle(_translate("advDialog", "Advanced Options"))
        self.SOCBox.setTitle(_translate("advDialog", "Measure of Score of Change (SOC)"))
        self.SOCComboBox.setItemText(0, _translate("advDialog", "SOC-f"))
        self.SOCComboBox.setItemText(1, _translate("advDialog", "SOC-RSS"))
        self.groupBox_2.setTitle(_translate("advDialog", "Initialization"))
        self.initComboBox.setItemText(0, _translate("advDialog", "GWR estimates"))
        self.initComboBox.setItemText(1, _translate("advDialog", "OLS estimates"))
        self.applyBTN.setText(_translate("advDialog", "Apply"))
        self.resetBTN.setText(_translate("advDialog", "Reset"))
        self.groupBox_3.setTitle(_translate("advDialog", "Convergence threshold"))
        self.convComboBox.setItemText(0, _translate("advDialog", "1e-5"))
        self.convComboBox.setItemText(1, _translate("advDialog", "1e-3"))
        self.SOCBox_2.setTitle(_translate("advDialog", "Variable standardization"))
        self.varSTDComboBox.setItemText(0, _translate("advDialog", "On"))
        self.varSTDComboBox.setItemText(1, _translate("advDialog", "Off"))
        self.groupBox_4.setTitle(_translate("advDialog", "Monte Carlo test for spatial variability"))
        self.mcComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.mcComboBox.setItemText(1, _translate("advDialog", "On (Very Slow)"))
        self.groupBox_5.setTitle(_translate("advDialog", "Local collinearity diagnostics"))
        self.locollinearComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.locollinearComboBox.setItemText(1, _translate("advDialog", "On"))
        self.groupBox_6.setTitle(_translate("advDialog", "Multiple comparison correction"))
        self.mccComboBox.setItemText(0, _translate("advDialog", "None"))
        self.mccComboBox.setItemText(1, _translate("advDialog", "Bonferroni"))
        self.mccComboBox.setItemText(2, _translate("advDialog", "Sidak"))
        self.mccComboBox.setItemText(3, _translate("advDialog", "FDR"))
    
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
        
        if self.soc == "SOC-f":
            self.SOCComboBox.setCurrentIndex(0)
        else:
            self.SOCComboBox.setCurrentIndex(1)

        if self.init == "GWR estimates":
            self.initComboBox.setCurrentIndex(0)
        else:
            self.initComboBox.setCurrentIndex(1)

        if self.converg == "1e-5":
            self.convComboBox.setCurrentIndex(0)
        else:
            self.convComboBox.setCurrentIndex(1)

        if self.mcc == "None":
            self.mccComboBox.setCurrentIndex(0)
        elif self.mcc == "Bonferroni":
            self.mccComboBox.setCurrentIndex(1)
        elif self.mcc == "Sidak":
            self.mccComboBox.setCurrentIndex(2)
        elif self.mcc == "FDR":
            self.mccComboBox.setCurrentIndex(3)


    def addActionsToUI(self):
        self.applyBTN.clicked.connect(self.applyOnClick)
        self.resetBTN.clicked.connect(self.resetOnClick)

    def applyOnClick(self):
        self.varSTD = self.varSTDComboBox.currentText()
        self.soc = self.SOCComboBox.currentText()
        self.init = self.initComboBox.currentText()
        self.converg = self.convComboBox.currentText()
        self.locollinear = self.locollinearComboBox.currentText()
        self.mcTest = self.mcComboBox.currentText()
        self.mcc = self.mccComboBox.currentText()
        
        self.advDialog.close()
    
    def resetOnClick(self):
        self.locollinearComboBox.setCurrentIndex(0)
        self.mcComboBox.setCurrentIndex(0)
        self.varSTDComboBox.setCurrentIndex(0)
        self.SOCComboBox.setCurrentIndex(0)
        self.initComboBox.setCurrentIndex(0)
        self.convComboBox.setCurrentIndex(0)
        self.mccComboBox.setCurrentIndex(0)


