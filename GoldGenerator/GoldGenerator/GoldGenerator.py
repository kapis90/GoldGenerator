import os
import re
import sys
from shutil import copyfile
from PyQt5 import QtCore, QtGui, QtWidgets
from GoldGeneratorForm import Ui_GoldGeneratorForm

class GoldGenerator(Ui_GoldGeneratorForm):
    
    def __init__(self, dialog):
        Ui_GoldGeneratorForm.__init__(self)
        self.setupUi(dialog)

        self.sourceBrowseButton.clicked.connect(self.browse_file)
        self.refsBrowseButton.clicked.connect(self.browse_dir)
        self.addButton.clicked.connect(self.browse_dirs)
        self.removeButton.clicked.connect(self.remove)
        self.generateButton.clicked.connect(self.generate)

    def console_message(self, message):
        self.consoleEdit.append(message)

    def browse_file(self):
        self.source = QtWidgets.QFileDialog.getOpenFileName(dialog, 'Open File', '', '')
        self.sourceEdit.setText(self.source[0])
  
    def browse_dir(self):
        self.refs = QtWidgets.QFileDialog.getExistingDirectory(dialog, 'Open directory', '', QtWidgets.QFileDialog.ShowDirsOnly)
        self.refsEdit.setText(self.refs)

    def browse_dirs(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(dialog, 'Point to local tests directory', '', QtWidgets.QFileDialog.ShowDirsOnly)
        self.test_names = [test for test in os.listdir(dir) if os.path.isdir(os.path.join(dir, test))]
        self.testListWidget.addItems(self.test_names)

    def remove(self):
        listItem = self.testListWidget.selectedItems()
        for item in listItem:
            self.testListWidget.takeItem(self.testListWidget.row(item))

    def generate(self):
        
        for item in [str(self.testListWidget.item(i).text()) for i in range(self.testListWidget.count())]:
            
            copyfile(self.sourceEdit.text(), self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + item + ".gold")
            self.console_message(item + " copied.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = GoldGenerator(dialog)
    dialog.show()
    sys.exit(app.exec_())