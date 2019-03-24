# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advOptGWR.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_advGWRDialog(object):
    def setupUi(self, advDialog):
        advDialog.setObjectName("advDialog")
        advDialog.setWindowModality(QtCore.Qt.WindowModal)
        advDialog.resize(401, 200)
        advDialog.setMinimumSize(QtCore.QSize(370, 200))
        advDialog.setModal(True)
        self.gridLayout_6 = QtWidgets.QGridLayout(advDialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SOCBox_2 = QtWidgets.QGroupBox(advDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SOCBox_2.sizePolicy().hasHeightForWidth())
        self.SOCBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SOCBox_2.setFont(font)
        self.SOCBox_2.setObjectName("SOCBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SOCBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.varSTDComboBox = QtWidgets.QComboBox(self.SOCBox_2)
        self.varSTDComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.varSTDComboBox.setFont(font)
        self.varSTDComboBox.setObjectName("varSTDComboBox")
        self.varSTDComboBox.addItem("")
        self.varSTDComboBox.addItem("")
        self.gridLayout_2.addWidget(self.varSTDComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.SOCBox_2, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(advDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.locollinearComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.locollinearComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.locollinearComboBox.setFont(font)
        self.locollinearComboBox.setObjectName("locollinearComboBox")
        self.locollinearComboBox.addItem("")
        self.locollinearComboBox.addItem("")
        self.gridLayout_4.addWidget(self.locollinearComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.resetBTN = QtWidgets.QPushButton(advDialog)
        self.resetBTN.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.resetBTN.setFont(font)
        self.resetBTN.setObjectName("resetBTN")
        self.gridLayout.addWidget(self.resetBTN, 1, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(advDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mcComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.mcComboBox.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mcComboBox.setFont(font)
        self.mcComboBox.setObjectName("mcComboBox")
        self.mcComboBox.addItem("")
        self.mcComboBox.addItem("")
        self.gridLayout_3.addWidget(self.mcComboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.applyBTN = QtWidgets.QPushButton(advDialog)
        self.applyBTN.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.applyBTN.setFont(font)
        self.applyBTN.setObjectName("applyBTN")
        self.gridLayout.addWidget(self.applyBTN, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.advDialog = advDialog
        self.mcTest = "Off"
        self.varSTD = "On"
        self.locollinear = "Off"
        #self.mcc = "None"

        self.retranslateUi(advDialog)
        QtCore.QMetaObject.connectSlotsByName(advDialog)

    def retranslateUi(self, advDialog):
        _translate = QtCore.QCoreApplication.translate
        advDialog.setWindowTitle(_translate("advDialog", "Advanced Options"))
        self.SOCBox_2.setTitle(
            _translate("advDialog", "Variable standardization"))
        self.varSTDComboBox.setItemText(0, _translate("advDialog", "On"))
        self.varSTDComboBox.setItemText(1, _translate("advDialog", "Off"))
        self.groupBox_5.setTitle(
            _translate("advDialog", "Local collinearity diagnostics"))
        self.locollinearComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.locollinearComboBox.setItemText(1, _translate("advDialog", "On"))
        self.resetBTN.setText(_translate("advDialog", "Reset"))
        self.groupBox_4.setTitle(
            _translate("advDialog",
                       "Monte Carlo test for spatial variability"))
        self.mcComboBox.setItemText(0, _translate("advDialog", "Off"))
        self.mcComboBox.setItemText(1, _translate("advDialog",
                                                  "On (Very Slow)"))
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
        #self.mcc = self.mccComboBox.currentText()
        self.advDialog.close()

    def resetOnClick(self):
        self.varSTDComboBox.setCurrentIndex(0)
        self.locollinearComboBox.setCurrentIndex(0)
        self.mcComboBox.setCurrentIndex(0)
        #self.mccComboBox.setCurrentIndex(0)
