import sys
from Ui_MainWindow import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from Camera import  Camera
import os
# self.tabWidget.tabBar().setTabButton(0,QtWidgets.QTabBar.RightSide,None)
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

def CreateFiles():
    if not os.path.exists('./db'):
        os.makedirs('./db')
    if not os.path.exists('./images'):
        os.makedirs('./images')
    if not os.path.exists('./png8_test'):
        os.makedirs('./png8_test')
    if not os.path.exists('./predict'):
        os.makedirs('./predict')
    if not os.path.exists('./results'):
        os.makedirs('./results')



if __name__ == "__main__":

    CreateFiles()
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.lastWindowClosed.connect(ui.player.CloseAll)
    camera1 = Camera("出矿口1","./ore1.mp4")
    camera2 = Camera("出矿口2","./ore1.mp4")
    camera3 = Camera("出矿口3","./ore1.mp4")
    camera4 = Camera("出矿口4","./ore1.mp4")
    ui.AddCamera(camera1)
    ui.AddCamera(camera2)
    ui.AddCamera(camera3)
    ui.AddCamera(camera4)
    sys.exit(app.exec_())