# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
#_Author: Ziqi Li (liziqi1992@gmail.com)
#Generated using pyuic5 -x advOptMGWR.ui -o advOptMGWR.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_advDialog(object):
    def setupUi(self, advDialog):
        advDialog.setObjectName("advDialog")
        advDialog.setWindowModality(QtCore.Qt.WindowModal)
        advDialog.resize(369, 218)
        advDialog.setModal(True)
        self.SOCBox = QtWidgets.QGroupBox(advDialog)
        self.SOCBox.setGeometry(QtCore.QRect(10, 110, 221, 51))
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
        self.initComboBox.addItem("")
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setGeometry(QtCore.QRect(250, 20, 110, 32))
        self.applyBTN.setObjectName("applyBTN")
        self.cancelBTN = QtWidgets.QPushButton(advDialog)
        self.cancelBTN.setGeometry(QtCore.QRect(250, 60, 110, 32))
        self.cancelBTN.setObjectName("cancelBTN")
        self.groupBox_3 = QtWidgets.QGroupBox(advDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 221, 51))
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
		
		
        self.advDialog = advDialog
        self.varSTD = "On"
        self.soc = "SOC-f"
        self.init = "GWR estimates"
        self.converg = "1e-5"

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
        self.initComboBox.setItemText(2, _translate("advDialog", "None"))
        self.applyBTN.setText(_translate("advDialog", "Apply"))
        self.cancelBTN.setText(_translate("advDialog", "Cancel"))
        self.groupBox_3.setTitle(_translate("advDialog", "Convergence threshold"))
        self.convComboBox.setItemText(0, _translate("advDialog", "1e-5"))
        self.convComboBox.setItemText(1, _translate("advDialog", "1e-3"))
        self.SOCBox_2.setTitle(_translate("advDialog", "Variable standardization"))
        self.varSTDComboBox.setItemText(0, _translate("advDialog", "On"))
        self.varSTDComboBox.setItemText(1, _translate("advDialog", "Off"))

    
    def loadSettings(self):

        if self.varSTD == "On":
            self.varSTDComboBox.setCurrentIndex(0)
        else:
            self.varSTDComboBox.setCurrentIndex(1)
        
        if self.soc == "SOC-f":
            self.SOCComboBox.setCurrentIndex(0)
        else:
            self.SOCComboBox.setCurrentIndex(1)

        if self.init == "GWR estimates":
            self.SOCComboBox.setCurrentIndex(0)
        else:
            self.initComboBox.setCurrentIndex(1)

        if self.converg == "1e-5":
            self.convComboBox.setCurrentIndex(0)
        else:
            self.convComboBox.setCurrentIndex(1)


    def addActionsToUI(self):
        self.applyBTN.clicked.connect(self.applyOnClick)

    def applyOnClick(self):
        self.varSTD = self.varSTDComboBox.currentText()
        self.soc = self.SOCComboBox.currentText()
        self.init = self.initComboBox.currentText()
        self.converg = self.convComboBox.currentText()
        self.advDialog.close()


