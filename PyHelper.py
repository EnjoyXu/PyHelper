#！Python
#--------------------------Import-----------------------------------
import sys
import os
# sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Windows.Mainwindow import Mainwindow
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet


#--------MAIN -----------------------------------------------------------

if __name__ == "__main__":
    # print(os.path.abspath(r"..\Instruments\Icon"))
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.center()

    # apply_stylesheet(app,theme = 'light_cyan.xml', invert_secondary=True,extra=extra)

    apply_stylesheet(app,theme = 'dark_amber.xml', invert_secondary=True,)

    mainwindow.show()

    sys.exit(app.exec())