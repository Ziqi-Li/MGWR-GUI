# -*- coding: utf-8 -*-
#_Author: Ziqi Li (liziqi1992@gmail.com)
#Generated using pyuic5 -x gui.ui -o gui.py

import os, sys

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
from simpledbf import Dbf5
from datetime import datetime
from mgwrlib.mgwr.gwr import GWR, MGWR
from mgwrlib.mgwr.sel_bw import Sel_BW
from spglm.glm import GLM
from spglm.family import Gaussian, Binomial, Poisson
from .outputs import *
from .loader import Ui_runningDialog
from .advancedMGWR import Ui_advMGWRDialog
from .advancedGWR import Ui_advGWRDialog
from .summaryGUI import Ui_summaryDlg
import multiprocessing as mp
#from .map import *
from time import sleep
import logging
import psutil
from io import StringIO

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, pool=None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 600)
        Dialog.setMaximumSize(QtCore.QSize(2000, 1600))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setWhatsThis("")
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setLocale(
            QtCore.QLocale(QtCore.QLocale.English,
                           QtCore.QLocale.UnitedStates))
        self.gridLayout_8 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.variableList = QtWidgets.QListWidget(self.groupBox_2)
        self.variableList.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.variableList.setFont(font)
        self.variableList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.variableList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variableList.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.variableList.setDragEnabled(False)
        self.variableList.setDragDropMode(
            QtWidgets.QAbstractItemView.NoDragDrop)
        self.variableList.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.variableList.setResizeMode(QtWidgets.QListView.Fixed)
        self.variableList.setObjectName("variableList")
        self.gridLayout_12.addWidget(self.variableList, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 5, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.removeY = QtWidgets.QToolButton(self.groupBox_6)
        self.removeY.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeY.setFont(font)
        self.removeY.setObjectName("removeY")
        self.gridLayout.addWidget(self.removeY, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.OffsetLabel = QtWidgets.QLineEdit(self.groupBox_6)
        self.OffsetLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.OffsetLabel.setFont(font)
        self.OffsetLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OffsetLabel.setObjectName("OffsetLabel")
        self.gridLayout.addWidget(self.OffsetLabel, 1, 3, 1, 1)
        self.addY = QtWidgets.QToolButton(self.groupBox_6)
        self.addY.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addY.setFont(font)
        self.addY.setObjectName("addY")
        self.gridLayout.addWidget(self.addY, 0, 1, 1, 1)
        self.responseLabel = QtWidgets.QLineEdit(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.responseLabel.setFont(font)
        self.responseLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.responseLabel.setReadOnly(True)
        self.responseLabel.setObjectName("responseLabel")
        self.gridLayout.addWidget(self.responseLabel, 0, 3, 1, 1)
        self.addOffset = QtWidgets.QToolButton(self.groupBox_6)
        self.addOffset.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addOffset.setFont(font)
        self.addOffset.setObjectName("addOffset")
        self.gridLayout.addWidget(self.addOffset, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.removeOffset = QtWidgets.QToolButton(self.groupBox_6)
        self.removeOffset.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeOffset.setFont(font)
        self.removeOffset.setObjectName("removeOffset")
        self.gridLayout.addWidget(self.removeOffset, 1, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.removeLocal = QtWidgets.QToolButton(self.groupBox_6)
        self.removeLocal.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeLocal.setFont(font)
        self.removeLocal.setObjectName("removeLocal")
        self.horizontalLayout_5.addWidget(self.removeLocal)
        self.addLocal = QtWidgets.QToolButton(self.groupBox_6)
        self.addLocal.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addLocal.setFont(font)
        self.addLocal.setObjectName("addLocal")
        self.horizontalLayout_5.addWidget(self.addLocal)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.localList = QtWidgets.QListWidget(self.groupBox_3)
        self.localList.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.localList.setFont(font)
        self.localList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.localList.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.localList.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localList.setObjectName("localList")
        self.gridLayout_15.addWidget(self.localList, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.gridLayout_14.setColumnStretch(1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 2, 5, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.removeYCoor = QtWidgets.QToolButton(self.groupBox_4)
        self.removeYCoor.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeYCoor.setFont(font)
        self.removeYCoor.setObjectName("removeYCoor")
        self.gridLayout_4.addWidget(self.removeYCoor, 2, 3, 1, 1)
        self.addID = QtWidgets.QToolButton(self.groupBox_4)
        self.addID.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addID.setFont(font)
        self.addID.setObjectName("addID")
        self.gridLayout_4.addWidget(self.addID, 0, 2, 1, 1)
        self.label_Y = QtWidgets.QLabel(self.groupBox_4)
        self.label_Y.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName("label_Y")
        self.gridLayout_4.addWidget(self.label_Y, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.idLabel = QtWidgets.QLineEdit(self.groupBox_4)
        self.idLabel.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.idLabel.setFont(font)
        self.idLabel.setText("")
        self.idLabel.setPlaceholderText("(optional)")
        self.idLabel.setDragEnabled(True)
        self.idLabel.setReadOnly(True)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout_4.addWidget(self.idLabel, 0, 1, 1, 1)
        self.label_X = QtWidgets.QLabel(self.groupBox_4)
        self.label_X.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_X.setFont(font)
        self.label_X.setObjectName("label_X")
        self.gridLayout_4.addWidget(self.label_X, 1, 0, 1, 1)
        self.yCoorLabel = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.yCoorLabel.setFont(font)
        self.yCoorLabel.setReadOnly(True)
        self.yCoorLabel.setObjectName("yCoorLabel")
        self.gridLayout_4.addWidget(self.yCoorLabel, 2, 1, 1, 1)
        self.addXCoor = QtWidgets.QToolButton(self.groupBox_4)
        self.addXCoor.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addXCoor.setFont(font)
        self.addXCoor.setObjectName("addXCoor")
        self.gridLayout_4.addWidget(self.addXCoor, 1, 2, 1, 1)
        self.removeXCoor = QtWidgets.QToolButton(self.groupBox_4)
        self.removeXCoor.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeXCoor.setFont(font)
        self.removeXCoor.setObjectName("removeXCoor")
        self.gridLayout_4.addWidget(self.removeXCoor, 1, 3, 1, 1)
        self.addYCoor = QtWidgets.QToolButton(self.groupBox_4)
        self.addYCoor.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addYCoor.setFont(font)
        self.addYCoor.setObjectName("addYCoor")
        self.gridLayout_4.addWidget(self.addYCoor, 2, 2, 1, 1)
        self.xCoorLabel = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.xCoorLabel.setFont(font)
        self.xCoorLabel.setReadOnly(True)
        self.xCoorLabel.setObjectName("xCoorLabel")
        self.gridLayout_4.addWidget(self.xCoorLabel, 1, 1, 1, 1)
        self.removeID = QtWidgets.QToolButton(self.groupBox_4)
        self.removeID.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.removeID.sizePolicy().hasHeightForWidth())
        self.removeID.setSizePolicy(sizePolicy)
        self.removeID.setMinimumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.removeID.setFont(font)
        self.removeID.setObjectName("removeID")
        self.gridLayout_4.addWidget(self.removeID, 0, 3, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isPrjCoorRBTN = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.isPrjCoorRBTN.setFont(font)
        self.isPrjCoorRBTN.setChecked(True)
        self.isPrjCoorRBTN.setObjectName("isPrjCoorRBTN")
        self.horizontalLayout.addWidget(self.isPrjCoorRBTN)
        self.isSphCoorRBTN = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.isSphCoorRBTN.setFont(font)
        self.isSphCoorRBTN.setObjectName("isSphCoorRBTN")
        self.horizontalLayout.addWidget(self.isSphCoorRBTN)
        self.gridLayout_13.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_13.setRowMinimumHeight(0, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isMGWRRBTN = QtWidgets.QRadioButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.isMGWRRBTN.setFont(font)
        self.isMGWRRBTN.setChecked(True)
        self.isMGWRRBTN.setObjectName("isMGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isMGWRRBTN)
        self.isGWRRBTN = QtWidgets.QRadioButton(self.groupBox_7)
        self.isGWRRBTN.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.isGWRRBTN.setFont(font)
        self.isGWRRBTN.setCheckable(True)
        self.isGWRRBTN.setChecked(False)
        self.isGWRRBTN.setObjectName("isGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isGWRRBTN)
        self.gridLayout_17.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.kernelDropdownGrou = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.kernelDropdownGrou.setFont(font)
        self.kernelDropdownGrou.setObjectName("kernelDropdownGrou")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.kernelDropdownGrou)
        self.gridLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fixedBox = QtWidgets.QComboBox(self.kernelDropdownGrou)
        self.fixedBox.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fixedBox.setFont(font)
        self.fixedBox.setObjectName("fixedBox")
        self.fixedBox.addItem("")
        self.fixedBox.addItem("")
        self.horizontalLayout_3.addWidget(self.fixedBox)
        self.shapeBox = QtWidgets.QComboBox(self.kernelDropdownGrou)
        self.shapeBox.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.shapeBox.setFont(font)
        self.shapeBox.setObjectName("shapeBox")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.horizontalLayout_3.addWidget(self.shapeBox)
        self.gridLayout_16.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.kernelDropdownGrou, 3, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.bwDropdown = QtWidgets.QComboBox(self.groupBox_9)
        self.bwDropdown.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bwDropdown.setFont(font)
        self.bwDropdown.setObjectName("bwDropdown")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.gridLayout_18.addWidget(self.bwDropdown, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight
                                          | QtCore.Qt.AlignTrailing
                                          | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading
                                         | QtCore.Qt.AlignLeft
                                         | QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_6)
        self.bwPreDefined = QtWidgets.QLineEdit(self.groupBox_9)
        self.bwPreDefined.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bwPreDefined.setFont(font)
        self.bwPreDefined.setObjectName("bwPreDefined")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.bwPreDefined)
        self.bwMin = QtWidgets.QLineEdit(self.groupBox_9)
        self.bwMin.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bwMin.setFont(font)
        self.bwMin.setObjectName("bwMin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.bwMin)
        self.bwMax = QtWidgets.QLineEdit(self.groupBox_9)
        self.bwMax.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bwMax.setFont(font)
        self.bwMax.setObjectName("bwMax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.bwMax)
        self.bwInterval = QtWidgets.QLineEdit(self.groupBox_9)
        self.bwInterval.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bwInterval.setFont(font)
        self.bwInterval.setObjectName("bwInterval")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.bwInterval)
        self.label_9 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_11)
        self.gridLayout_18.addLayout(self.formLayout, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_9, 4, 0, 2, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setAlignment(QtCore.Qt.AlignBottom
                                      | QtCore.Qt.AlignLeading
                                      | QtCore.Qt.AlignLeft)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.optimCriDropdown = QtWidgets.QComboBox(self.groupBox_11)
        self.optimCriDropdown.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.optimCriDropdown.setFont(font)
        self.optimCriDropdown.setObjectName("optimCriDropdown")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.gridLayout_9.addWidget(self.optimCriDropdown, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_11, 0, 2, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.modelTypeDropdown = QtWidgets.QComboBox(self.groupBox_12)
        self.modelTypeDropdown.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.modelTypeDropdown.setFont(font)
        self.modelTypeDropdown.setObjectName("modelTypeDropdown")
        self.modelTypeDropdown.addItem("")
        self.gridLayout_10.addWidget(self.modelTypeDropdown, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.advancedBTN = QtWidgets.QToolButton(self.groupBox_10)
        self.advancedBTN.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.advancedBTN.setFont(font)
        self.advancedBTN.setObjectName("advancedBTN")
        self.gridLayout_7.addWidget(self.advancedBTN, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_10, 5, 1, 1, 3)
        self.groupBox_13 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saveBetasBTN = QtWidgets.QToolButton(self.groupBox_13)
        self.saveBetasBTN.setMinimumSize(QtCore.QSize(23, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.saveBetasBTN.setFont(font)
        self.saveBetasBTN.setObjectName("saveBetasBTN")
        self.gridLayout_2.addWidget(self.saveBetasBTN, 1, 2, 1, 1)
        self.saveSumBTN = QtWidgets.QToolButton(self.groupBox_13)
        self.saveSumBTN.setMinimumSize(QtCore.QSize(23, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.saveSumBTN.setFont(font)
        self.saveSumBTN.setObjectName("saveSumBTN")
        self.gridLayout_2.addWidget(self.saveSumBTN, 0, 2, 1, 1)
        self.betaFileSavePath = QtWidgets.QLineEdit(self.groupBox_13)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.betaFileSavePath.setFont(font)
        self.betaFileSavePath.setObjectName("betaFileSavePath")
        self.gridLayout_2.addWidget(self.betaFileSavePath, 1, 1, 1, 1)
        self.sumFileSavePath = QtWidgets.QLineEdit(self.groupBox_13)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sumFileSavePath.setFont(font)
        self.sumFileSavePath.setReadOnly(True)
        self.sumFileSavePath.setObjectName("sumFileSavePath")
        self.gridLayout_2.addWidget(self.sumFileSavePath, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_13)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_13)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_13, 6, 0, 1, 3)
        self.runBTN = QtWidgets.QPushButton(Dialog)
        self.runBTN.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.runBTN.setFont(font)
        self.runBTN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.runBTN.setObjectName("runBTN")
        self.gridLayout_3.addWidget(self.runBTN, 6, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setContentsMargins(9, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.openDataPath = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.openDataPath.setFont(font)
        self.openDataPath.setObjectName("openDataPath")
        self.gridLayout_6.addWidget(self.openDataPath, 0, 0, 1, 1)
        self.openDataBTN = QtWidgets.QToolButton(self.groupBox)
        self.openDataBTN.setMinimumSize(QtCore.QSize(23, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.openDataBTN.setFont(font)
        self.openDataBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.openDataBTN.setObjectName("openDataBTN")
        self.gridLayout_6.addWidget(self.openDataBTN, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pool = pool

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MGWR"))
        self.groupBox_2.setTitle(_translate("Dialog", "Variable List"))
        self.groupBox_6.setTitle(_translate("Dialog", "Regression Variables"))
        self.addOffset.setText(_translate("Dialog", ">"))
        self.removeOffset.setText(_translate("Dialog", "<"))
        self.label_5.setText(_translate("Dialog", "Offset"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.addY.setText(_translate("Dialog", ">"))
        self.removeY.setText(_translate("Dialog", "<"))
        self.groupBox_3.setTitle(_translate("Dialog", "Local"))
        self.removeLocal.setText(_translate("Dialog", "<"))
        self.addLocal.setText(_translate("Dialog", ">"))
        self.groupBox_7.setTitle(_translate("Dialog", "GWR Mode"))
        self.isMGWRRBTN.setText(_translate("Dialog", "MGWR"))
        self.isGWRRBTN.setText(_translate("Dialog", "GWR"))
        self.kernelDropdownGrou.setTitle(
            _translate("Dialog", "Spatial Kernel"))
        self.fixedBox.setItemText(0, _translate("Dialog", "Adaptive"))
        self.fixedBox.setItemText(1, _translate("Dialog", "Fixed"))
        self.shapeBox.setItemText(0, _translate("Dialog", "Bisquare"))
        self.shapeBox.setItemText(1, _translate("Dialog", "Gaussian"))
        self.shapeBox.setItemText(2, _translate("Dialog", "Exponential"))
        self.groupBox_9.setTitle(_translate("Dialog", "Bandwidth Searching"))
        self.bwDropdown.setItemText(0, _translate("Dialog", "Golden Section"))
        self.bwDropdown.setItemText(1, _translate("Dialog", "Interval Search"))
        self.bwDropdown.setItemText(
            2, _translate("Dialog", "Pre-defiend bandwidth"))
        self.label_6.setText(_translate("Dialog", "Pre-defined"))
        self.label_9.setText(_translate("Dialog", "Min"))
        self.label_10.setText(_translate("Dialog", "Max"))
        self.label_11.setText(_translate("Dialog", "Interval"))
        self.groupBox_4.setTitle(_translate("Dialog", "Location Variables"))
        self.isPrjCoorRBTN.setText(_translate("Dialog", "Projected"))
        self.isSphCoorRBTN.setText(_translate("Dialog", "Spherical"))
        self.removeYCoor.setText(_translate("Dialog", ">"))
        self.addID.setText(_translate("Dialog", "<"))
        self.label_Y.setText(_translate("Dialog", "Y    "))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_X.setText(_translate("Dialog", "X    "))
        self.addXCoor.setText(_translate("Dialog", "<"))
        self.removeXCoor.setText(_translate("Dialog", ">"))
        self.addYCoor.setText(_translate("Dialog", "<"))
        self.removeID.setText(_translate("Dialog", ">"))
        self.groupBox.setTitle(_translate("Dialog", "Data Files"))
        self.openDataBTN.setText(_translate("Dialog", "..."))
        self.groupBox_10.setTitle(_translate("Dialog", "Model Options"))
        self.groupBox_11.setTitle(
            _translate("Dialog", "Optimization Criterion"))
        self.optimCriDropdown.setItemText(0, _translate("Dialog", "AICc"))
        self.optimCriDropdown.setItemText(1, _translate("Dialog", "AIC"))
        self.optimCriDropdown.setItemText(2, _translate("Dialog", "BIC"))
        self.optimCriDropdown.setItemText(3, _translate("Dialog", "CV"))
        self.groupBox_12.setTitle(_translate("Dialog", "Model Type"))
        self.modelTypeDropdown.setItemText(0, _translate("Dialog", "Gaussian"))
        self.advancedBTN.setText(_translate("Dialog", "Advanced"))
        self.runBTN.setText(_translate("Dialog", "Run"))
        self.groupBox_13.setTitle(_translate("Dialog", "Outputs"))
        self.saveBetasBTN.setText(_translate("Dialog", "..."))
        self.saveSumBTN.setText(_translate("Dialog", "..."))
        self.label_7.setText(_translate("Dialog", "Summary File"))
        self.label_8.setText(_translate("Dialog", "Parameter Estimates"))

    def update_label(self):
        current_time = self.elapsedTimeFormatter(self.time)
        self.loaderUI.label_2.setText(current_time)

    def elapsedTimeFormatter(self, time):
        secs = time.elapsed() / 1000
        mins = int((secs / 60) % 60)
        hours = int((secs / 3600))
        secs = int(secs % 60)
        return str(hours).zfill(2) + ':' + str(mins).zfill(2) + ':' + str(
            secs).zfill(2)

    def addActionsToUI(self):

        self.greyOutLineEdit(self.OffsetLabel)
        self.greyOutLineEdit(self.bwPreDefined)
        self.greyOutLineEdit(self.bwMin)
        self.greyOutLineEdit(self.bwMax)
        self.greyOutLineEdit(self.bwInterval)

        self.openDataBTN.clicked.connect(self.openData)
        #self.openPredictionBTN.clicked.connect(self.openPredictData)

        self.saveSumBTN.clicked.connect(lambda: self.getSaveFile(0))
        self.saveBetasBTN.clicked.connect(lambda: self.getSaveFile(1))

        self.addID.clicked.connect(lambda: self.addVariable(self.idLabel))
        self.removeID.clicked.connect(lambda: self.removeVariable(self.idLabel)
                                      )

        self.addXCoor.clicked.connect(lambda: self.addVariable(self.xCoorLabel)
                                      )
        self.removeXCoor.clicked.connect(lambda: self.removeVariable(
            self.xCoorLabel))

        self.addYCoor.clicked.connect(lambda: self.addVariable(self.yCoorLabel)
                                      )
        self.removeYCoor.clicked.connect(lambda: self.removeVariable(
            self.yCoorLabel))

        self.addY.clicked.connect(lambda: self.addVariable(self.responseLabel))
        self.removeY.clicked.connect(lambda: self.removeVariable(
            self.responseLabel))

        self.addOffset.clicked.connect(lambda: self.addVariable(self.
                                                                OffsetLabel))
        self.removeOffset.clicked.connect(lambda: self.removeVariable(
            self.OffsetLabel))

        self.addLocal.clicked.connect(self.addVarToLocal)
        self.removeLocal.clicked.connect(self.removeVarFromLocal)

        self.runBTN.clicked.connect(self.run_onclick)
        self.advancedBTN.clicked.connect(self.advancedOnClick)

        self.openDataPath.textChanged.connect(lambda: self.removeRed(
            self.openDataPath))
        self.sumFileSavePath.textChanged.connect(lambda: self.removeRed(
            self.sumFileSavePath))
        self.betaFileSavePath.textChanged.connect(lambda: self.removeRed(
            self.betaFileSavePath))

        self.responseLabel.textChanged.connect(lambda: self.removeRed(
            self.responseLabel))
        self.xCoorLabel.textChanged.connect(lambda: self.removeRed(self.
                                                                   xCoorLabel))
        self.yCoorLabel.textChanged.connect(lambda: self.removeRed(self.
                                                                   yCoorLabel))
        self.idLabel.textChanged.connect(lambda: self.removeRed(self.idLabel))

        self.bwMin.textChanged.connect(lambda: self.removeRed(self.bwMin))
        self.bwMax.textChanged.connect(lambda: self.removeRed(self.bwMax))
        self.bwPreDefined.textChanged.connect(lambda: self.removeRed(
            self.bwPreDefined))
        self.bwInterval.textChanged.connect(lambda: self.removeRed(self.
                                                                   bwInterval))

        self.isGWRRBTN.clicked.connect(self.gwrMode)
        self.isMGWRRBTN.clicked.connect(self.mgwrMode)

        self.isPrjCoorRBTN.clicked.connect(self.projCoors)
        self.isSphCoorRBTN.clicked.connect(self.sphCoors)

        validator = QtGui.QDoubleValidator()
        validator.setBottom(0)
        self.bwMin.setValidator(validator)
        self.bwMax.setValidator(validator)
        self.bwInterval.setValidator(validator)
        self.bwPreDefined.setValidator(validator)

        self.bwDropdown.currentIndexChanged.connect(self.changeSearchMethod)
        self.modelTypeDropdown.currentIndexChanged.connect(self.modelChanged)

        self.mgwrMode()

        self.thread = GWRThread(self)
        self.thread.finished.connect(self.workDone)
        self.runningWindow = QtWidgets.QDialog()

        self.runningDialog = QtWidgets.QDialog()
        self.loaderUI = Ui_runningDialog()
        self.loaderUI.setupUi(self.runningDialog)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.time = QtCore.QTime()

        self.path = os.path.dirname(
            os.path.dirname(os.path.dirname(sys.argv[0])))

        self.advMGWRDialog = QtWidgets.QDialog()
        self.advMGWRDialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.advMGWRUI = Ui_advMGWRDialog()
        self.advMGWRUI.setupUi(self.advMGWRDialog)
        self.advMGWRUI.addActionsToUI()

        self.advGWRDialog = QtWidgets.QDialog()
        self.advGWRDialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.advGWRUI = Ui_advGWRDialog()
        self.advGWRUI.setupUi(self.advGWRDialog)
        self.advGWRUI.addActionsToUI()
        self.log_stream = StringIO()

    def openData(self):

        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, 'OpenFile', self.path, "Table(*.csv *.xls *.xlsx *.dbf)")
            if fileName:
                self.openDataPath.setText(fileName)
                if fileName.endswith('.csv'):
                    self.data = pd.read_csv(fileName)
                elif fileName.endswith('.xlsx') or fileName.endswith('.xls'):
                    self.data = pd.read_excel(fileName)
                elif fileName.endswith('.dbf'):
                    self.data = Dbf5(fileName).to_dataframe()

                fields = self.data.columns.tolist()
                self.localList.clear()
                self.localList.addItem('Intercept')
                self.variableList.clear()
                self.OffsetLabel.clear()
                self.idLabel.clear()
                self.xCoorLabel.clear()
                self.yCoorLabel.clear()
                self.responseLabel.clear()
                self.variableList.addItems(fields)

        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(
                'Something went wrong when opening data. Please double check.'
            )
            error_dialog.exec_()
            f = open('log.txt', 'w')
            f.write('An exceptional thing happed - %s' % e)
            f.close()
            logging.exception('')

    def openPredictData(self):
        self.path = os.path.dirname(
            os.path.dirname(os.path.dirname(sys.argv[0])))
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, 'OpenFile', self.path, "CSV (*.csv)")
            if fileName:
                self.predictInputEdit.setText(fileName)
                self.predictData = pd.read_csv(fileName)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(
                'Something went wrong when opening data. Please double check.'
            )
            error_dialog.exec_()

    def addVariable(self, destination):
        if destination.text() and self.variableList.selectedItems():
            self.variableList.addItem(destination.text())
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(
                self.variableList.row(self.variableList.selectedItems()[0]))
            item = None
        elif not destination.text() and self.variableList.selectedItems():
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(
                self.variableList.row(self.variableList.selectedItems()[0]))
            item = None

    def removeVariable(self, origin):
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

    def removeRed(self, lineEdit):
        lineEdit.setStyleSheet("")

    def greyOutLineEdit(self, lineEdit):
        lineEdit.clear()
        lineEdit.setStyleSheet("background-color:LightGrey")
        lineEdit.setDisabled(True)

    def deGreyOutLineEdit(self, lineEdit):
        lineEdit.setStyleSheet("")
        lineEdit.setDisabled(False)

    def changeSearchMethod(self, index):
        #golden section
        if index == 0:
            self.removeRed(self.bwMin)
            self.removeRed(self.bwMax)
            self.removeRed(self.bwInterval)
            self.removeRed(self.bwPreDefined)
            self.greyOutLineEdit(self.bwPreDefined)
            self.greyOutLineEdit(self.bwInterval)
            self.greyOutLineEdit(self.bwMin)
            self.greyOutLineEdit(self.bwMax)
        #interval
        elif index == 1:
            self.removeRed(self.bwPreDefined)
            self.greyOutLineEdit(self.bwPreDefined)
            self.deGreyOutLineEdit(self.bwInterval)
            self.deGreyOutLineEdit(self.bwMin)
            self.deGreyOutLineEdit(self.bwMax)
        #defined
        elif index == 2 and self.isGWR:
            self.removeRed(self.bwMin)
            self.removeRed(self.bwMax)
            self.removeRed(self.bwInterval)
            self.deGreyOutLineEdit(self.bwPreDefined)
            self.greyOutLineEdit(self.bwInterval)
            self.greyOutLineEdit(self.bwMin)
            self.greyOutLineEdit(self.bwMax)

    def modelChanged(self, index):
        #Gaussian
        if index == 0:
            self.removeVariable(self.OffsetLabel)
            self.greyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(False)
            self.removeOffset.setEnabled(False)
        #Binomial
        elif index == 1:
            self.removeVariable(self.OffsetLabel)
            self.greyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(False)
            self.removeOffset.setEnabled(False)
        #Poisson
        elif index == 2:
            self.deGreyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(True)
            self.removeOffset.setEnabled(True)

    def gwrMode(self):

        #self.predictionBox.show()
        #self.predictionBox.setEnabled(True)
        self.advancedBTN.setEnabled(True)

        self.modelTypeDropdown.clear()
        self.modelTypeDropdown.addItem("Gaussian")
        self.modelTypeDropdown.addItem("Binomial")
        self.modelTypeDropdown.addItem("Poisson")

        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.bwDropdown.clear()
        self.bwDropdown.addItem("Golden Section")
        self.bwDropdown.addItem("Interval Search")
        self.bwDropdown.addItem("Pre-defined bandwidth")

        self.isGWR = True
        self.isMGWR = False

    def mgwrMode(self):
        #self.predictionBox.setEnabled(False)
        self.advancedBTN.setEnabled(True)

        self.modelTypeDropdown.clear()
        self.modelTypeDropdown.addItem("Gaussian")
        self.bwDropdown.removeItem(1)
        self.bwDropdown.removeItem(1)

        self.isMGWR = True
        self.isGWR = False

    def projCoors(self):
        self.label_X.setText('X   ')
        self.label_Y.setText('Y   ')

    def sphCoors(self):
        self.label_X.setText('Lon')
        self.label_Y.setText('Lat')

    def advancedOnClick(self):
        if self.isGWR:
            self.advGWRUI.loadSettings()
            self.advGWRDialog.exec_()

        if self.isMGWR:
            self.advMGWRUI.loadSettings()
            self.advMGWRDialog.exec_()

    #Get 3 Save Paths for control, summary and betas
    def getSaveFile(self, ext):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 'SaveFile',
            os.path.join(os.path.dirname(self.path), 'MGWR_session'))
        if fileName:
            if ext == 0:
                self.sumFileSavePath.setText(fileName + '_summary.txt')
                self.betaFileSavePath.setText(fileName + '_results.csv')
            if ext == 1:
                self.betaFileSavePath.setText(fileName + '_results.csv')

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
        if not self.responseLabel.text():
            self.responseLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.xCoorLabel.text():
            self.xCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.yCoorLabel.text():
            self.yCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.localList.count():
            self.localList.setStyleSheet("QListWidget{border: 2px solid red;}")
            allSet = False

        if self.bwDropdown.currentText() == "Interval Search":
            if not self.bwMin.text():
                self.bwMin.setStyleSheet("border: 2px solid red;")
                allSet = False
            if not self.bwMax.text():
                self.bwMax.setStyleSheet("border: 2px solid red;")
                allSet = False
            if not self.bwInterval.text():
                self.bwInterval.setStyleSheet("border: 2px solid red;")
                allSet = False
        if self.bwDropdown.currentText() == "Pre-defined bandwidth":
            if not self.bwPreDefined.text():
                self.bwPreDefined.setStyleSheet("border: 2px solid red;")
                allSet = False

        return allSet

    def loadDataModel(self):
        try:
            #Load Variables
            if self.idLabel.text():
                self.id = self.data[[self.idLabel.text()]]
                self.idName = self.idLabel.text()
            else:
                self.id = pd.Series(np.arange(self.data.shape[0]))
                self.idName = "id"

            print(self.id)
            self.data['Intercept'] = 1
            self.yName = self.responseLabel.text()
            self.XNames = [
                str(self.localList.item(i).text())
                for i in range(self.localList.count())
            ]
            if 'Intercept' in self.XNames:
                self.constant = True
                self.X = self.data[self.XNames].drop(columns=['Intercept'])
            else:
                self.constant = False
                self.X = self.data[self.XNames]

            self.y = self.data[[self.responseLabel.text()]]
            #self.X = self.data[self.XNames]
            self.xCoor = self.data[[self.xCoorLabel.text()]]
            self.yCoor = self.data[[self.yCoorLabel.text()]]

            self.comp_data = pd.concat(
                [self.id, self.y, self.X, self.xCoor, self.yCoor],
                axis=1).dropna()
            #self.comp_data = self.comp_data[self.comp_data.applymap(np.isreal).all(1)]

            if self.idLabel.text():
                self.id = self.comp_data[[self.idLabel.text()]].values.reshape(
                    -1, 1)
            else:
                self.id = pd.Series(np.arange(self.comp_data.shape[0]))

            self.y = self.comp_data[[self.responseLabel.text()
                                     ]].values.reshape(-1, 1)
            self.X = self.comp_data.ix[:, 2:-2].values
            self.xCoor = self.comp_data.ix[:, -2]
            self.yCoor = self.comp_data.ix[:, -1]

            self.nObs = len(self.comp_data.index)
            self.nMiss = len(self.data.index) - self.nObs
            self.coords = np.array(list(zip(self.xCoor, self.yCoor)))
            self.offset = None

            if self.isPrjCoorRBTN.isChecked():
                self.coorType = False
            if self.isSphCoorRBTN.isChecked():
                self.coorType = True

            #Load Model Options:

            if self.bwDropdown.currentText() == "Golden Section":
                self.search = 'golden_section'

            elif self.bwDropdown.currentText() == "Interval Search":
                self.search = 'interval'
            else:
                self.search = 'preset'

            self.fixed = (self.fixedBox.currentText() == "Fixed")
            self.kernel = self.shapeBox.currentText().lower()
            self.criterion = self.optimCriDropdown.currentText()
            self.isGWR = self.isGWRRBTN.isChecked()
            self.isMGWR = self.isMGWRRBTN.isChecked()

            if self.modelTypeDropdown.currentText() == "Gaussian":
                self.family = Gaussian()
            elif self.modelTypeDropdown.currentText() == "Poisson":
                self.family = Poisson()
                if self.OffsetLabel.text() is not '':
                    self.offset = self.data[[self.OffsetLabel.text()
                                             ]].as_matrix().reshape(-1, 1)
            elif self.modelTypeDropdown.currentText() == "Binomial":
                self.family = Binomial()

            #MGWR Advanced Settings
            self.MGWRVarSTD = self.advMGWRUI.varSTD
            self.GWRVarSTD = self.advGWRUI.varSTD

            if self.MGWRVarSTD == 'On' and self.isMGWR:
                self.X = (self.X - np.mean(self.X, axis=0)) / np.std(
                    self.X, axis=0)
                self.y = (self.y - np.mean(self.y, axis=0)) / np.std(
                    self.y, axis=0)

            if self.GWRVarSTD == 'On' and self.isGWR:
                self.X = (self.X - np.mean(self.X, axis=0)) / np.std(
                    self.X, axis=0)
                self.y = (self.y - np.mean(self.y, axis=0)) / np.std(
                    self.y, axis=0)

            self.SOC = self.advMGWRUI.soc
            self.initBeta = self.advMGWRUI.init
            self.tol_multi = float(self.advMGWRUI.converg)
            self.tol_gwr = 1e-05

            if self.isMGWR:
                self.mcTest = self.advMGWRUI.mcTest
                self.locollinear = self.advMGWRUI.locollinear
                self.mcc = "Bonferroni"
            if self.isGWR:
                self.mcTest = self.advGWRUI.mcTest
                self.locollinear = self.advGWRUI.locollinear
                self.mcc = "Bonferroni"

            if self.initBeta == "GWR estimates":
                self.init_multi = True
                self.init_multi_bw = None
            else:
                self.init_multi = False
                if self.fixed:
                    self.init_multi_bw = np.inf
                else:
                    self.init_multi_bw = self.y.shape[0]

            if self.SOC == "SOC-f":
                self.rss_score = False
            else:
                self.rss_score = True

            return True

        except:
            return False

    def run_onclick(self):

        if not self.preCheckEmptyFields():
            err_msg = QtWidgets.QMessageBox.critical(
                None, "Error", "Please fix inputs in red.")
            return

        if not self.loadDataModel():
            err_msg = QtWidgets.QMessageBox.critical(
                None, "Error",
                "Something wrong when loading variables to model.")
            return

        self.threadRunning = True
        self.thread.start()

        self.time.start()
        self.timer.start(1000)  # every 10,000 milliseconds
        self.loaderUI.restartTimer()
        self.runningDialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                                          | QtCore.Qt.WindowCloseButtonHint)
        #self.runningDialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.loaderUI.connect(self.loaderUI, Qt.SIGNAL('triggered()'), self.closeEvent)
        self.runningDialog.closeEvent = self.closeEvent
        self.runningDialog.exec_()

    def closeEvent(self, event):
        if self.threadRunning:
            reply = QtWidgets.QMessageBox.question(
                None, 'Message',
                "Closing this diaglog will quit MGWR, are you sure to quit?",
                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:

                #self.timer.stop()
                #self.loaderUI.stopThread(self.thread)
                event.accept()
                #self.thread.stop()

                QtWidgets.QApplication.quit()
            else:
                event.ignore()

    def workDone(self):
        self.timer.stop()
        self.threadRunning = False
        #self.runningDialog.close()
        if not self.success:
            err_msg = QtWidgets.QMessageBox.critical(
                None, "Error",
                "Something went wrong during model calibration. Please double check your settings and data."
            )
            return

        msg = QtWidgets.QMessageBox.information(
            None, "Success", "Running complete!\nTime Elapsed:\n" +
            self.elapsedTimeFormatter(self.time))
        summaryDlg = QtWidgets.QDialog()
        smyui = Ui_summaryDlg()
        smyui.setupUi(summaryDlg)
        smyui.loadText(self.sumFileSavePath.text())
        summaryDlg.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                                  | QtCore.Qt.WindowCloseButtonHint)
        summaryDlg.exec_()

    #Run model
    def runGWR(self):
        self.begin_t = datetime.now()
        print("Started at: ", str(self.begin_t).split('.', 2)[0])
        try:
            if self.isGWR:
                print("Running GWR...")
                self.selector = Sel_BW(
                    self.coords,
                    self.y,
                    self.X,
                    kernel=self.kernel,
                    fixed=self.fixed,
                    family=self.family,
                    offset=self.offset,
                    constant=self.constant,
                    spherical=self.coorType)
                if self.search == 'golden_section':
                    print("Golden section search minimizing", self.criterion)
                    self.bw = self.selector.search(
                        search_method='golden_section',
                        criterion=self.criterion,
                        pool=self.pool,
                        verbose=True)

                elif self.search == 'interval':
                    print("Interval bandwidth searching:")
                    min = int(float(self.bwMin.text()))
                    max = int(float(self.bwMax.text()))
                    step = int(float(self.bwInterval.text()))
                    self.bw = self.selector.search(
                        search_method='interval',
                        bw_min=min,
                        bw_max=max,
                        interval=step,
                        criterion=self.criterion,
                        pool=self.pool,
                        verbose=True)

                else:
                    self.bw = int(float(self.bwPreDefined.text()))
                print("Fitting GWR using optimal bandwidth: ", self.bw)
                self.results = GWR(
                    self.coords,
                    self.y,
                    self.X,
                    self.bw,
                    fixed=self.fixed,
                    kernel=self.kernel,
                    family=self.family,
                    offset=self.offset,
                    constant=self.constant,
                    spherical=self.coorType).fit(pool=self.pool)

                if self.mcTest != "Off":
                    print("Starting spatial variability test")
                    self.testMCResults = self.results.spatial_variability(
                        self.selector, pool=self.pool)

                if self.locollinear != "Off":
                    self.locollinearResults = self.results.local_collinearity()

                self.end_t = datetime.now()
                outputGWR(self)

            if self.isMGWR:
                print("MGWR running...")
                print("Backfitting...")
                self.selector = Sel_BW(
                    self.coords,
                    self.y,
                    self.X,
                    fixed=self.fixed,
                    kernel=self.kernel,
                    multi=True,
                    constant=self.constant,
                    spherical=self.coorType)
                self.bws = self.selector.search(
                    search_method='golden_section',
                    criterion=self.criterion,
                    rss_score=self.rss_score,
                    tol_multi=self.tol_multi,
                    init_multi=self.init_multi_bw,
                    pool=self.pool,
                    verbose=True)
                print("Computing inference...")
                suggested_n_chunks = int(np.ceil(1.5 * (self.selector.X_loc.shape[0])**2*8*self.selector.X_loc.shape[1]/psutil.virtual_memory().available))
                self.results = MGWR(
                    self.coords,
                    self.y,
                    self.X,
                    self.selector,
                    kernel=self.kernel,
                    fixed=self.fixed,
                    constant=self.constant,
                    spherical=self.coorType).fit(
                        n_chunks=suggested_n_chunks, pool=self.pool)

                if self.mcTest != "Off":
                    print("Starting spatial variability test")
                    self.testMCResults = self.results.spatial_variability(
                        self.selector, pool=self.pool)

                if self.locollinear != "Off":
                    self.locollinearResults = self.results.local_collinearity()

                self.end_t = datetime.now()
                outputMGWR(self)

            print("Done!")
            print("Ended at: ", str(self.end_t).split('.', 2)[0])
            self.success = True

        except Exception as err:
            #error_dialog = QtWidgets.QErrorMessage()
            #error_dialog.showMessage('Something went wrong when opening data. Please double check.')
            #error_dialog.exec_()
            #logging.basicConfig(filename='mgwr.log', level=logging.DEBUG)

            logging.basicConfig(stream=self.log_stream, level=logging.DEBUG)
            logging.exception(err)
            self.end_t = datetime.now()
            print("Error!")
            print("Ended at: ", str(self.end_t).split('.', 2)[0])
            print(self.log_stream.getvalue())
            self.log_stream.seek(0)
            self.log_stream.truncate(0)
            self.success = False

            return


class GWRThread(QtCore.QThread):
    def __init__(self, Ui_Dialog, parent=None):
        super(QtCore.QThread, self).__init__()
        self.diag = Ui_Dialog

    def run(self):
        self.diag.runGWR()

    def stop(self):
        print("stopping")


class timerThread(QtCore.QThread):
    timeElapsed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(timerThread, self).__init__(parent)
        self.timeStart = None

    def start(self, timeStart):
        self.timeStart = timeStart

        return super(timerThread, self).start()

    def run(self):
        while self.parent().isRunning():
            self.timeElapsed.emit(time.time() - self.timeStart)
            time.sleep(1)
