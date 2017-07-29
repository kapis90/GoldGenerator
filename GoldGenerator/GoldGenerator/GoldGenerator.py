import os
from pathlib import Path
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
        self.testsContainer = dict()

    def _validate(self):
        
        if self.sourceEdit.text() !="":
            source_flag = True 
        else:
            source_flag = False
            self.console_message("Source file cannot be empty", "ERROR")

        if self.refsEdit.text() !="":
            refs_flag = True
        else:
            refs_flag = False
            self.console_message("Refs directory cannot be empty", "ERROR")

        if self.gf_abrevEdit.text() !="":
            abrev_flag = True
        else:
            abrev_flag = False
            self.console_message("GF_ABREV cannot be empty", "ERROR")

        if self.testsContainer != {}:
            test_flag = True
        else:
            test_flag = False
            self.console_message("Test directories cannot be empty", "ERROR")

        return source_flag and refs_flag and abrev_flag and test_flag
        
        
            
        

    def console_message(self, message, severity=None):

        styles = {
                    "ERROR":"<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >" + message + "</span>", 
                    "WARRNING":"<span style=\" font-size:8pt; font-weight:600; color:#0000ff;\" >" + message + "</span>"}

        self.consoleEdit.append(styles.get(severity, message))

    def browse_file(self):
        self.source = QFileDialog.getOpenFileName(dialog, 'Open File', '', '')
        if self.source != "":
            self.sourceEdit.setText(self.source[0])
  
    def browse_dir(self):
        self.refs = QFileDialog.getExistingDirectory(dialog, 'Open directory', '', QFileDialog.ShowDirsOnly)
        if self.refs != "":
            self.refsEdit.setText(self.refs)

    def browse_dirs(self):

        tests_path = list()
        getOpenDirectories = getExistingDirectories()
        if getOpenDirectories.exec_():
            tests_path.extend(getOpenDirectories.selectedFiles())
            for path in tests_path:
                self.testsContainer[path] = os.path.basename(path)

            self.testListWidget.clear()
            self.testListWidget.insertItems(0, self.testsContainer.values())
            self.testListWidget.sortItems(Qt.AscendingOrder)
        
        #print(self.testsContainer)

    def remove(self):
        
        listItem = self.testListWidget.selectedItems()

        for item in listItem:
            
            test_name = self.testListWidget.takeItem(self.testListWidget.row(item)).text()
            self.testsContainer = {k:v for k,v in self.testsContainer.items() if v!=test_name}

        #print(self.testsContainer)

    def generate(self):

        if self._validate():
            if self.searchBox.isChecked():
                
                for test_path, name in self.testsContainer.items():
                    file_to_copy = Path(test_path + "/" + self.sourceEdit.text())

                    try:
                        copyfile(file_to_copy, self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + name + ".gold")
                    except (FileExistsError, FileNotFoundError) as error:
                        self.console_message("File " + str(file_to_copy) + " does not exists. ", "ERROR")
                        self.console_message("Gold generation for " + name + " has been skipped", "WARRNING")
                    else:
                        self.console_message("Gold file for test: " + name + " succesfully generated.")
            
            else:

                for path, name in self.testsContainer.items():
                    try:
                        copyfile(self.sourceEdit.text(), self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + name + ".gold")
                    except (FileExistsError, FileNotFoundError) as error:
                        self.console_message("File " + self.sourceEdit.text() + " does not exists. ", "ERROR")
                        self.console_message("Gold generation for " + name + " has been skipped", "WARRNING")
                    else:
                        self.console_message("Gold file for test: " + name + " succesfully generated.")

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