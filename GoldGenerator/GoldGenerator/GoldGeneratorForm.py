# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kapis\Source\Repos\GoldGenerator\GoldGenerator\GoldGenerator\UI\GoldGeneratorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoldGeneratorForm(object):
    def setupUi(self, GoldGeneratorForm):
        GoldGeneratorForm.setObjectName("GoldGeneratorForm")
        GoldGeneratorForm.setEnabled(True)
        GoldGeneratorForm.resize(665, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GoldGeneratorForm.sizePolicy().hasHeightForWidth())
        GoldGeneratorForm.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(GoldGeneratorForm)
        self.groupBox.setGeometry(QtCore.QRect(2, 348, 661, 160))
        self.groupBox.setObjectName("groupBox")
        self.consoleEdit = QtWidgets.QTextEdit(self.groupBox)
        self.consoleEdit.setGeometry(QtCore.QRect(4, 15, 653, 141))
        self.consoleEdit.setReadOnly(True)
        self.consoleEdit.setObjectName("consoleEdit")
        self.dirLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.dirLabel.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.dirLabel.setObjectName("dirLabel")
        self.testListWidget = QtWidgets.QListWidget(GoldGeneratorForm)
        self.testListWidget.setGeometry(QtCore.QRect(92, 110, 467, 209))
        self.testListWidget.setObjectName("testListWidget")
        self.testListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.generateButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.generateButton.setGeometry(QtCore.QRect(290, 326, 75, 23))
        self.generateButton.setCheckable(False)
        self.generateButton.setAutoDefault(False)
        self.generateButton.setDefault(False)
        self.generateButton.setFlat(False)
        self.generateButton.setObjectName("generateButton")
        self.line = QtWidgets.QFrame(GoldGeneratorForm)
        self.line.setGeometry(QtCore.QRect(8, 100, 650, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.refsLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.refsLabel.setGeometry(QtCore.QRect(10, 40, 72, 16))
        self.refsLabel.setMinimumSize(QtCore.QSize(70, 0))
        self.refsLabel.setObjectName("refsLabel")
        self.refsEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.refsEdit.setGeometry(QtCore.QRect(90, 40, 467, 20))
        self.refsEdit.setObjectName("refsEdit")
        self.refsBrowseButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.refsBrowseButton.setGeometry(QtCore.QRect(576, 39, 75, 23))
        self.refsBrowseButton.setObjectName("refsBrowseButton")
        self.sourceLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.sourceLabel.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.sourceLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.sourceLabel.setObjectName("sourceLabel")
        self.sourceEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.sourceEdit.setEnabled(True)
        self.sourceEdit.setGeometry(QtCore.QRect(90, 10, 467, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceEdit.sizePolicy().hasHeightForWidth())
        self.sourceEdit.setSizePolicy(sizePolicy)
        self.sourceEdit.setObjectName("sourceEdit")
        self.sourceBrowseButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.sourceBrowseButton.setGeometry(QtCore.QRect(576, 10, 75, 23))
        self.sourceBrowseButton.setObjectName("sourceBrowseButton")
        self.gf_abrevLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.gf_abrevLabel.setGeometry(QtCore.QRect(10, 70, 75, 16))
        self.gf_abrevLabel.setMinimumSize(QtCore.QSize(75, 0))
        self.gf_abrevLabel.setObjectName("gf_abrevLabel")
        self.gf_abrevEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.gf_abrevEdit.setGeometry(QtCore.QRect(90, 70, 132, 20))
        self.gf_abrevEdit.setObjectName("gf_abrevEdit")
        self.addButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.addButton.setGeometry(QtCore.QRect(576, 110, 75, 23))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.removeButton.setGeometry(QtCore.QRect(576, 140, 75, 23))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(GoldGeneratorForm)
        QtCore.QMetaObject.connectSlotsByName(GoldGeneratorForm)
        GoldGeneratorForm.setTabOrder(self.sourceEdit, self.sourceBrowseButton)
        GoldGeneratorForm.setTabOrder(self.sourceBrowseButton, self.addButton)
        GoldGeneratorForm.setTabOrder(self.addButton, self.testListWidget)
        GoldGeneratorForm.setTabOrder(self.testListWidget, self.removeButton)
        GoldGeneratorForm.setTabOrder(self.removeButton, self.generateButton)
        GoldGeneratorForm.setTabOrder(self.generateButton, self.consoleEdit)

    def retranslateUi(self, GoldGeneratorForm):
        _translate = QtCore.QCoreApplication.translate
        GoldGeneratorForm.setWindowTitle(_translate("GoldGeneratorForm", "Gold Generator"))
        self.groupBox.setTitle(_translate("GoldGeneratorForm", "Console"))
        self.dirLabel.setText(_translate("GoldGeneratorForm", "Directories:"))
        self.generateButton.setText(_translate("GoldGeneratorForm", "Generate"))
        self.refsLabel.setText(_translate("GoldGeneratorForm", "Refs directory:"))
        self.refsBrowseButton.setText(_translate("GoldGeneratorForm", "Browse"))
        self.sourceLabel.setText(_translate("GoldGeneratorForm", "Source file:"))
        self.sourceBrowseButton.setText(_translate("GoldGeneratorForm", "Browse"))
        self.gf_abrevLabel.setText(_translate("GoldGeneratorForm", "GF_ABREV:"))
        self.addButton.setText(_translate("GoldGeneratorForm", "Add..."))
        self.removeButton.setText(_translate("GoldGeneratorForm", "Remove"))

