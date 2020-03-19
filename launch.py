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
        self.ui.PBTNcalculate.clicked.connect(self.calculate)
        self.ui.PBTNclear.clicked.connect(self.clear)
        self.ui.listWidget.itemDoubleClicked.connect(self.copyHis)
        self.ui.PBTNhisclear.clicked.connect(self.clearHis)

    def basicUi(self): 
        self.ui.status=self.statusBar()
        self.ui.status.showMessage("Pyculator 0.1 by JiaxueG")

    def clear(self): 
        self.ui.lcdNumber.display("0")
        self.ui.lineEdit.clear()

    def calculate(self): 
        text=self.ui.lineEdit.text()
        try:
            result = eval(text)
            self.ui.lcdNumber.display(str(result))
            self.ui.listWidget.addItem(text)
            self.ui.lineEdit.clear()
        except:
            self.ui.lcdNumber.display("Err")

    def copyHis(self, item): 
        content=item.text()
        self.ui.lineEdit.setText(content)
        result = eval(content)
        self.ui.lcdNumber.display(str(result))

    def clearHis(self): 
        self.ui.listWidget.clear()


if __name__=="__main__": 
    app = QApplication(sys.argv)
    myWin = launchPyculator()
    myWin.show()
    sys.exit(app.exec_())
