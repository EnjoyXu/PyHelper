import sys
from os import path
from xml.etree.ElementTree import Element
from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon,QPalette
from PySide6.QtCore import QLine, Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox, QComboBox, QDialog,QColorDialog,
                               QDialogButtonBox, QFileDialog, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox, QStackedWidget, QTabWidget,
                               QTextEdit, QToolButton, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)



class Abs_SubSubwindow(QDialog):
    '''
    Abstract SubSubwindow
    '''
    def __init__(self, ) -> None:
        super().__init__()
        self.ini_gui()
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint)
        self.setWindowIcon(QIcon(r".\Instruments\Icon\pyhelper.png"))
        self.center()

    def ini_gui(self):
        pass

    
    def center(self):
        cp = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        qr = self.frameGeometry()
        qr.moveCenter(cp)
        self.move(qr.topLeft())