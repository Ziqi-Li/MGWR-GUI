# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui import Ui_Dialog

def addActionsToUI(myDialog):
    myDialog.openDataButton.clicked.connect(openData)

def openData():
    print('PyQt5 button click')

