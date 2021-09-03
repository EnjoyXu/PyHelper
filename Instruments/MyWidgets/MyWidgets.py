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



class MyTableWidget(QTableWidget):
    '''
    Enable: edit multiselected values
    '''
    def commitData(self, editor):
        
        # call parent commitData first
        super(QTableWidget, self).commitData(editor)
        
        theModel = self.currentIndex().model()

        value = theModel.data(self.currentIndex(), Qt.EditRole)
        # curRow, curCol = self.currentIndex().row(), self.currentIndex().column()

        for itemRange in self.selectionModel().selection():
            
            for idx in itemRange.indexes():
                self.setItem(idx.row(),idx.column(),QTableWidgetItem(value))


class MyTabWidget(QTabWidget):
    def __init__(self, ) -> None:
        super().__init__()
        self.ini_gui()

        self.add_Tab1()
        self.add_Tab2()
        self.add_Tab3()

    def ini_gui(self):
        # self.setFixedSize(350,400)
        pass
        
    def add_Tab1(self):
        #figure_settings
        self.fig_settings = QWidget()

        #add widget
        self.title = QLineEdit()
        self.set_color = QPushButton()
        self.set_color.clicked.connect(lambda :self.set_color_clicked("set_color","plot_color"))

        self.grid = QCheckBox("Grid")
        self.grid.setChecked(False)
        
        self.grid_linestyle_label = QLabel("Linestyle")
        self.grid_linestyle = QComboBox()
        self.grid_linestyle.addItems(['"solid"','"dashed"','"dashdot"','"dotted"','"None"'])
        self.grid_linestyle.hide()
        self.grid_linestyle_label.hide()


        self.grid_linewidth_label = QLabel("Linewidth")
        self.grid_linewidth_label.hide()
        self.grid_linewidth = QLineEdit()
        self.grid_linewidth.hide()

        self.grid_color_label = QLabel("Color")
        self.grid_set_color = QPushButton()
        self.grid_set_color.clicked.connect(lambda :self.set_color_clicked("grid_set_color","grid_plot_color"))
        self.grid_color_label.hide()
        self.grid_set_color.hide()

        self.grid.stateChanged.connect(self.grid_check)
        




        #set layout
        layout = QGridLayout()

        layout.addWidget(QLabel("Title"),0,0)
        layout.addWidget(self.title,0,1)
        layout.addWidget(QLabel("Color:"),0,2)
        layout.addWidget(self.set_color,0,3)
        layout.addWidget(self.grid,1,0)
        
        layout.addWidget(self.grid_linestyle_label,2,0)
        layout.addWidget(self.grid_linestyle,2,1)

        layout.addWidget(self.grid_linewidth_label,2,2)
        layout.addWidget(self.grid_linewidth,2,3)

        layout.addWidget(self.grid_color_label,3,0)
        layout.addWidget(self.grid_set_color,3,1)


        

        self.fig_settings.setLayout(layout)

        #add Tab
        self.addTab(self.fig_settings,"Figure")

    def set_color_clicked(self,set_color,color):
        exec("self.%s = QColorDialog.getColor()" % color)
        
        exec("""
if self.%s.isValid():
    self.%s.setStyleSheet("background-color:rgb"+\
        str(self.%s.getRgb()[:3]))
        """%(color,set_color,color))
        

    def grid_check(self):
        check = ".show()" if self.grid.isChecked() else ".hide()"
        name_lst = ["grid_linestyle_label","grid_linestyle","grid_linewidth_label","grid_linewidth",\
            "grid_color_label","grid_set_color"]

        for name in name_lst:
            m = "self."+name+check
            exec(m)

        

            

    def add_Tab2(self):
        #axis_settings
        self.axis_settings = QWidget()
        
        #add widget
        self.x_label = QLineEdit()
        self.hide_x = QCheckBox("Hide X")
        self.hide_x.setChecked(False)
        self.xtick = QLineEdit()


        self.y_label = QLineEdit()
        self.hide_y = QCheckBox("Hide Y")
        self.hide_y.setChecked(False)
        self.ytick = QLineEdit()

        #set layout
        layout = QGridLayout()

        layout.addWidget(QLabel("Xlabel:"),0,0)
        layout.addWidget(self.x_label,0,1)
        layout.addWidget(self.hide_x,0,2)

        layout.addWidget(QLabel("X tick:"),1,0)
        layout.addWidget(self.xtick,1,1)
        

        layout.addWidget(QLabel("Ylabel:"),2,0)
        layout.addWidget(self.y_label,2,1)
        layout.addWidget(self.hide_y,2,2)

        layout.addWidget(QLabel("Y tick:"),3,0)
        layout.addWidget(self.ytick,3,1)


        self.axis_settings.setLayout(layout)

        #add tab
        self.addTab(self.axis_settings,"Axis")


    def add_Tab3(self):
        #Other settings
        self.other_settings = QWidget()

        #add widget
        self.path = QLineEdit()
        self.path_select = QPushButton("...")
        self.path_select.setFixedSize(30,30)
        self.path_select.clicked.connect(self.path_select_clicked)

        self.dpi = QLineEdit()



        #set layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Save Figure Path:"),0,0)
        layout.addWidget(self.path,0,1,1,2)
        layout.addWidget(self.path_select,0,3)
        
        layout.addWidget(QLabel("dpi:"),1,0,1,1)
        layout.addWidget(self.dpi,1,1,1,1)

        self.other_settings.setLayout(layout)

        #add tab
        self.addTab(self.other_settings,"Others")
    

    def path_select_clicked(self):
        path = QFileDialog.getSaveFileName()
        # print(path)
        self.path.setText(path[0])





class MatchTabWidge(QTabWidget):
    def __init__(self,) -> None:
        super().__init__()

        self.add_Tab1()


    
    def add_Tab1(self):
        #Custom
        self._custom = QWidget()
        
        #add widget
        self._RegularExpress = QLineEdit()


        #set layout
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Regular Expression"))
        layout.addWidget(self._RegularExpress)

        self._custom.setLayout(layout)


        self.addTab(self._custom,"Custom")