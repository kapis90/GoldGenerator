import os
import re
import sys
from shutil import copyfile
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
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
        self.testsContainer = list()

    def _path_exist(self, path):
        for test in self.testsContainer:
            if test["name"]==os.path.basename(path):
                return True

    def console_message(self, message, severity=None):

        styles = {
                    "ERROR":"<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >" + message + "</span>", 
                    "WARRNING":"<span style=\" font-size:8pt; font-weight:600; color:#0000ff;\" >" + message + "</span>"}

        self.consoleEdit.append(styles.get(severity, message))

    def browse_file(self):
        self.source = QFileDialog.getOpenFileName(dialog, 'Open File', '', '')
        self.sourceEdit.setText(self.source[0])
  
    def browse_dir(self):
        self.refs = QFileDialog.getExistingDirectory(dialog, 'Open directory', '', QFileDialog.ShowDirsOnly)
        self.refsEdit.setText(self.refs)

    def browse_dirs(self):

        tests = list()
        getOpenDirectories = getExistingDirectories()
        if getOpenDirectories.exec_():
            tests.extend(getOpenDirectories.selectedFiles())
            tests = sorted(set(tests))
            for test in tests:
                if (not self._path_exist(test)):
                    self.testsContainer.append({"full_path":test, "name":os.path.basename(test)})
                    self.testListWidget.insertItem(0, os.path.basename(test))
                else:
                    self.console_message("Test is already on the list: " + os.path.basename(test) + " has been skipped", "WARRNING")
            self.testListWidget.sortItems(Qt.AscendingOrder)
        
        print(self.testsContainer)

    def remove(self):
        indexToRemove = list()
        listItem = self.testListWidget.selectedItems()
        for item in listItem:
            test_name = self.testListWidget.takeItem(self.testListWidget.row(item)).text()
            for i in range(len(self.testsContainer)):
                if self.testsContainer[i]["name"]==test_name:
                    indexToRemove.append(i)

            for item in indexToRemove:
                del self.testsContainer[item]
            del indexToRemove[:]
            print(self.testsContainer)

    def generate(self):
        
        for item in [str(self.testListWidget.item(i).text()) for i in range(self.testListWidget.count())]:
            
            copyfile(self.sourceEdit.text(), self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + item + ".gold")
            self.console_message("Gold file for test: " + item + " succesfully generated.")

class getExistingDirectories(QFileDialog):
    def __init__(self, *args):
        super(getExistingDirectories, self).__init__(*args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.Directory)
        self.setOption(self.ShowDirsOnly, True)
        self.findChildren(QListView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.findChildren(QTreeView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    prog = GoldGenerator(dialog)
    dialog.show()
    sys.exit(app.exec_())