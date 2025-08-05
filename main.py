# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui import Ui_Dialog
import sys,os,time
import multiprocessing as mp
import psutil
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Windows 8.1+
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()  # Windows 7
    except:
        pass


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == "__main__":
    #mp.set_start_method('spawn',force=True)
    
    #os.environ["OMP_NUM_THREADS"] = "1"
    mp.freeze_support()
    #os.environ["OPENBLAS_NUM_THREADS"] = "1"
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('mac')


    #  calculate scale factor based on primary screen size
    screen = app.primaryScreen()
    scale_factor = screen.size().width() / 1920.0

    # Set application font and scale it
    font = app.font()
    font.setHintingPreference(QtGui.QFont.PreferFullHinting)
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    font.setPointSizeF(font.pointSizeF() * scale_factor)
    app.setFont(font)


    
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "arial.ttf")

    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print("failed to load font:", font_path)
    else:
        font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            font = QtGui.QFont(font_families[0])
            font.setPointSize(10)  # 預設字型大小，可調整
            app.setFont(font)
            print(f"font {font_families[0]} has been loaded successfully")
    

    app_icon = QtGui.QIcon()
    app_icon.addFile(resource_path('img/MGWR16.png'), QtCore.QSize(16,16))
    app_icon.addFile(resource_path('img/MGWR24.png'), QtCore.QSize(24,24))
    app_icon.addFile(resource_path('img/MGWR32.png'), QtCore.QSize(32,32))
    app_icon.addFile(resource_path('img/MGWR48.png'), QtCore.QSize(48,48))
    app_icon.addFile(resource_path('img/MGWR64.png'), QtCore.QSize(64,64))
    app_icon.addFile(resource_path('img/MGWR128.png'), QtCore.QSize(128,128))
    app.setWindowIcon(app_icon)
    
    
    # Create and display the splash screen
    splash_pix = QtGui.QPixmap(resource_path('img/Group.png'))
    #splash_pix = img.scaled(QtCore.QSize(634/2,468/2),QtCore.Qt.KeepAspectRatio)
    
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # adding progress bar
    progressBar = QtWidgets.QProgressBar(splash)
    progressBar.setGeometry(splash.width()//10, 9*splash.height()//10,
                            8*splash.width()//10, splash.height()//10)
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
    pool = mp.Pool(psutil.cpu_count())
    ui.setupUi(Dialog, pool)
    # ui.scaleUi(Dialog, scale_factor)
    Dialog.setFixedSize(Dialog.size())
    ui.addActionsToUI()
    Dialog.show()
    splash.finish(Dialog)
    sys.exit(app.exec_())

