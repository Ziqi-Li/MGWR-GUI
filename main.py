# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QApplication,QSplashScreen,QProgressBar,QDialog
import sys,os
import time
from src.gui import Ui_Dialog


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == "__main__":
    import sys, time
    
    app = QApplication(sys.argv)
    app.setStyle('mac')
	
    app_icon = QIcon()
    app_icon.addFile(resource_path('img/MGWR16.png'), QSize(16,16))
    app_icon.addFile(resource_path('img/MGWR24.png'), QSize(24,24))
    app_icon.addFile(resource_path('img/MGWR32.png'), QSize(32,32))
    app_icon.addFile(resource_path('img/MGWR48.png'), QSize(48,48))
    app_icon.addFile(resource_path('img/MGWR64.png'), QSize(64,64))
    app_icon.addFile(resource_path('img/MGWR128.png'), QSize(128,128))
    app.setWindowIcon(app_icon)
    
    
    # Create and display the splash screen
    splash_pix = QPixmap(resource_path('img/Group.png'))
    #splash_pix = img.scaled(QtCore.QSize(634/2,468/2),QtCore.Qt.KeepAspectRatio)
    
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # adding progress bar
    progressBar = QProgressBar(splash)
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
    Dialog = QDialog()
    Dialog.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setFixedSize(Dialog.size())
    ui.addActionsToUI()
    Dialog.show()
    splash.finish(Dialog)
    sys.exit(app.exec_())

