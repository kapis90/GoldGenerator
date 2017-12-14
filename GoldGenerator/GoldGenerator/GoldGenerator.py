import os.path
from os import remove
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
        
        # Connect signals
        self.sourceBrowseButton.clicked.connect(self.browse_file)
        self.refsBrowseButton.clicked.connect(self.browse_dir)
        self.addButton.clicked.connect(self.browse_dirs)
        self.removeButton.clicked.connect(lambda: self.remove(self.testListWidget.selectedItems()))
        self.generateButton.clicked.connect(self.generate)
        
        
        # Declare an empty container for tests
        self.testsContainer = dict()

    def _validate(self):
        """ Function to validate if all fields are filled up correctly. Return proper error to console if not """
        
        if self.sourceEdit.text() != "":
            source_flag = True 
        else:
            source_flag = False
            self.console_message("Source file cannot be empty", "ERROR")

        if self.refsEdit.text() != "":
            refs_flag = True
        else:
            refs_flag = False
            self.console_message("Refs directory cannot be empty", "ERROR")

        if self.gf_abrevEdit.text() != "":
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
        
    def _summary(self):
        counter = 0
        for i in range(0,self.testListWidget.count()):
            if self.testListWidget.item(i).foreground().color() == Qt.red:
                counter = counter + 1

        if counter:
            self.console_message("Number of failures: %s" % counter, "ERROR")
        else: 
            self.console_message("Generation complete successfully")

    def _getGreenItems(self):
        result = list()
        for i in range(0,self.testListWidget.count()):
            if self.testListWidget.item(i).foreground().color() == Qt.darkGreen:
                result.append(self.testListWidget.item(i))
        
        return result

    def console_message(self, message, severity="NORMAL"):
        """ Function to construct console message. Severity could be ERROR, WARNING or not specified. If not specifed its normal black text """

        styles = {
                    "ERROR":"<span style=\" font-size:8pt; color:#ff0000;\" >" + message + "</span>", 
                    "WARNING":"<span style=\" font-size:8pt; color:#0000ff;\" >" + message + "</span>",
                    "NORMAL":"<span style=\" font-size:8pt; color:#000000;\" >" + message + "</span>"}

        self.consoleEdit.append(styles.get(severity, message)) # message is a default key returned when severity is None (not found in styles dict)

    def browse_file(self):
        """ Function to fill up source file filed """

        self.source = QFileDialog.getOpenFileName(dialog, 'Open File', '', '')
        if self.source != "":
            self.sourceEdit.setText(self.source[0])

    def browse_dir(self):
        """ Function to fill up refs dir filed """

        self.refs = QFileDialog.getExistingDirectory(dialog, 'Open directory', '', QFileDialog.ShowDirsOnly)
        if self.refs != "":
            self.refsEdit.setText(self.refs)

    def browse_dirs(self):
        """ Function to select test directories """

        tests_path = list()
        getOpenDirectories = getExistingDirectories()
        if getOpenDirectories.exec_():
            tests_path.extend(getOpenDirectories.selectedFiles())
        # Creation of testContainer as dict with path as keys and test_name as values
            for path in tests_path:
                self.testsContainer[path] = os.path.basename(path)

            # Do not change already exists items (preserve colors)
            for path, name in self.testsContainer.items():
                if not self.testListWidget.findItems(name,Qt.MatchExactly):
                    self.testListWidget.addItem(name)
            
            self.testListWidget.sortItems(Qt.AscendingOrder)
        

    def remove(self, testListWidgetItemList):
        """ Function to remove selected test directories """

        for item in testListWidgetItemList:
            
            test_name = self.testListWidget.takeItem(self.testListWidget.row(item)).text()
            # Create new testsContainer without 'test_name'
            self.testsContainer = {path:name for path,name in self.testsContainer.items() if name != test_name}

    def generate(self):
        """ Main function to generate golds
            
            1. Validate all fields
            2. Depend on 'Search for result' checkbox:
                - enabled:
                    Try to copy file from test dir and throws error if it's not found. Give it correct gold name (GF_ABREV.TEST_NAME.gold)
                    Also colorize items in the list and remove original file after copy
                - disabled:
                    Try to copy selected file to refs directory and throws error if it's not found. Give it correct gold name (GF_ABREV.TEST_NAME.gold)
                    Also colorize items in the list
        """
        
        # Validation if all fileds filed up
        if self._validate():
            # 'Check of result' is checked
            if self.searchBox.isChecked():
                
                # Join paths for each test, copy to refs dir and delete file
                for test_path, name in self.testsContainer.items():
                    file_to_copy = Path(test_path + "/" + self.sourceEdit.text())
                    # If item color is darkGreen that means gold was already generated correctly in previous iteration
                    if self.testListWidget.findItems(name,Qt.MatchExactly)[0].foreground().color() != Qt.darkGreen:
                        try:
                            copyfile(file_to_copy, self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + name + ".gold")
                            os.remove(file_to_copy)
                        except (FileExistsError, FileNotFoundError) as error:
                            self.console_message("File " + str(file_to_copy) + " does not exists. ", "ERROR")
                            self.console_message("Gold generation for " + name + " has been skipped", "WARNING")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.red)
                        except Exception as error:
                            self.console_message(str(error), "ERROR")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.red)
                        else:
                            self.console_message("Gold file for test: " + name + " succesfully generated.")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.darkGreen)
                            

            # Copy specified file for all tests to refs dir
            else:
                for path, name in self.testsContainer.items():
                    # If item color is darkGreen that means gold was already generated correctly in previous iteration
                    if self.testListWidget.findItems(name,Qt.MatchExactly)[0].foreground().color() != Qt.darkGreen:
                        try:
                            copyfile(self.sourceEdit.text(), self.refsEdit.text() + "/" + self.gf_abrevEdit.text() + "." + name + ".gold")
                        except (FileExistsError, FileNotFoundError) as error:
                            self.console_message("File " + self.sourceEdit.text() + " does not exists. ", "ERROR")
                            self.console_message("Gold generation for " + name + " has been skipped", "WARNING")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.red)
                        except Exception as error:
                            self.console_message(str(error), "ERROR")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.red)
                        else:
                            self.console_message("Gold file for test: " + name + " succesfully generated.")
                            self.testListWidget.findItems(name, Qt.MatchExactly)[0].setForeground(Qt.darkGreen)
            # If checkbox 'Keep Failures Only' is checked then delete all green (successfuly generated golds) tests
            if self.keepFailuresBox.isChecked():
                self.remove(self._getGreenItems())            
            self._summary()

class getExistingDirectories(QFileDialog):
    """ Overloaded class for selecting tests dialog (to handle multiselection of dirs) """

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
    dialog.setWindowIcon(QIcon('./GoldGenerator.ico'))
    prog = GoldGenerator(dialog)
    dialog.show()
    sys.exit(app.exec_())