import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
# from Camera import  Camera
import os
# self.tabWidget.tabBar().setTabButton(0,QtWidgets.QTabBar.RightSide,None)
# from ui.Ui_MainWindow import *
from ui.Ui_MainWindow import Ui_MainWindow
from utils.video.Camera import Camera
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'


# def CreateFiles():
#     if not os.path.exists('./db'):
#         os.makedirs('./db')
#     if not os.path.exists('./images'):
#         os.makedirs('./images')
#     if not os.path.exists('./png8_test'):
#         os.makedirs('./png8_test')
#     if not os.path.exists('./predict'):
#         os.makedirs('./predict')
#     if not os.path.exists('./results'):
#         os.makedirs('./results')

def CreateFiles():
    if not os.path.exists('data/processing/db'):
        os.makedirs('data/processing/db')
    if not os.path.exists('data/processing/images'):
        os.makedirs('data/processing/images')
    if not os.path.exists('data/processing/png8_test'):
        os.makedirs('data/processing/png8_test')
    if not os.path.exists('data/processing/predict'):
        os.makedirs('data/processing/predict')
    if not os.path.exists('data/processing/results'):
        os.makedirs('data/processing/results')


if __name__ == "__main__":

    CreateFiles()
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.lastWindowClosed.connect(ui.player.CloseAll)
    camera1 = Camera("出矿口1","data/mp4/ore1.mp4")
    camera2 = Camera("出矿口2","data/mp4/ore1.mp4")
    camera3 = Camera("出矿口3","data/mp4/ore1.mp4")
    camera4 = Camera("出矿口4","data/mp4/ore1.mp4")
    ui.AddCamera(camera1)
    ui.AddCamera(camera2)
    ui.AddCamera(camera3)
    ui.AddCamera(camera4)
    sys.exit(app.exec_())
