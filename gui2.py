from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QPushButton as Button
from PyQt5.QtWidgets import QVBoxLayout as VertBox
    
from PyQt5 import QtCore as Core, QtGui as Gui, QtWidgets as Widg, uic
from PyQt5.QtCore import Qt
import sys

class MainWindow(Widg.QMainWindow):
    def __init__(self):
        super().__init__()
        #main components
        self.layout = VertBox()
        self.label = Label()
        # self.Setlayout(self.layout)

app = Widg.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()