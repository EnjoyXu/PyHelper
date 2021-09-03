import sys
from os import path as pth



from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon, QTextBlock, QValidator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,QCheckBox,QStackedWidget,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)
import pyperclip
import re

from SubSubwindows.AbstractSubSubwindow import Abs_SubSubwindow

sys.path.append(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))

from Instruments.MyWidgets.MyWidgets import MatchTabWidge




class Matchwindow(Abs_SubSubwindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Match")

        self._matchwidget = MatchTabWidge()
        self._matchwidget._RegularExpress.textChanged.connect(self.text_changed)


        self.add_replace()
        self.add_grid_group_box()
        self.add_export()
        



        #set layaout
        layout = QGridLayout()
        layout.addWidget(self._matchwidget,0,0,1,2)
        
        layout.addWidget(self._replace_check,1,0,1,1)
        layout.addWidget(self._replace,1,1,1,1)

        layout.addWidget(self._grid_group_box,2,0,1,2)

        layout.addWidget(self.export_expression,3,0)
        layout.addWidget(self.export_code,3,1)


        self.setLayout(layout)

    
    def add_replace(self):
        self._replace_check = QCheckBox("Replace")

        self._replace = QLineEdit()
        self._replace.textChanged.connect(self.text_changed)
        self._replace.hide()

        self._replace_check.clicked.connect(self.check_replace)
    
    def add_grid_group_box(self):
        self._grid_group_box = QGroupBox("Text")

        self._text_in = QTextEdit()
        self._text_in.textChanged.connect(self.text_changed)
        self._text_out = QTextEdit()
        self._text_out.setReadOnly(True)


        #set layout 
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Input test string"))
        layout.addWidget(self._text_in)
        layout.addWidget(self._text_out)

        self._grid_group_box.setLayout(layout)

    def add_export(self):
        self.export_expression = QPushButton("RE")
        self.export_expression.clicked.connect(self.export_expression_clicked)
        
        self.export_code = QPushButton("Code")
        self.export_code.clicked.connect(self.export_code_clicked)


    def export_expression_clicked(self):
        pyperclip.copy(self._matchwidget._RegularExpress.text())
    
    def export_code_clicked(self):
        
        string = 'pattern = re.compile("%s")\n' % self._matchwidget._RegularExpress.text()
        if self._replace_check.isChecked():
            string += 'outcome = re.sub(pattern,string)'      
        else:
            string += 'outcome = re.findall(pattern,string)'

        pyperclip.copy(string)
        


    def check_replace(self):
        check = ".show()" if self._replace_check.isChecked() else ".hide()"
        exec("self._replace" + check)
        
    

    def text_changed(self):
        try:
            string = 'pattern = re.compile("%s")\n' % self._matchwidget._RegularExpress.text()
            if self._replace_check.isChecked():
                string += 'outcome = re.sub(pattern,"%s","%s")'\
                    %(self._replace.text(),self._text_in.toPlainText()  )  
                exec(string)
                exec("self._text_out.setText(outcome)")

            else:
                string += "outcome = re.findall(pattern,'%s')"%self._text_in.toPlainText()
                exec(string)
                exec(r'self._text_out.setText("\n".join(outcome))')
                
        except:
            self._text_out.setText("Wrong Regular Expression")
            
    # def text_changed(self):
    #     string = 'pattern = re.compile("%s")\n' % self._matchwidget._RegularExpress.text()
    #     if self._replace_check.isChecked():
    #         string += 'outcome = re.sub(pattern,"%s","%s")'\
    #             %(self._replace.text(),self._text_in.toPlainText()  )  
    #         exec(string)
    #         exec("self._text_out.setText(outcome)")

    #     else:
    #         string += "outcome = re.findall(pattern,'%s')"%self._text_in.toPlainText()
    #         exec(string)
    #         exec(r'self._text_out.setText("\n".join(outcome))')
            
    #         exec('''out1 = re.sub(pattern,'%s',"<font color='red' ><red>Here</font>")'''\
    #             %(self._text_in.toPlainText()))
    #         exec("self._text_in.setHtml(out1)")
            
        






        
    

    

