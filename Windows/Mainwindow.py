import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QApplication, QDialog,
                               QGridLayout, QGroupBox,QDialogButtonBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)
from PySide6.QtGui import QCursor, QMouseEvent, QIcon,QScreen
from PySide6.QtUiTools import QUiLoader
from os import path as pth

#import Subwindows
sys.path.append(  pth.dirname( pth.abspath(__file__) ) ) 




from Subwindows.Subwindows import *


class Mainwindow(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.ini_gui()


        self.add_grid_group_box()
        self.setCentralWidget(self._grid_group_box)
        

        #Layout for Mainwindow
        # main_layout  = QVBoxLayout()
        # main_layout.addWidget(self._grid_group_box)
        
        
        # self.setLayout(main_layout)
    

    def ini_gui(self):
        #set title
        self.setWindowTitle("PyHelper") 
        self.setFixedSize(300,800)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # iconpath = pth.abspath(r".\Instruments\Icon\pyhelper.png")
        self.setWindowIcon(QIcon(r".\Instruments\Icon\pyhelper.png"))


    def center(self):
        cp = QScreen.availableGeometry(QApplication.primaryScreen()).topRight()
        qr = self.frameGeometry()
        qr.moveTopRight(cp)
        self.move(qr.topLeft())
    

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

    def add_grid_group_box(self):
        self._grid_group_box = QGroupBox("Main window")
        #------------------------------------------------------------
        #create buttons
        #bt 1 Pyplot
        self._Pyplot = QPushButton("Pyplot")
        self._Pyplot.clicked.connect(lambda:self.Mainbutton_clicked("Pyplotwindow"))

        #bt_2 Re
        self._Re = QPushButton("Re")
        self._Re.clicked.connect(lambda:self.Mainbutton_clicked("Rewindow"))

        #bt_3 Latex
        self._Latex = QPushButton("Latex")
        self._Latex.clicked.connect(lambda:self.Mainbutton_clicked("Latexwindow"))

        #bt Exit
        self._exit_button = QPushButton("Exit")
        self._exit_button.clicked.connect(lambda : self.close())
        
        


        #------------------------------------------------------------

        #set layout 
        layout =  QGridLayout()
        layout.addWidget(self._Pyplot,0,0)
        layout.addWidget(self._Re,0,1)
        layout.addWidget(self._Latex,1,0)


        layout.addWidget(self._exit_button,2,0,1,2)

        self._grid_group_box.setLayout(layout)
    

    
        

    
    #Button clicked functions
    def Mainbutton_clicked(self,name):
        self.hide()

        exec("qr1 = self.frameGeometry()")
        #Create a subwindow
        exec("Subwindow = %s()"%name) 
        exec("Subwindow.move(qr1.topLeft())" )
        exec("Subwindow.show()")
        exec("Subwindow.exec()")
        exec("qr2 = Subwindow.frameGeometry()")
        exec("self.move(qr2.topLeft())")

        self.show()