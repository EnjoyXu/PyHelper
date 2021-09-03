import sys
from os import path as pth

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
sys.path.append(pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__))))))

from Instruments.Subplots import runSubplots
from Instruments.MyWidgets.MyWidgets import MyTabWidget


class PlotSetwindow(Abs_SubSubwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()

        self.add_stack_style()
        self.add_grid_group_box_1()
        self.add_grid_group_box_2()

        self._ok = QPushButton("OK")
        self._ok.clicked.connect(self.ok_clicked)
        

        #set layout
        layout = QVBoxLayout()
        layout.addWidget(self._grid_group_box_1)
        layout.addWidget(self._grid_group_box_2)
        layout.addWidget(self._ok)

        self.setLayout(layout)

        self._cb_style.currentIndexChanged.connect(lambda : self.stack_display(self._cb_style.currentIndex(),self._stack_style ))
    
    
    def ini_gui(self):
        self.setFixedSize(500,600)
        self.setWindowTitle("Plot Setting")


    def add_grid_group_box_1(self):
        self._grid_group_box_1 = QGroupBox()
        
        self._obj_mode = QCheckBox("OBJ Mode")
        self._obj_mode.setChecked(False)
        self._obj_mode.stateChanged.connect(self.check_obj)

        self._obj_mode_name = QLineEdit()
        self._obj_mode_name.hide()

        self._cb_style = QComboBox()
        self._cb_style.addItems(["plot","scatter"])

        #set layout
        layout = QGridLayout()
        layout.addWidget(self._obj_mode,0,0)
        layout.addWidget(self._obj_mode_name,0,1)

        layout.addWidget(QLabel("Plot Style"),1,0)
        layout.addWidget(self._cb_style,1,1,1,1  )
        
        layout.addWidget(self._stack_style,2,0,2,2)
        
        self._grid_group_box_1.setLayout(layout)

    def check_obj(self):
        check = ".show()" if self._obj_mode.isChecked() else ".hide()"
        exec("self._obj_mode_name" + check)
    



    def add_stack_style(self):
        self._stack_style = QStackedWidget()
        
        self.add_stack1_plot()
        self.add_stack2_scatter()

        
    def add_stack1_plot(self):
        self._stack1_plot = QWidget()

        #Add widges
        self._plot_cb_linestyle = QComboBox()
        self._plot_cb_linestyle.addItems(['"solid"','"dashed"','"dashdot"','"dotted"','"None"'])
        self._plot_linewidth = QLineEdit()

        self._plot_label = QLineEdit()
        self._plot_marker = QLineEdit()


        #set layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Linestyle:"),0,0)
        layout.addWidget(self._plot_cb_linestyle,0,1)

        layout.addWidget(QLabel("LineWidth:"),0,2)
        layout.addWidget(self._plot_linewidth,0,3)

        layout.addWidget(QLabel("Legend:"),1,0)
        layout.addWidget(self._plot_label,1,1)

        layout.addWidget(QLabel("Marker:"),1,2)
        layout.addWidget(self._plot_marker,1,3)

      
        self._stack1_plot.setLayout(layout)
        self._stack_style.addWidget(self._stack1_plot)

    def add_stack2_scatter(self):
        self._stack2_scatter = QWidget()
        
        #Add widges
        self._scat_s = QLineEdit()
        self._scat_marker = QLineEdit()
        self._scat_alpha =  QLineEdit()

        self._scat_label = QLineEdit()
        self._scat_cmap = QLineEdit()

        self._scat_edgecolors = QLineEdit()
        self._scat_linewidth = QLineEdit()

        


        #set layout
        layout = QGridLayout()
        
        layout.addWidget(QLabel("s"),0,0)
        layout.addWidget(self._scat_s,0,1)

        layout.addWidget(QLabel("Marker:"),0,2)
        layout.addWidget(self._scat_marker,0,3)

        layout.addWidget(QLabel("Alpha:"),0,4)
        layout.addWidget(self._scat_alpha,0,5)

        layout.addWidget(QLabel("Legend:"),1,0)
        layout.addWidget(self._scat_label,1,1)

        layout.addWidget(QLabel("Cmap:"),1,2)
        layout.addWidget(self._scat_cmap,1,3)

        layout.addWidget(QLabel("Edgecolor:"),2,0)
        layout.addWidget(self._scat_edgecolors,2,1)

        layout.addWidget(QLabel("Linewidth:"),2,2)
        layout.addWidget(self._scat_linewidth,2,3)


        self._stack2_scatter.setLayout(layout)
        self._stack_style.addWidget(self._stack2_scatter)

    def add_grid_group_box_2(self):
        # universal settings
        self._grid_group_box_2 = QGroupBox("Universal Settings")

        self._universal_settings = MyTabWidget()

        layout = QVBoxLayout()
        layout.addWidget(self._universal_settings)
        
        self._grid_group_box_2.setLayout(layout)

         

    def stack_display(self,i,stack):
        stack.setCurrentIndex(i)

    def ok_clicked(self):
        self.string = ''

        is_label = False # Judge whether to set legend


        #Judge whether obj mode is on
        self.obj_name = self._obj_mode_name.text()+"." if self._obj_mode.isChecked() else "plt."
        self.control = "set_" if self._obj_mode.isChecked() else ""

        #Plot style
        if self._cb_style.currentText() == "plot":
            self.string += self.obj_name + "plot(x,y,\n\t"
            self.string += "ls = " + self._plot_cb_linestyle.currentText()+ ",\n\t"

            name_lst = ["linewidth","label","marker"]
            name_lst = [("_plot_" + x , x) for x in name_lst]

            for name in name_lst:
                self.style_write_in(name[0],name[1])
            
            if len(self._plot_label.text()) != 0:
                is_label = True
            
          
        elif self._cb_style.currentText() == "scatter":
            self.string += self.obj_name + "scatter(x,y,\n\t" 

            name_lst = ["s","marker","alpha","label","cmap","edgecolors","linewidth"]
            name_lst = [("_scat_" + x , x) for x in name_lst]

            for name in name_lst:
                self.style_write_in(name[0],name[1])
            
            if len(self._scat_label.text()) != 0:
                is_label = True

        # add color
        self.color_write_in("_universal_settings.plot_color")
        self.string += ")\n"

        # add legend
        if is_label:
            self.string += "plt.legend(loc = 'best')\n"


        # Figure
        self.set_write_in(r"_universal_settings.title","title")

        if self._universal_settings.grid.isChecked():
            self.string += self.obj_name + "grid("

            name_lst = ["linestyle","linewidth"]
            name_lst = [("_universal_settings.grid_"+x ,x )  for x in name_lst]

            self.style_write_in(name_lst[0][0],name_lst[0][1],"currentText")
            self.style_write_in(name_lst[1][0],name_lst[1][1],)

            self.color_write_in("_universal_settings.grid_plot_color")

            self.string += ")\n"

        # Axis
        if self._universal_settings.hide_x.isChecked():
            self.string += self.obj_name + self.control+\
                "xticks([])"
        else:
            self.set_write_in("_universal_settings.x_label","xlabel")
            self.set_write_in("_universal_settings.xtick","xticks")

        if self._universal_settings.hide_y.isChecked():
            self.string += self.obj_name + self.control+\
                "yticks([])"
        else:
            self.set_write_in("_universal_settings.y_label","ylabel")
            self.set_write_in("_universal_settings.ytick","yticks")

 
        # Others
        path = self._universal_settings.path.text()
        dpi = self._universal_settings.dpi.text()


        
        if len(path) != 0:
            if len(dpi) != 0 :
                dpi = ", dpi = "+dpi
            self.string += 'plt.savefig("%s",dpi=%s )' % (path,dpi)


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