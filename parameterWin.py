# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created: Fri Oct  2 01:58:21 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_paramWindow(object):
    def setupUi(self, paramWindow):
        paramWindow.setObjectName(_fromUtf8("paramWindow"))
        paramWindow.resize(379, 155)
        paramWindow.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Loma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        paramWindow.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(paramWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(paramWindow)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.lineEditFilename = QtGui.QLineEdit(paramWindow)
        self.lineEditFilename.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditFilename.setObjectName(_fromUtf8("lineEditFilename"))
        self.gridLayout.addWidget(self.lineEditFilename, 0, 3, 1, 2)
        self.label_2 = QtGui.QLabel(paramWindow)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 2)
        self.spinBoxNodeNumber = QtGui.QSpinBox(paramWindow)
        self.spinBoxNodeNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxNodeNumber.setObjectName(_fromUtf8("spinBoxNodeNumber"))
        self.gridLayout.addWidget(self.spinBoxNodeNumber, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonValider = QtGui.QPushButton(paramWindow)
        self.pushButtonValider.setObjectName(_fromUtf8("pushButtonValider"))
        self.horizontalLayout.addWidget(self.pushButtonValider)
        spacerItem2 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonAnnuler = QtGui.QPushButton(paramWindow)
        self.pushButtonAnnuler.setObjectName(_fromUtf8("pushButtonAnnuler"))
        self.horizontalLayout.addWidget(self.pushButtonAnnuler)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(paramWindow)
        QtCore.QMetaObject.connectSlotsByName(paramWindow)

    def retranslateUi(self, paramWindow):
        paramWindow.setWindowTitle(_translate("paramWindow", "Parameters", None))
        self.label.setText(_translate("paramWindow", "File name", None))
        self.label_2.setText(_translate("paramWindow", "Number of nodes", None))
        self.pushButtonValider.setText(_translate("paramWindow", "Valider", None))
        self.pushButtonAnnuler.setText(_translate("paramWindow", "Annuler", None))

