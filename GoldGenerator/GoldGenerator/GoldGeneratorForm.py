# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kkoltons\Source\Repos\GoldGenerator\GoldGenerator\GoldGenerator\UI\GoldGeneratorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoldGeneratorForm(object):
    def setupUi(self, GoldGeneratorForm):
        GoldGeneratorForm.setObjectName("GoldGeneratorForm")
        GoldGeneratorForm.setEnabled(True)
        GoldGeneratorForm.resize(638, 638)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GoldGeneratorForm.sizePolicy().hasHeightForWidth())
        GoldGeneratorForm.setSizePolicy(sizePolicy)
        GoldGeneratorForm.setBaseSize(QtCore.QSize(0, 200))
        self.gridLayout_2 = QtWidgets.QGridLayout(GoldGeneratorForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.testListWidget = QtWidgets.QListWidget(GoldGeneratorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testListWidget.sizePolicy().hasHeightForWidth())
        self.testListWidget.setSizePolicy(sizePolicy)
        self.testListWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.testListWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.testListWidget.setDragEnabled(False)
        self.testListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.testListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.testListWidget.setObjectName("testListWidget")
        self.gridLayout_2.addWidget(self.testListWidget, 5, 1, 7, 2)
        self.generateButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.generateButton.setCheckable(False)
        self.generateButton.setAutoDefault(False)
        self.generateButton.setDefault(False)
        self.generateButton.setFlat(False)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout_2.addWidget(self.generateButton, 11, 3, 1, 1)
        self.refsLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.refsLabel.setMinimumSize(QtCore.QSize(70, 0))
        self.refsLabel.setObjectName("refsLabel")
        self.gridLayout_2.addWidget(self.refsLabel, 2, 0, 1, 1)
        self.refsEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.refsEdit.setObjectName("refsEdit")
        self.gridLayout_2.addWidget(self.refsEdit, 2, 1, 1, 2)
        self.sourceBrowseButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.sourceBrowseButton.setObjectName("sourceBrowseButton")
        self.gridLayout_2.addWidget(self.sourceBrowseButton, 1, 3, 1, 1)
        self.addButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.addButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(112, 23))
        self.addButton.setObjectName("addButton")
        self.gridLayout_2.addWidget(self.addButton, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox = QtWidgets.QGroupBox(GoldGeneratorForm)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.consoleEdit = QtWidgets.QTextEdit(self.groupBox)
        self.consoleEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.consoleEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.consoleEdit.setReadOnly(True)
        self.consoleEdit.setObjectName("consoleEdit")
        self.verticalLayout.addWidget(self.consoleEdit)
        self.gridLayout_2.addWidget(self.groupBox, 12, 0, 1, 4)
        self.removeButton = QtWidgets.QPushButton(GoldGeneratorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_2.addWidget(self.removeButton, 6, 3, 1, 1)
        self.line = QtWidgets.QFrame(GoldGeneratorForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 4)
        self.gf_abrevEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.gf_abrevEdit.setObjectName("gf_abrevEdit")
        self.gridLayout_2.addWidget(self.gf_abrevEdit, 3, 1, 1, 1)
        self.gf_abrevLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.gf_abrevLabel.setMinimumSize(QtCore.QSize(75, 0))
        self.gf_abrevLabel.setObjectName("gf_abrevLabel")
        self.gridLayout_2.addWidget(self.gf_abrevLabel, 3, 0, 1, 1)
        self.dirLabel = QtWidgets.QLabel(GoldGeneratorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dirLabel.sizePolicy().hasHeightForWidth())
        self.dirLabel.setSizePolicy(sizePolicy)
        self.dirLabel.setObjectName("dirLabel")
        self.gridLayout_2.addWidget(self.dirLabel, 5, 0, 1, 1)
        self.refsBrowseButton = QtWidgets.QPushButton(GoldGeneratorForm)
        self.refsBrowseButton.setObjectName("refsBrowseButton")
        self.gridLayout_2.addWidget(self.refsBrowseButton, 2, 3, 1, 1)
        self.sourceLabel = QtWidgets.QLabel(GoldGeneratorForm)
        self.sourceLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.sourceLabel.setObjectName("sourceLabel")
        self.gridLayout_2.addWidget(self.sourceLabel, 1, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(GoldGeneratorForm)
        self.sourceEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceEdit.sizePolicy().hasHeightForWidth())
        self.sourceEdit.setSizePolicy(sizePolicy)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridLayout_2.addWidget(self.sourceEdit, 1, 1, 1, 2)
        self.searchBox = QtWidgets.QCheckBox(GoldGeneratorForm)
        self.searchBox.setObjectName("searchBox")
        self.gridLayout_2.addWidget(self.searchBox, 0, 0, 1, 2)
        self.keepFailuresBox = QtWidgets.QCheckBox(GoldGeneratorForm)
        self.keepFailuresBox.setObjectName("keepFailuresBox")
        self.gridLayout_2.addWidget(self.keepFailuresBox, 10, 3, 1, 1)

        self.retranslateUi(GoldGeneratorForm)
        self.searchBox.toggled['bool'].connect(self.sourceBrowseButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(GoldGeneratorForm)
        self.consoleEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.consoleEdit.customContextMenuRequested.connect(self.openMenu)
        GoldGeneratorForm.setTabOrder(self.searchBox, self.sourceEdit)
        GoldGeneratorForm.setTabOrder(self.sourceEdit, self.sourceBrowseButton)
        GoldGeneratorForm.setTabOrder(self.sourceBrowseButton, self.refsEdit)
        GoldGeneratorForm.setTabOrder(self.refsEdit, self.refsBrowseButton)
        GoldGeneratorForm.setTabOrder(self.refsBrowseButton, self.gf_abrevEdit)
        GoldGeneratorForm.setTabOrder(self.gf_abrevEdit, self.testListWidget)
        GoldGeneratorForm.setTabOrder(self.testListWidget, self.consoleEdit)

    def retranslateUi(self, GoldGeneratorForm):
        _translate = QtCore.QCoreApplication.translate
        GoldGeneratorForm.setWindowTitle(_translate("GoldGeneratorForm", "Gold Generator"))
        self.generateButton.setText(_translate("GoldGeneratorForm", "Generate"))
        self.refsLabel.setText(_translate("GoldGeneratorForm", "Refs directory:"))
        self.sourceBrowseButton.setText(_translate("GoldGeneratorForm", "Browse"))
        self.addButton.setText(_translate("GoldGeneratorForm", "Add..."))
        self.groupBox.setTitle(_translate("GoldGeneratorForm", "Console"))
        self.removeButton.setText(_translate("GoldGeneratorForm", "Remove"))
        self.gf_abrevLabel.setText(_translate("GoldGeneratorForm", "GF_ABREV:"))
        self.dirLabel.setText(_translate("GoldGeneratorForm", "Directories:"))
        self.refsBrowseButton.setText(_translate("GoldGeneratorForm", "Browse"))
        self.sourceLabel.setText(_translate("GoldGeneratorForm", "Source file:"))
        self.searchBox.setText(_translate("GoldGeneratorForm", "Search for result"))
        self.keepFailuresBox.setText(_translate("GoldGeneratorForm", "Keep Failures Only"))
        self.generateButton.setText(_translate("GoldGeneratorForm", "Generate"))
		
    def openMenu(self, position):
        
        menu = QtWidgets.QMenu()
        clearAction = menu.addAction("Clear All")
        action = menu.exec_(self.consoleEdit.mapToGlobal(position))
        if action == clearAction:
            self.consoleEdit.clear()



