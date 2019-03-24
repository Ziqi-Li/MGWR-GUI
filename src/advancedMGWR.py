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
        advDialog.resize(457, 253)
        advDialog.setModal(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(advDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SOCBox = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SOCBox.setFont(font)
        self.SOCBox.setObjectName("SOCBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.SOCBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SOCComboBox = QtWidgets.QComboBox(self.SOCBox)
        self.SOCComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SOCComboBox.setFont(font)
        self.SOCComboBox.setObjectName("SOCComboBox")
        self.SOCComboBox.addItem("")
        self.SOCComboBox.addItem("")
        self.gridLayout_5.addWidget(self.SOCComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.SOCBox, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.mcComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.mcComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mcComboBox.setFont(font)
        self.mcComboBox.setObjectName("mcComboBox")
        self.mcComboBox.addItem("")
        self.mcComboBox.addItem("")
        self.gridLayout_8.addWidget(self.mcComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.initComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.initComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.initComboBox.setFont(font)
        self.initComboBox.setObjectName("initComboBox")
        self.initComboBox.addItem("")
        self.initComboBox.addItem("")
        self.gridLayout_6.addWidget(self.initComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.convComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.convComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.convComboBox.setFont(font)
        self.convComboBox.setObjectName("convComboBox")
        self.convComboBox.addItem("")
        self.convComboBox.addItem("")
        self.gridLayout_7.addWidget(self.convComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.SOCBox_2 = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SOCBox_2.setFont(font)
        self.SOCBox_2.setObjectName("SOCBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.SOCBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.varSTDComboBox = QtWidgets.QComboBox(self.SOCBox_2)
        self.varSTDComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.varSTDComboBox.setFont(font)
        self.varSTDComboBox.setObjectName("varSTDComboBox")
        self.varSTDComboBox.addItem("")
        self.varSTDComboBox.addItem("")
        self.gridLayout_4.addWidget(self.varSTDComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.SOCBox_2, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(advDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.locollinearComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.locollinearComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.locollinearComboBox.setFont(font)
        self.locollinearComboBox.setObjectName("locollinearComboBox")
        self.locollinearComboBox.addItem("")
        self.locollinearComboBox.addItem("")
        self.gridLayout_9.addWidget(self.locollinearComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.resetBTN = QtWidgets.QPushButton(advDialog)
        self.resetBTN.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.resetBTN.setFont(font)
        self.resetBTN.setObjectName("resetBTN")
        self.gridLayout_2.addWidget(self.resetBTN, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.applyBTN.setFont(font)
        self.applyBTN.setObjectName("applyBTN")
        self.gridLayout.addWidget(self.applyBTN, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.advDialog = advDialog
        self.varSTD = "On"
        self.mcTest = "Off"
        self.locollinear = "Off"
        self.soc = "SOC-f"
        self.init = "GWR estimates"
        self.converg = "1e-5"
        #self.mcc = "None"

        self.retranslateUi(advDialog)
        QtCore.QMetaObject.connectSlotsByName(advDialog)

    def retranslateUi(self, advDialog):
        _translate = QtCore.QCoreApplication.translate
        advDialog.setWindowTitle(_translate("advDialog", "Advanced Options"))
        self.SOCBox.setTitle(
            _translate("advDialog", "Measure of Score of Change (SOC)"))
        self.SOCComboBox.setItemText(0, _translate("advDialog", "SOC-f"))
        self.SOCComboBox.setItemText(1, _translate("advDialog", "SOC-RSS"))
        self.groupBox_4.setTitle(
            _translate("advDialog",
                       "Monte Carlo test for spatial variability"))
        self.mcComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.mcComboBox.setItemText(1, _translate("advDialog",
                                                  "On (Very Slow)"))
        self.groupBox_2.setTitle(_translate("advDialog", "Initialization"))
        self.initComboBox.setItemText(0,
                                      _translate("advDialog", "GWR estimates"))
        self.initComboBox.setItemText(1,
                                      _translate("advDialog", "OLS estimates"))
        self.groupBox_3.setTitle(
            _translate("advDialog", "Convergence threshold"))
        self.convComboBox.setItemText(0, _translate("advDialog", "1e-5"))
        self.convComboBox.setItemText(1, _translate("advDialog", "1e-3"))
        self.SOCBox_2.setTitle(
            _translate("advDialog", "Variable standardization"))
        self.varSTDComboBox.setItemText(0, _translate("advDialog", "On"))
        self.varSTDComboBox.setItemText(1, _translate("advDialog", "Off"))
        self.groupBox_5.setTitle(
            _translate("advDialog", "Local collinearity diagnostics"))
        self.locollinearComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.locollinearComboBox.setItemText(1, _translate("advDialog", "On"))
        self.resetBTN.setText(_translate("advDialog", "Reset"))
        self.applyBTN.setText(_translate("advDialog", "Apply"))

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
        self.soc = self.SOCComboBox.currentText()
        self.init = self.initComboBox.currentText()
        self.converg = self.convComboBox.currentText()
        self.locollinear = self.locollinearComboBox.currentText()
        self.mcTest = self.mcComboBox.currentText()
        #self.mcc = self.mccComboBox.currentText()

        self.advDialog.close()

    def resetOnClick(self):
        self.locollinearComboBox.setCurrentIndex(0)
        self.mcComboBox.setCurrentIndex(0)
        self.varSTDComboBox.setCurrentIndex(0)
        self.SOCComboBox.setCurrentIndex(0)
        self.initComboBox.setCurrentIndex(0)
        self.convComboBox.setCurrentIndex(0)
        #self.mccComboBox.setCurrentIndex(0)
