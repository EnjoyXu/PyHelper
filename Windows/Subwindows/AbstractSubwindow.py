import sys
from os import path
from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)


class Abs_Subwindow(QDialog):
    '''
    Abstract Subwindow
    '''
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300,800)
        self.ini_gui()
        self.add_exit_button()
        


        
    def ini_gui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(r".\Instruments\Icon\pyhelper.png"))

        
    
    def add_grid_group_box(self):
        pass

    def add_exit_button(self):
        self.exit_button = QPushButton("Back")
        self.exit_button.clicked.connect(self.accept)
        

    #----------move--------------------
    def mousePressEvent(self, event:QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_dragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        
    def mouseReleaseEvent(self,event:QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_dragPosition)
            event.accept()
    #-----------------------------------