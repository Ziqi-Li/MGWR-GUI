# -*- coding: utf-8 -*-
#_author: Ziqi Li (liziqi1992@gmail.com)
#Generated using pyuic5 -x gui.ui -o gui.py


import os,sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
from datetime import datetime
from pysal.contrib.gwr.gwr import GWR,MGWR
from pysal.contrib.gwr.sel_bw import Sel_BW
from pysal.contrib.glm.glm import GLM
import pyproj
from .summary import *
from .running_now import Ui_runningDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(763, 628)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(299, 0, 181, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.variableList = QtWidgets.QListWidget(self.groupBox_2)
        self.variableList.setGeometry(QtCore.QRect(10, 20, 161, 341))
        self.variableList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.variableList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variableList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.variableList.setDragEnabled(False)
        self.variableList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.variableList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.variableList.setResizeMode(QtWidgets.QListView.Fixed)
        self.variableList.setObjectName("variableList")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 0, 261, 371))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.removeY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeY.setObjectName("removeY")
        self.gridLayout.addWidget(self.removeY, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.OffsetLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.OffsetLabel.setEnabled(False)
        self.OffsetLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OffsetLabel.setObjectName("OffsetLabel")
        self.gridLayout.addWidget(self.OffsetLabel, 1, 3, 1, 1)
        self.addY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addY.setObjectName("addY")
        self.gridLayout.addWidget(self.addY, 0, 1, 1, 1)
        self.responseLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.responseLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.responseLabel.setReadOnly(True)
        self.responseLabel.setObjectName("responseLabel")
        self.gridLayout.addWidget(self.responseLabel, 0, 3, 1, 1)
        self.addOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addOffset.setObjectName("addOffset")
        self.gridLayout.addWidget(self.addOffset, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.removeOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeOffset.setObjectName("removeOffset")
        self.gridLayout.addWidget(self.removeOffset, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(68, 90, 181, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.localList = QtWidgets.QListWidget(self.groupBox_3)
        self.localList.setGeometry(QtCore.QRect(10, 20, 161, 241))
        self.localList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.localList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.localList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localList.setObjectName("localList")
        self.removeLocal = QtWidgets.QToolButton(self.groupBox_6)
        self.removeLocal.setGeometry(QtCore.QRect(9, 230, 23, 21))
        self.removeLocal.setObjectName("removeLocal")
        self.addLocal = QtWidgets.QToolButton(self.groupBox_6)
        self.addLocal.setGeometry(QtCore.QRect(40, 230, 23, 21))
        self.addLocal.setObjectName("addLocal")
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 210, 271, 41))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 205, 18))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isGWRRBTN.setEnabled(True)
        self.isGWRRBTN.setCheckable(True)
        self.isGWRRBTN.setChecked(False)
        self.isGWRRBTN.setObjectName("isGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isGWRRBTN)
        self.isMGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isMGWRRBTN.setChecked(True)
        self.isMGWRRBTN.setObjectName("isMGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isMGWRRBTN)
        self.kernelDropdownGrou = QtWidgets.QGroupBox(Dialog)
        self.kernelDropdownGrou.setGeometry(QtCore.QRect(10, 250, 271, 51))
        self.kernelDropdownGrou.setObjectName("kernelDropdownGrou")
        self.kernelDropdown = QtWidgets.QComboBox(self.kernelDropdownGrou)
        self.kernelDropdown.setGeometry(QtCore.QRect(10, 20, 241, 26))
        self.kernelDropdown.setObjectName("kernelDropdown")
        self.kernelDropdown.addItem("")
        self.kernelDropdown.addItem("")
        self.kernelDropdown.addItem("")
        self.kernelDropdown.addItem("")
        self.kernelDropdown.addItem("")
        self.kernelDropdown.addItem("")
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 271, 201))
        self.groupBox_9.setObjectName("groupBox_9")
        self.bwDropdown = QtWidgets.QComboBox(self.groupBox_9)
        self.bwDropdown.setGeometry(QtCore.QRect(10, 20, 241, 26))
        self.bwDropdown.setObjectName("bwDropdown")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_9)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 191, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.bwPreDefined = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwPreDefined.setEnabled(False)
        self.bwPreDefined.setObjectName("bwPreDefined")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bwPreDefined)
        self.bwMin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMin.setEnabled(False)
        self.bwMin.setObjectName("bwMin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bwMin)
        self.bwMax = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMax.setEnabled(False)
        self.bwMax.setObjectName("bwMax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bwMax)
        self.bwInterval = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwInterval.setEnabled(False)
        self.bwInterval.setObjectName("bwInterval")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bwInterval)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 50, 271, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 205, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isPrjCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isPrjCoorRBTN.setChecked(True)
        self.isPrjCoorRBTN.setObjectName("isPrjCoorRBTN")
        self.horizontalLayout.addWidget(self.isPrjCoorRBTN)
        self.isSphCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isSphCoorRBTN.setObjectName("isSphCoorRBTN")
        self.horizontalLayout.addWidget(self.isSphCoorRBTN)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 261, 101))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.removeYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeYCoor.setObjectName("removeYCoor")
        self.gridLayout_4.addWidget(self.removeYCoor, 2, 3, 1, 1)
        self.addID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addID.setObjectName("addID")
        self.gridLayout_4.addWidget(self.addID, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.idLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.idLabel.setText("")
        self.idLabel.setDragEnabled(True)
        self.idLabel.setReadOnly(True)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout_4.addWidget(self.idLabel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.yCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.yCoorLabel.setReadOnly(True)
        self.yCoorLabel.setObjectName("yCoorLabel")
        self.gridLayout_4.addWidget(self.yCoorLabel, 2, 1, 1, 1)
        self.addXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addXCoor.setObjectName("addXCoor")
        self.gridLayout_4.addWidget(self.addXCoor, 1, 2, 1, 1)
        self.removeXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeXCoor.setObjectName("removeXCoor")
        self.gridLayout_4.addWidget(self.removeXCoor, 1, 3, 1, 1)
        self.addYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addYCoor.setObjectName("addYCoor")
        self.gridLayout_4.addWidget(self.addYCoor, 2, 2, 1, 1)
        self.xCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.xCoorLabel.setReadOnly(True)
        self.xCoorLabel.setObjectName("xCoorLabel")
        self.gridLayout_4.addWidget(self.xCoorLabel, 1, 1, 1, 1)
        self.removeID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeID.setObjectName("removeID")
        self.gridLayout_4.addWidget(self.removeID, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 271, 51))
        self.groupBox.setObjectName("groupBox")
        self.openDataBTN = QtWidgets.QToolButton(self.groupBox)
        self.openDataBTN.setGeometry(QtCore.QRect(240, 20, 26, 21))
        self.openDataBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.openDataBTN.setObjectName("openDataBTN")
        self.openDataPath = QtWidgets.QLineEdit(self.groupBox)
        self.openDataPath.setGeometry(QtCore.QRect(11, 21, 221, 21))
        self.openDataPath.setObjectName("openDataPath")
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(300, 370, 451, 131))
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_10)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 431, 101))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_11 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_11.setObjectName("groupBox_11")
        self.optimCriDropdown = QtWidgets.QComboBox(self.groupBox_11)
        self.optimCriDropdown.setGeometry(QtCore.QRect(10, 20, 161, 26))
        self.optimCriDropdown.setObjectName("optimCriDropdown")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_11, 0, 2, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_12.setObjectName("groupBox_12")
        self.modelTypeDropdown = QtWidgets.QComboBox(self.groupBox_12)
        self.modelTypeDropdown.setGeometry(QtCore.QRect(10, 20, 161, 26))
        self.modelTypeDropdown.setObjectName("modelTypeDropdown")
        self.modelTypeDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_15.setObjectName("groupBox_15")
        self.initDropDown = QtWidgets.QComboBox(self.groupBox_15)
        self.initDropDown.setGeometry(QtCore.QRect(10, 20, 161, 26))
        self.initDropDown.setObjectName("initDropDown")
        self.initDropDown.addItem("")
        self.initDropDown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_15, 1, 1, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_14.setObjectName("groupBox_14")
        self.SOCDropdown = QtWidgets.QComboBox(self.groupBox_14)
        self.SOCDropdown.setGeometry(QtCore.QRect(10, 20, 161, 26))
        self.SOCDropdown.setObjectName("SOCDropdown")
        self.SOCDropdown.addItem("")
        self.SOCDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_14, 1, 2, 1, 1)
        self.runBTN = QtWidgets.QPushButton(Dialog)
        self.runBTN.setGeometry(QtCore.QRect(580, 530, 151, 71))
        self.runBTN.setObjectName("runBTN")
        self.groupBox_13 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 500, 531, 121))
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_13)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 511, 91))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sumFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.sumFileSavePath.setReadOnly(True)
        self.sumFileSavePath.setObjectName("sumFileSavePath")
        self.gridLayout_3.addWidget(self.sumFileSavePath, 0, 1, 1, 1)
        self.betaFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.betaFileSavePath.setReadOnly(True)
        self.betaFileSavePath.setObjectName("betaFileSavePath")
        self.gridLayout_3.addWidget(self.betaFileSavePath, 1, 1, 1, 1)
        self.saveBetasBTN = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.saveBetasBTN.setObjectName("saveBetasBTN")
        self.gridLayout_3.addWidget(self.saveBetasBTN, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.saveSumBTN = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.saveSumBTN.setObjectName("saveSumBTN")
        self.gridLayout_3.addWidget(self.saveSumBTN, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.processFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.processFileSavePath.setReadOnly(True)
        self.processFileSavePath.setObjectName("processFileSavePath")
        self.gridLayout_3.addWidget(self.processFileSavePath, 2, 1, 1, 1)
        self.saveProcessBTN = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.saveProcessBTN.setObjectName("saveProcessBTN")
        self.gridLayout_3.addWidget(self.saveProcessBTN, 2, 2, 1, 1)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MGWR"))
        self.groupBox_2.setTitle(_translate("Dialog", "Variable List"))
        self.groupBox_6.setTitle(_translate("Dialog", "Regression Variables"))
        self.removeY.setText(_translate("Dialog", "<"))
        self.label_5.setText(_translate("Dialog", "Offset"))
        self.addY.setText(_translate("Dialog", ">"))
        self.addOffset.setText(_translate("Dialog", ">"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.removeOffset.setText(_translate("Dialog", "<"))
        self.groupBox_3.setTitle(_translate("Dialog", "Local"))
        self.removeLocal.setText(_translate("Dialog", "<"))
        self.addLocal.setText(_translate("Dialog", ">"))
        self.groupBox_7.setTitle(_translate("Dialog", "GWR Mode"))
        self.isGWRRBTN.setText(_translate("Dialog", "GWR"))
        self.isMGWRRBTN.setText(_translate("Dialog", "MGWR"))
        self.kernelDropdownGrou.setTitle(_translate("Dialog", "Kernel"))
        self.kernelDropdown.setItemText(0, _translate("Dialog", "Adaptive Bisquare"))
        self.kernelDropdown.setItemText(1, _translate("Dialog", "Adaptive Gaussian"))
        self.kernelDropdown.setItemText(2, _translate("Dialog", "Adaptive Exponential"))
        self.kernelDropdown.setItemText(3, _translate("Dialog", "Fixed Bisquare"))
        self.kernelDropdown.setItemText(4, _translate("Dialog", "Fixed Gaussian"))
        self.kernelDropdown.setItemText(5, _translate("Dialog", "Fixed Exponential"))
        self.groupBox_9.setTitle(_translate("Dialog", "Bandwidth"))
        self.bwDropdown.setItemText(0, _translate("Dialog", "Golden Section"))
        self.bwDropdown.setItemText(1, _translate("Dialog", "Interval Search"))
        self.bwDropdown.setItemText(2, _translate("Dialog", "Pre-defiend bandwidth"))
        self.label_6.setText(_translate("Dialog", "Defined"))
        self.label_9.setText(_translate("Dialog", "Min"))
        self.label_10.setText(_translate("Dialog", "Max"))
        self.label_11.setText(_translate("Dialog", "Interval"))
        self.groupBox_4.setTitle(_translate("Dialog", "Location Variables"))
        self.isPrjCoorRBTN.setText(_translate("Dialog", "Projected"))
        self.isSphCoorRBTN.setText(_translate("Dialog", "Spherical"))
        self.removeYCoor.setText(_translate("Dialog", ">"))
        self.addID.setText(_translate("Dialog", "<"))
        self.label_3.setText(_translate("Dialog", "Y"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "X"))
        self.addXCoor.setText(_translate("Dialog", "<"))
        self.removeXCoor.setText(_translate("Dialog", ">"))
        self.addYCoor.setText(_translate("Dialog", "<"))
        self.removeID.setText(_translate("Dialog", ">"))
        self.groupBox.setTitle(_translate("Dialog", "Data Files"))
        self.openDataBTN.setText(_translate("Dialog", "..."))
        self.groupBox_10.setTitle(_translate("Dialog", "Model Options"))
        self.groupBox_11.setTitle(_translate("Dialog", "Optimization Criterion"))
        self.optimCriDropdown.setItemText(0, _translate("Dialog", "AICc"))
        self.optimCriDropdown.setItemText(1, _translate("Dialog", "AIC"))
        self.optimCriDropdown.setItemText(2, _translate("Dialog", "BIC"))
        self.optimCriDropdown.setItemText(3, _translate("Dialog", "CV"))
        self.groupBox_12.setTitle(_translate("Dialog", "Model Type"))
        self.modelTypeDropdown.setItemText(0, _translate("Dialog", "Gaussian"))
        self.groupBox_15.setTitle(_translate("Dialog", "Initialization"))
        self.initDropDown.setItemText(0, _translate("Dialog", "GWR estimates"))
        self.initDropDown.setItemText(1, _translate("Dialog", "OLS estimates"))
        self.groupBox_14.setTitle(_translate("Dialog", "Measure of Score of Change"))
        self.SOCDropdown.setItemText(0, _translate("Dialog", "SOC-f"))
        self.SOCDropdown.setItemText(1, _translate("Dialog", "SOC-RSS"))
        self.runBTN.setText(_translate("Dialog", "Run"))
        self.groupBox_13.setTitle(_translate("Dialog", "Outputs"))
        self.saveBetasBTN.setText(_translate("Dialog", "..."))
        self.label_8.setText(_translate("Dialog", "Local Estimate File"))
        self.label_7.setText(_translate("Dialog", "Summary File"))
        self.saveSumBTN.setText(_translate("Dialog", "..."))
        self.label_12.setText(_translate("Dialog", "Calibration Process File"))
        self.saveProcessBTN.setText(_translate("Dialog", "..."))


    def addActionsToUI(self):
        self.openDataBTN.clicked.connect(self.openData)
        self.saveSumBTN.clicked.connect(lambda:self.getSaveFile(0))
        self.saveBetasBTN.clicked.connect(lambda:self.getSaveFile(1))
        self.saveProcessBTN.clicked.connect(lambda:self.getSaveFile(2))
        
        self.addID.clicked.connect(lambda: self.addVariable(self.idLabel))
        self.removeID.clicked.connect(lambda: self.removeVariable(self.idLabel))
        
        self.addXCoor.clicked.connect(lambda: self.addVariable(self.xCoorLabel))
        self.removeXCoor.clicked.connect(lambda: self.removeVariable(self.xCoorLabel))
        
        self.addYCoor.clicked.connect(lambda: self.addVariable(self.yCoorLabel))
        self.removeYCoor.clicked.connect(lambda: self.removeVariable(self.yCoorLabel))
        
        self.addY.clicked.connect(lambda: self.addVariable(self.responseLabel))
        self.removeY.clicked.connect(lambda: self.removeVariable(self.responseLabel))
    
        self.addLocal.clicked.connect(self.addVarToLocal)
        self.removeLocal.clicked.connect(self.removeVarFromLocal)
    
        self.runBTN.clicked.connect(self.runGWR)
        
        self.openDataPath.textChanged.connect(lambda: self.removeRed(self.openDataPath))
        self.sumFileSavePath.textChanged.connect(lambda: self.removeRed(self.sumFileSavePath))
        self.betaFileSavePath.textChanged.connect(lambda: self.removeRed(self.betaFileSavePath))
        self.betaFileSavePath.textChanged.connect(lambda: self.removeRed(self.processFileSavePath))
        
        self.responseLabel.textChanged.connect(lambda: self.removeRed(self.responseLabel))
        self.xCoorLabel.textChanged.connect(lambda: self.removeRed(self.xCoorLabel))
        self.yCoorLabel.textChanged.connect(lambda: self.removeRed(self.yCoorLabel))
        self.idLabel.textChanged.connect(lambda: self.removeRed(self.idLabel))
        
        
    
        if self.bwDropdown.currentText() == "Golden Section":
            self.bwMin.setEnabled(False)
            self.bwMax.setEnabled(False)
            self.bwInterval.setEnabled(False)
            self.bwPreDefined.setEnabled(False)
        
        elif self.bwDropdown.currentText() == "Interval":
            self.bwMin.setEnabled(True)
            self.bwMax.setEnabled(True)
            self.bwInterval.setEnabled(True)
        else:
            self.bwPreDefined.setEnabled(True)
            self.bwMin.setEnabled(False)
            self.bwMax.setEnabled(False)
            self.bwInterval.setEnabled(False)

    
    def openData(self):
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))
        try:
            fileName,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile',self.path,"CSV (*.csv)")
            if fileName:
                self.openDataPath.setText(fileName)
                self.data = pd.read_csv(fileName)
                fields = pd.read_csv(fileName, nrows=1).columns.values.tolist()
                self.localList.clear()
                self.localList.addItem('Intercept')
                self.variableList.clear()
                self.idLabel.clear()
                self.xCoorLabel.clear()
                self.yCoorLabel.clear()
                self.responseLabel.clear()
                self.variableList.addItems(fields)
    
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Something went wrong when openning data. Please double check.')
            error_dialog.exec_()


    def addVariable(self,destination):
        print(destination.text())
        if destination.text() and self.variableList.selectedItems():
            self.variableList.addItem(destination.text())
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(self.variableList.row(self.variableList.selectedItems()[0]))
            item = None
        elif not destination.text() and self.variableList.selectedItems():
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(self.variableList.row(self.variableList.selectedItems()[0]))
            item = None

    def removeVariable(self,origin):
        if origin.text():
            item = self.variableList.addItem(origin.text())
            origin.setText("")

    def addVarToLocal(self):
        for item in self.variableList.selectedItems():
            self.localList.addItem(item.text())
            noneItem = self.variableList.takeItem(self.variableList.row(item))
            noneItem = None
            self.localList.setStyleSheet("QListWidget{border: 0px solid red;}")

    def removeVarFromLocal(self):
        for item in self.localList.selectedItems():
            self.variableList.addItem(item.text())
            noneItem = self.localList.takeItem(self.localList.row(item))
            noneItem = None

    def removeRed(self,lineEdit):
        lineEdit.setStyleSheet("border: 0px solid red;")

    #Get 3 Save Paths for control, summary and betas
    def getSaveFile(self,ext):
        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(None, 'SaveFile',os.path.join(os.path.dirname(self.path),'MGWR_session'))
        if fileName:
            if ext == 0:
                self.sumFileSavePath.setText(fileName+'_summary.txt')
                self.betaFileSavePath.setText(fileName + '_betas.csv')
                self.processFileSavePath.setText(fileName + '_process.csv')
            if ext == 1:
                self.betaFileSavePath.setText(fileName + '_betas.csv')
            if ext == 2:
                self.processFileSavePath.setText(fileName + '_process.csv')

    
    
    #Getting all data for running model
    def preCheckEmptyFields(self):
        allSet = True
        if not self.openDataPath.text():
            self.openDataPath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.sumFileSavePath.text():
            self.sumFileSavePath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.betaFileSavePath.text():
            self.betaFileSavePath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.processFileSavePath.text():
            self.processFileSavePath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.responseLabel.text():
            self.responseLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.idLabel.text():
            self.idLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.xCoorLabel.text():
            self.xCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.yCoorLabel.text():
            self.yCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.localList.count():
            self.localList.setStyleSheet("QListWidget{border: 2px solid red;}")
        
        
        return allSet

            
    def loadDataModel(self):
        if 1==1:
        #Load Variables
            self.id = self.data[[self.idLabel.text()]].as_matrix().reshape(-1,1)
            self.data['Intercept'] = 1
            self.y = self.data[[self.responseLabel.text()]].as_matrix().reshape(-1,1)
            self.yName = self.responseLabel.text()
            self.XNames =  [str(self.localList.item(i).text()) for i in range(self.localList.count())]
            self.X = self.data[self.XNames].as_matrix()
            self.xCoor = self.data[[self.xCoorLabel.text()]].ix[:,0]
            self.yCoor = self.data[[self.yCoorLabel.text()]].ix[:,0]
            self.nObs = len(self.data.index)
            
            if self.isPrjCoorRBTN.isChecked():
                self.coorType = 'Projected'
                self.coords = list(zip(self.xCoor,self.yCoor))
            if self.isSphCoorRBTN.isChecked():
                self.coorType = 'Spherical'
                wgs84=pyproj.Proj("+init=EPSG:4326")
                web=pyproj.Proj("+init=EPSG:3857")
                xx, yy = pyproj.transform(wgs84, web, self.xCoor.tolist(), self.yCoor.tolist())
                self.coords = list(zip(xx,yy))
        
    
            #Load Model Options:
            self.search = 'golden_section'
            self.fixed = (str.split(self.kernelDropdown.currentText())[0] == "Fixed")
            self.kernel = str.split(self.kernelDropdown.currentText())[1].lower()
            print(self.kernel)
            self.criterion = self.optimCriDropdown.currentText()
            self.isGWR = self.isGWRRBTN.isChecked()
            self.isMGWR = self.isMGWRRBTN.isChecked()
            self.isRss_score = True
            self.tol_multi = 1e-05
            self.tol_gwr = 1e-05
        
            self.init_multi = (self.initDropDown.currentText() == 'GWR estimates')
            self.isRss_score = (self.SOCDropdown.currentText() == 'SOC-RSS')
        
        
        #except:
        #return False
        return True
        


    #Run model
    def runGWR(self):
        w = QtWidgets.QDialog()
        nd = Ui_runningDialog()
        nd.setupUi(w)
        w.show()
        if not self.preCheckEmptyFields():
            err_msg = QtWidgets.QMessageBox.critical(None, "Error", "Please fix inputs in red!")

            return
        
        if not self.loadDataModel():
            err_msg = QtWidgets.QMessageBox.critical(None, "Error", "Something wrong when loading variables to model. Please double check you data. No Missing values allowed.")
            return


        self.begin_t = datetime.now()
        
        if self.isGWR:
            self.GLMResult = GLM(self.y,self.X).fit()
            
            print ("running GWR")
            
            self.bw = Sel_BW(self.coords, self.y, self.X, kernel=self.kernel, fixed=self.fixed, constant = False)
            self.bw = self.bw.search(search=self.search, criterion=self.criterion)
                
            self.results = GWR(self.coords, self.y, self.X, self.bw, fixed=self.fixed, kernel=self.kernel, constant = False).fit()
            self.saveBetasToCSVGWR(self.results)
            self.end_t = datetime.now()
            summaryGWR(self)
            print ("Done")
            msg = QtWidgets.QMessageBox.information(None, "Success", "Running complete!")
            
            """
            try:
                '''
                __init__(self, coords, y, X_loc, X_glob=None, family=Gaussian(),
                offset=None, kernel='bisquare', fixed=False, multi=False, constant=True)
                '''
                bw = Sel_BW(self.coords, self.y, self.X, kernel=self.kernel, fixed=self.fixed, constant = False)
            
                '''
                search(self, search='golden_section', criterion='AICc', bw_min=0.0,
                bw_max=0.0, interval=0.0, tol=1.0e-6, max_iter=200, init_multi=True,
                tol_multi=1.0e-5, rss_score=False, max_iter_multi=200)
                    '''
                bw = bw.search(search=self.search, criterion=self.criterion)
            
                self.results = GWR(self.coords, self.y, self.X, bw, fixed=self.fixed, kernel=self.kernel, constant = False).fit()
                self.saveBetasToCSVGWR(self.results)
                self.end_t = datetime.now()
                summaryGWR(self)
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Something went wrong when running GWR Model. Please double check your settings and data.')
                error_dialog.exec_()
            """
        
        if self.isMGWR:
            if 1==1:
                print ("running MGWR")
                self.bw = Sel_BW(self.coords, self.y, self.X, fixed=self.fixed,kernel=self.kernel, multi=True,constant = False)
                self.bws = self.bw.search(search='golden_section',criterion=self.criterion,tol_multi=self.tol_multi,init_multi=self.init_multi, rss_score=self.isRss_score)
                XB = self.bw.XB
                err = self.bw.err
                self.results = MGWR(self.coords, self.y, self.X, self.bws, XB, err, kernel=self.kernel, fixed=self.fixed,constant=False).fit()
                self.saveBetasToCSVMGWR(self.results)
                self.saveProcessToCSVMGWR()
                self.end_t = datetime.now()
                summaryMGWR(self)
                print ("Done")
                msg = QtWidgets.QMessageBox.information(None, "Success", "Running complete!")
                #except:
#err_msg = QtWidgets.QMessageBox.critical(None, 'Error', 'Something went wrong when running MGWR Model. Please double check your settings and data.')
            


    def saveProcessToCSVMGWR(self):
        bw = self.bw
        processDF = pd.concat([pd.DataFrame(bw.bw[1]), pd.DataFrame(bw.bw[2]),pd.DataFrame(bw.bw[3])], axis=1)
        processDF.columns = ['bw_'+ x for x in self.XNames] + [self.criterion +'_'+ x for x in self.XNames] + [self.SOCDropdown.currentText()]
        processDF.to_csv(self.processFileSavePath.text(),sep=',',index=True)

    def saveBetasToCSVMGWR(self,results):
        resultsDF = pd.DataFrame(np.column_stack((self.id,self.xCoor,self.yCoor,self.y,results.predy,results.resid_response,results.params)))
        resultsDF.columns = ['GeoID','x_coor','y_coor','y','yhat','residual'] + ['beta_'+ x for x in self.XNames]
        resultsDF.to_csv(self.betaFileSavePath.text(),sep=',',index=False)
    
    def saveBetasToCSVGWR(self,results):
        resultsDF = pd.DataFrame(np.column_stack((self.id,self.xCoor,self.yCoor,self.y,results.predy,results.resid_response,results.localR2, results.influ,results.cooksD,results.params,results.bse,results.tvalues)))
        resultsDF.columns = ['GeoID','x_coor','y_coor','y','yhat','residual','localR2','influ','CooksD'] + ['beta_'+ x for x in self.XNames] + ['se_'+ x for x in self.XNames] + ['t_'+ x for x in self.XNames]
        resultsDF.to_csv(self.betaFileSavePath.text(),sep=',',index=False)

