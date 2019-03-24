# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os


class Ui_runningDialog(object):
    def setupUi(self, runningDialog):
        runningDialog.setObjectName("runningDialog")
        runningDialog.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            runningDialog.sizePolicy().hasHeightForWidth())
        runningDialog.setSizePolicy(sizePolicy)
        runningDialog.setMinimumSize(QtCore.QSize(600, 400))
        runningDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(runningDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(runningDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(runningDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.printTextEdit = QtWidgets.QTextEdit(runningDialog)
        self.printTextEdit.setObjectName("printTextEdit")
        self.gridLayout.addWidget(self.printTextEdit, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 2)
        self.loadingGIFLabel = QtWidgets.QLabel(runningDialog)
        self.loadingGIFLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loadingGIFLabel.setText("")
        self.loadingGIFLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingGIFLabel.setObjectName("loadingGIFLabel")
        self.gridLayout_2.addWidget(self.loadingGIFLabel, 1, 1, 1, 1)
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
        runningDialog.setWindowTitle(
            _translate("runningDialog", "MGWR Running"))
        self.label.setText(_translate("runningDialog", "Time Elapsed:"))
        self.label_2.setText(_translate("runningDialog", "00:00:00"))

    def restartTimer(self):
        self.printTextEdit.clear()
        self.label_2.setText("00:00:00")

    def stopThread(self, thread):
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

    def flush(self):
        pass
