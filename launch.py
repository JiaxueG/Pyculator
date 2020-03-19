import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Pyculator import *
from PyQt5.QtCore import Qt, pyqtSlot

class launchPyculator(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.basicUi()
    
    def basicUi(self): 
        self.ui.status=self.statusBar()
        self.ui.status.showMessage("Pyculator 0.1 by JiaxueG")

if __name__=="__main__": 
    app = QApplication(sys.argv)
    myWin = launchPyculator()
    myWin.show()
    sys.exit(app.exec_())
