import sys
from os import path as pth

sys.path.append(pth.dirname(pth.dirname(pth.abspath(__file__))))

from SubSubwindows.Latex.Latex import *


from PySide6.QtWidgets import (QGridLayout, QGroupBox, QPushButton,
                                QVBoxLayout)

from .AbstractSubwindow import Abs_Subwindow


class Latexwindow(Abs_Subwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()
        self.add_grid_group_box()
        self.add_exit_button()

        layout = QVBoxLayout()
        layout.addWidget(self._grid_group_box)



        self.setLayout(layout)


    
    def ini_gui(self):
        super().ini_gui()
        self.setWindowTitle("Latex")


    def add_grid_group_box(self):
        self._grid_group_box = QGroupBox("Latex")

        self._Hotkey = QPushButton("Hotkey")
        self._Hotkey.clicked.connect(self.Hotkey_clicked)

        
        

        #set layout
        layout = QGridLayout()
        layout.addWidget(self._Hotkey,0,0,1,1)
        layout.addWidget(self._exit_button,1,0,1,2)

        self._grid_group_box.setLayout(layout)

    
    def Hotkey_clicked(self):
        hotkeywindow = Hotkeywindow()

        hotkeywindow.show()
        hotkeywindow.exec()

