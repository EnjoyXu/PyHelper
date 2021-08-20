import sys
from os import path as pth
from typing import Text
from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,QCheckBox,QStackedWidget,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)
import pyperclip

from SubSubwindows.AbstractSubSubwindow import Abs_SubSubwindow
sys.path.append(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))

from Instruments.Subplots import runSubplots
from Instruments.MyWidgets.MyWidgets import MyTabWidget


class PlotSetwindow(Abs_SubSubwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()

        self.add_stack_style()
        self.add_grid_group_box_1()
        self.add_grid_group_box_2()

        self.ok = QPushButton("OK")
        self.ok.clicked.connect(self.ok_clicked)
        

        #set layout
        layout = QVBoxLayout()
        layout.addWidget(self.grid_group_box_1)
        layout.addWidget(self.grid_group_box_2)
        layout.addWidget(self.ok)

        self.setLayout(layout)

        self.cb_style.currentIndexChanged.connect(lambda : self.stack_display(self.cb_style.currentIndex(),self.stack_style ))
    
    def ini_gui(self):
        self.setFixedSize(500,600)
        self.setWindowTitle("Plot Setting")


    def add_grid_group_box_1(self):
        self.grid_group_box_1 = QGroupBox()
        
        self.obj_mode = QCheckBox("OBJ Mode")
        self.obj_mode.setChecked(False)
        self.obj_mode.stateChanged.connect(self.check_obj)

        self.obj_mode_name = QLineEdit()
        self.obj_mode_name.hide()

        self.cb_style = QComboBox()
        self.cb_style.addItems(["plot","scatter"])

        #set layout
        layout = QGridLayout()
        layout.addWidget(self.obj_mode,0,0)
        layout.addWidget(self.obj_mode_name,0,1)

        layout.addWidget(QLabel("Plot Style"),1,0)
        layout.addWidget(self.cb_style,1,1,1,1  )
        
        layout.addWidget(self.stack_style,2,0,2,2)
        
        self.grid_group_box_1.setLayout(layout)

    def check_obj(self):
        check = ".show()" if self.obj_mode.isChecked() else ".hide()"
        exec("self.obj_mode_name" + check)
    



    def add_stack_style(self):
        self.stack_style = QStackedWidget()
        
        self.add_stack1_plot()
        self.add_stack2_scatter()

        
    def add_stack1_plot(self):
        self.stack1_plot = QWidget()

        #Add widges
        self.plot_cb_linestyle = QComboBox()
        self.plot_cb_linestyle.addItems(['"solid"','"dashed"','"dashdot"','"dotted"','"None"'])
        self.plot_linewidth = QLineEdit()

        self.plot_label = QLineEdit()
        self.plot_marker = QLineEdit()


        #set layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Linestyle:"),0,0)
        layout.addWidget(self.plot_cb_linestyle,0,1)

        layout.addWidget(QLabel("LineWidth:"),0,2)
        layout.addWidget(self.plot_linewidth,0,3)

        layout.addWidget(QLabel("Legend:"),1,0)
        layout.addWidget(self.plot_label,1,1)

        layout.addWidget(QLabel("Marker:"),1,2)
        layout.addWidget(self.plot_marker,1,3)

      
        self.stack1_plot.setLayout(layout)
        self.stack_style.addWidget(self.stack1_plot)

    def add_stack2_scatter(self):
        self.stack2_scatter = QWidget()
        
        #Add widges
        self.scat_s = QLineEdit()
        self.scat_marker = QLineEdit()
        self.scat_alpha =  QLineEdit()

        self.scat_label = QLineEdit()
        self.scat_cmap = QLineEdit()

        self.scat_edgecolors = QLineEdit()
        self.scat_linewidth = QLineEdit()

        


        #set layout
        layout = QGridLayout()
        
        layout.addWidget(QLabel("s"),0,0)
        layout.addWidget(self.scat_s,0,1)

        layout.addWidget(QLabel("Marker:"),0,2)
        layout.addWidget(self.scat_marker,0,3)

        layout.addWidget(QLabel("Alpha:"),0,4)
        layout.addWidget(self.scat_alpha,0,5)

        layout.addWidget(QLabel("Legend:"),1,0)
        layout.addWidget(self.scat_label,1,1)

        layout.addWidget(QLabel("Cmap:"),1,2)
        layout.addWidget(self.scat_cmap,1,3)

        layout.addWidget(QLabel("Edgecolor:"),2,0)
        layout.addWidget(self.scat_edgecolors,2,1)

        layout.addWidget(QLabel("Linewidth:"),2,2)
        layout.addWidget(self.scat_linewidth,2,3)


        self.stack2_scatter.setLayout(layout)
        self.stack_style.addWidget(self.stack2_scatter)

    def add_grid_group_box_2(self):
        # universal settings
        self.grid_group_box_2 = QGroupBox("Universal Settings")

        self.universal_settings = MyTabWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.universal_settings)
        
        self.grid_group_box_2.setLayout(layout)

         

    def stack_display(self,i,stack):
        stack.setCurrentIndex(i)

    def ok_clicked(self):
        self.string = ''

        is_label = False # Judge whether to set legend


        #Judge whether obj mode is on
        self.obj_name = self.obj_mode_name.text()+"." if self.obj_mode.isChecked() else "plt."
        self.control = "set_" if self.obj_mode.isChecked() else ""

        #Plot style
        if self.cb_style.currentText() == "plot":
            self.string += self.obj_name + "plot(x,y,\n\t"
            self.string += "ls = " + self.plot_cb_linestyle.currentText()+ ",\n\t"

            name_lst = ["linewidth","label","marker"]
            name_lst = [("plot_" + x , x) for x in name_lst]

            for name in name_lst:
                self.style_write_in(name[0],name[1])
            
            if len(self.plot_label.text()) != 0:
                is_label = True
            
          
        elif self.cb_style.currentText() == "scatter":
            self.string += self.obj_name + "scatter(x,y,\n\t" 

            name_lst = ["s","marker","alpha","label","cmap","edgecolors","linewidth"]
            name_lst = [("scat_" + x , x) for x in name_lst]

            for name in name_lst:
                self.style_write_in(name[0],name[1])
            
            if len(self.scat_label.text()) != 0:
                is_label = True

        # add color
        self.color_write_in("universal_settings.plot_color")
        self.string += ")\n"

        # add legend
        if is_label:
            self.string += "plt.legend(loc = 'best')\n"


        # Figure
        self.set_write_in(r"universal_settings.title","title")

        if self.universal_settings.grid.isChecked():
            self.string += self.obj_name + "grid("

            name_lst = ["linestyle","linewidth"]
            name_lst = [("universal_settings.grid_"+x ,x )  for x in name_lst]

            self.style_write_in(name_lst[0][0],name_lst[0][1],"currentText")
            self.style_write_in(name_lst[1][0],name_lst[1][1],)

            self.color_write_in("universal_settings.grid_plot_color")

            self.string += ")\n"

        # Axis
        if self.universal_settings.hide_x.isChecked():
            self.string += self.obj_name + self.control+\
                "xticks([])"
        else:
            self.set_write_in("universal_settings.x_label","xlabel")
            self.set_write_in("universal_settings.xtick","xticks")

        if self.universal_settings.hide_y.isChecked():
            self.string += self.obj_name + self.control+\
                "yticks([])"
        else:
            self.set_write_in("universal_settings.y_label","ylabel")
            self.set_write_in("universal_settings.ytick","yticks")

 
        # Others
        path = self.universal_settings.path.text()
        dpi = self.universal_settings.dpi.text()


        
        if len(path) != 0:
            if len(dpi) != 0 :
                dpi = ", dpi = "+dpi
            self.string += 'plt.savefig("%s%s ")' % (path,dpi)


        pyperclip.copy(self.string)
        
    
    #-----------------------Write in functions-------------------
    def style_write_in(self,wgname,outname='',funcname="text"):
        if outname == '':
            outname = wgname
        exec_str = '''
item = self.%s.%s()
if len(item) != 0:
    self.string += "%s = "+item+'''%(wgname,funcname,outname) 
        exec_str +=  r'",\n\t"'
        

        exec( exec_str)
    
    def set_write_in(self,wgname,outname='',funcname="text"):
        if outname == '':
            outname = wgname
        exec_str = '''
item = self.%s.%s()
if len(item) != 0:
    self.string += self.obj_name +self.control+"%s("+item+")"'''%(wgname,funcname,outname) 
        exec_str +=  r'+"\n"'
        
        exec( exec_str)
    
    def color_write_in(self,wgname,outname='color',funcname="getRgb"):
        try:
            exec_str = '''
if self.%s.isValid():
    item = self.%s.%s()
    item = tuple([x/255 for x in item])
    self.string += "%s = "+str(item)+'''%(wgname,wgname,funcname,outname)
            exec_str +=  r'",\n\t"'
            # print(exec_str)
            exec( exec_str)
        except:
            pass