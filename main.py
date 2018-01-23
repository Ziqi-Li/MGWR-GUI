# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from src.gui import Ui_Dialog
#from src.controller import addActionsToUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.addActionsToUI()
    
    
    Dialog.show()
    sys.exit(app.exec_())

