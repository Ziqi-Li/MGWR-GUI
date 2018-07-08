# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from src.gui import Ui_Dialog


if __name__ == "__main__":
    import sys, time
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('mac')
    
    
    # Create and display the splash screen
    splash_pix = QtGui.QPixmap('./img/Group.png')
    #splash_pix = img.scaled(QtCore.QSize(634/2,468/2),QtCore.Qt.KeepAspectRatio)
    
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # adding progress bar
    progressBar = QtWidgets.QProgressBar(splash)
    progressBar.setGeometry(splash.width()/10, 8.8*splash.height()/10,
                            9*splash.width()/10, splash.height()/10)
    splash.setMask(splash_pix.mask())
    
    splash.show()
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.01:
            app.processEvents()

    #Initiate Main Dialog
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setFixedSize(Dialog.size())
    ui.addActionsToUI()
    Dialog.show()
    splash.finish(Dialog)
    sys.exit(app.exec_())

