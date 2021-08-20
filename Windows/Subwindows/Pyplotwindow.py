import sys
from os import path as pth

sys.path.append(pth.dirname(pth.dirname(pth.abspath(__file__))))
# print(sys.path)

from SubSubwindows.Pyplot.Pyplot import *

from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)



from .AbstractSubwindow import Abs_Subwindow


class Pyplotwindow(Abs_Subwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()
        
        self.add_grid_group_box()

        #set layout
        layout = QVBoxLayout()
        layout.addWidget(self.grid_group_box)

        self.setLayout(layout)

    def ini_gui(self):
        super().ini_gui()
        self.setWindowTitle("Pyplot")
    
    def add_grid_group_box(self):
        self.grid_group_box = QGroupBox("Pyplot")
        #------------------------------------------------------------
        #create buttons
        #bt 1 Subplots
        Subplots = QPushButton("Subplots")
        Subplots.clicked.connect(self.Subplots_clicked)

        #bt 2 PlotSet
        Plotset = QPushButton("Plot Setting")
        Plotset.clicked.connect(self.PlotSet_clicked)


        
        #------------------------------------------------------------
        #set layout
        layout = QGridLayout()
        layout.addWidget(Subplots,0,0)
        layout.addWidget(Plotset,0,1)


        layout.addWidget(self.exit_button,1,0,1,2)

        self.grid_group_box.setLayout(layout)

    def Subplots_clicked(self):
        subplotwindow = Subplotswindow()
        subplotwindow.center()

        subplotwindow.show()
        subplotwindow.exec()

    def PlotSet_clicked(self):
        plotsetwindow = PlotSetwindow()
        plotsetwindow.center()

        plotsetwindow.show()
        plotsetwindow.exec()

    

   