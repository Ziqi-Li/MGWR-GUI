# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os

class Ui_runningDialog(object):
    def setupUi(self, runningDialog):
        runningDialog.setObjectName("runningDialog")
        runningDialog.resize(501, 361)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(runningDialog.sizePolicy().hasHeightForWidth())
        runningDialog.setSizePolicy(sizePolicy)
        runningDialog.setModal(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(runningDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 30, 171, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.loadingGIFLabel = QtWidgets.QLabel(runningDialog)
        self.loadingGIFLabel.setGeometry(QtCore.QRect(110, 60, 50, 50))
        self.loadingGIFLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loadingGIFLabel.setText("")
        self.loadingGIFLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingGIFLabel.setObjectName("loadingGIFLabel")
        self.printTextEdit = QtWidgets.QTextEdit(runningDialog)
        self.printTextEdit.setGeometry(QtCore.QRect(20, 60, 461, 281))
        self.printTextEdit.setObjectName("printTextEdit")
    
        
        """
        self.movie = QtGui.QMovie(resource_path("img/loader-50.gif"), QtCore.QByteArray())
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.loadingGIFLabel.setMovie(self.movie)
        self.movie.start()
        """
        self.printTextEdit.setReadOnly(True)
        self.retranslateUi(runningDialog)
        QtCore.QMetaObject.connectSlotsByName(runningDialog)

    def retranslateUi(self, runningDialog):
        _translate = QtCore.QCoreApplication.translate
        runningDialog.setWindowTitle(_translate("runningDialog", "MGWR Running"))
        self.label.setText(_translate("runningDialog", "Time Elapsed:"))
        self.label_2.setText(_translate("runningDialog", "00:00:00"))
    
    def restartTimer(self):
        self.printTextEdit.clear()
        self.label_2.setText("00:00:00")

    def stopThread(self,thread):
        thread.terminate()

    def __init__(self, parent=None, **kwargs):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        cursor = self.printTextEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.printTextEdit.setTextCursor(cursor)
        self.printTextEdit.ensureCursorVisible()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class EmittingStream(QtCore.QObject):
    
    textWritten = QtCore.pyqtSignal(str)
    
    def write(self, text):
        self.textWritten.emit(str(text))



