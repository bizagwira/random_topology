# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RfParameters.ui'
#
# Created: Tue Oct 20 17:03:03 2015
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

class Ui_rfSettingWindow(object):
    def setupUi(self, rfSettingWindow):
        rfSettingWindow.setObjectName(_fromUtf8("rfSettingWindow"))
        rfSettingWindow.resize(379, 155)
        rfSettingWindow.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Loma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        rfSettingWindow.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(rfSettingWindow)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(rfSettingWindow)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.rangeDoubleSpinBox = QtGui.QDoubleSpinBox(rfSettingWindow)
        self.rangeDoubleSpinBox.setMinimumSize(QtCore.QSize(150, 40))
        self.rangeDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rangeDoubleSpinBox.setMinimum(5.0)
        self.rangeDoubleSpinBox.setMaximum(200.0)
        self.rangeDoubleSpinBox.setProperty("value", 5.0)
        self.rangeDoubleSpinBox.setObjectName(_fromUtf8("rangeDoubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.rangeDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(rfSettingWindow)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.spinBoxNodeNumber = QtGui.QSpinBox(rfSettingWindow)
        self.spinBoxNodeNumber.setMinimumSize(QtCore.QSize(150, 40))
        self.spinBoxNodeNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxNodeNumber.setMinimum(2)
        self.spinBoxNodeNumber.setMaximum(200)
        self.spinBoxNodeNumber.setObjectName(_fromUtf8("spinBoxNodeNumber"))
        self.horizontalLayout_3.addWidget(self.spinBoxNodeNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonValider = QtGui.QPushButton(rfSettingWindow)
        self.pushButtonValider.setObjectName(_fromUtf8("pushButtonValider"))
        self.horizontalLayout.addWidget(self.pushButtonValider)
        spacerItem2 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonAnnuler = QtGui.QPushButton(rfSettingWindow)
        self.pushButtonAnnuler.setObjectName(_fromUtf8("pushButtonAnnuler"))
        self.horizontalLayout.addWidget(self.pushButtonAnnuler)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(rfSettingWindow)
        QtCore.QMetaObject.connectSlotsByName(rfSettingWindow)

    def retranslateUi(self, rfSettingWindow):
        rfSettingWindow.setWindowTitle(_translate("rfSettingWindow", "Parameters", None))
        self.label.setText(_translate("rfSettingWindow", "Max RF range (m)", None))
        self.label_2.setText(_translate("rfSettingWindow", "Number of nodes", None))
        self.pushButtonValider.setText(_translate("rfSettingWindow", "Valider", None))
        self.pushButtonAnnuler.setText(_translate("rfSettingWindow", "Annuler", None))

