from Windows.SubSubwindows.Re import *
import sys
from os import path as pth

sys.path.append(pth.dirname(pth.dirname(pth.abspath(__file__))))

from SubSubwindows.Re.Re import *


from PySide6.QtWidgets import (QGridLayout, QGroupBox, QPushButton,
                                QVBoxLayout)

from .AbstractSubwindow import Abs_Subwindow


class Rewindow(Abs_Subwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()

        self.add_grid_group_box()

        #set layout
        layout = QVBoxLayout()
        layout.addWidget(self._grid_group_box)

        self.setLayout(layout)
    


    def ini_gui(self):
        super().ini_gui()
        self.setWindowTitle("Re")
        

    def add_grid_group_box(self):
        self._grid_group_box = QGroupBox("Re")
        #------------------------------------------------------------
        #create buttons
        #bt 1 Match
        _Match = QPushButton("Match")
        _Match.clicked.connect(self.Match_clicked)



        #------------------------------------------------------------
        #set layout
        layout = QGridLayout()
        layout.addWidget(_Match,0,0)


        layout.addWidget(self._exit_button)

        
        self._grid_group_box.setLayout(layout)
        


    def Match_clicked(self):
        matchwindow = Matchwindow()
        matchwindow.center()
        
        matchwindow.show()
        matchwindow.exec()




