import sys
from os import path as pth

# Instruments .. 
sys.path.append(pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__))))))

# SubSubwindows
sys.path.append(pth.dirname(pth.dirname(pth.abspath(__file__))))


from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)


from AbstractSubSubwindow import Abs_SubSubwindow



from Instruments.Subplots import runSubplots
from Instruments.MyWidgets.MyWidgets import MyTableWidget





class Subplotswindow(Abs_SubSubwindow):
    def __init__(self) -> None:
        super().__init__()

        self.add_Table()

    
    def ini_gui(self):
        super().ini_gui()
        self.setGeometry(300,300,450,300)
        self.setWindowTitle("Subplots")
    
    def add_Table(self):
        self.table  = MyTableWidget()
        # table.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.table.setRowCount(10)
        self.table.setColumnCount(10)

        for row in range(10):
            for col in range(10):
                item = QTableWidgetItem("")
                self.table.setItem(row,col,item)
        
        #create a button to run
        runbutton =  QPushButton("OK")
        runbutton.clicked.connect(self.runbutton_clicked)

        #set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(runbutton)
        self.setLayout(layout)

        

    
    def runbutton_clicked(self):
        lst = []
        for row in range(10):
            row_lst = []
            for col in range(10):
                text = self.table.item(row,col).text()
                if len(text) != 0:
                    row_lst.append(int(self.table.item(row,col).text()))
            if len(row_lst) != 0:        
                lst.append(row_lst)
        
        runSubplots(lst)