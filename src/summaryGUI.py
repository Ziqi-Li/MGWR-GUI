# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_summaryDlg(object):
    def setupUi(self, summaryDlg):

        summaryDlg.setObjectName("summaryDlg")
        summaryDlg.setWindowModality(QtCore.Qt.WindowModal)
        summaryDlg.setEnabled(True)
        summaryDlg.resize(750, 400)

        grid = QtWidgets.QGridLayout()
        summaryDlg.setLayout(grid)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        summaryDlg.setFont(font)

        self.summaryEdit = QtWidgets.QTextEdit()
        self.summaryEdit.setReadOnly(True)
        grid.addWidget(self.summaryEdit, 0, 0)
        self.retranslateUi(summaryDlg)
        QtCore.QMetaObject.connectSlotsByName(summaryDlg)

    def retranslateUi(self, summaryDlg):
        _translate = QtCore.QCoreApplication.translate
        summaryDlg.setWindowTitle(_translate("summaryDlg", "Summary"))

    def loadText(self, filePath):
        self.summaryEdit.setReadOnly(True)
        text = open(filePath).read()
        self.summaryEdit.setText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    summaryDlg = QtWidgets.QDialog()
    ui = Ui_summaryDlg()
    ui.setupUi(summaryDlg)
    summaryDlg.show()
    sys.exit(app.exec_())
