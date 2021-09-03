import sys
from os import path as pth
from os import startfile



from PySide6.QtGui import QScreen,QMouseEvent,QCursor,QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,QCheckBox,QStackedWidget,
                               QTextEdit, QVBoxLayout, QWidget,QMainWindow,
                               QTableWidget,QTableWidgetItem,QFrame)
import pyperclip
import subprocess
import signal

from SubSubwindows.AbstractSubSubwindow import Abs_SubSubwindow
sys.path.append(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))

from Instruments.Hotkey import *
# from Instruments.MyWidgets.MyWidgets import MyTabWidget

class Hotkeywindow(Abs_SubSubwindow):
    def __init__(self) -> None:
        super().__init__()
        self.ini_gui()
        self.checkbat()

        #add buttons
        self.control_text_start = "Start ▶"
        self.control_text_stop = "Stop ■"
        self.control = False #if hotkey.py is running
        self._control = QPushButton(self.control_text_start)
        self._control.clicked.connect(self.control_clicked)

        self._config = QPushButton("Config")
        self._config.clicked.connect(self.config_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self._control)
        layout.addWidget(self._config)

        self.setLayout(layout)
        
    def __del__(self):
        if self.control:
            self.kill_hotkey()



    def ini_gui(self):
        self.setWindowTitle("Hotkey")
        self.setFixedSize(220,120)


    def control_clicked(self):
        if self.control:
            self.kill_hotkey()
            self._control.setText(self.control_text_start)
            self.control = False
            

        else:
            self.hotkey = subprocess.Popen(pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))\
            +r"\Instruments\Hotkey.bat",shell=False)
            self._control.setText(self.control_text_stop)
            self.control = True
            





    def config_clicked(self):
        path = pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))\
            +r"\Instruments\Hotkey.py"
        startfile(path)
        print(path)



    def checkbat(self):
        path_pyhelper = pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))\
            +r"\PyHelper.bat"
        path_hotkey = pth.dirname(pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__)))))\
            +r"\Instruments\Hotkey.bat"

        print(pth.abspath("...."))
        with open(path_pyhelper,'r') as file:
            content = file.readlines()
        
        content[0] = content[0] + "cd ./Instruments \n"
        # content[0] = content[0] + "chdir \n"

        for i in range(len(content)):
            if "PyHelper" in content[i]:
                content[i] = content[i].replace("PyHelper","Hotkey")

        with open(path_hotkey,'w') as file:
            file.writelines(content)
    
    def kill_hotkey(self):
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(self.hotkey.pid)])