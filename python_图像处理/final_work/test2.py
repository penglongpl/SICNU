import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        helpMenu.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
        self.show()
    
    def test(self):
        QMessageBox.information(None, "提示",
        "这是来自wjsaya(sayawj@163.com)的测试消息\n\n"
        "支持使用\\n换行\n"
        "调用方法: QtWidgets.QMessageBox.information"
        )
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())