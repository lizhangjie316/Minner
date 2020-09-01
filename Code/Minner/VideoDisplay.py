import sys
import cv2
import threading
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
# import DisplayUI
from Camera import Camera
from multiprocessing import Process
from SegModel import *
class Display:
    def __init__(self):
        self.threads=list()
        self.closeToggles=list()
        self.currentStates=list()
        self.showLabels=list()
        # 默认视频源为文件
        self.capdict=dict()
        self.frameRatedict=dict()
        self.isCamera = False
        self.fps=120
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        self.seg = SegModel()
        self.maththread=threading.Thread(target=self.seg.Analysis)
        self.maththread.start()
    # def reset(self):
    #     #设置应该关闭的信号
    def FiniSignal(self):
        return self.seg.finiSignal
    def init(self,LabelList):
        self.stopEvent.set()
        time.sleep(0.5)
        self.stopEvent.clear()
        self.showLabels=LabelList
        self.closeToggles=[0]*len(self.showLabels)
        self.currentStates=["-1"]*len(self.showLabels)

    #获得可用的显示label索引
    def GetCurrentLabelIndex(self):
        index=0;
        for state in self.currentStates:
            if state=="-1":
                return index
            index+=1
        return -1;
    def GetLabelIndexByID(self,ID):
        index = 0;
        for state in self.currentStates:
            if state == ID:
                return index
            index += 1
        return -1;

    def Open(self,Camera,CID):
        index=self.GetCurrentLabelIndex()
        self.capdict[index] = cv2.VideoCapture(Camera.GetUrl())
        self.frameRatedict[index]=self.capdict[index].get(cv2.CAP_PROP_FPS)
        # 创建视频显示线程
        self.currentStates[index]=CID
        th = threading.Thread(target = self.Display,args=(index,))
        th.start()

    def Close(self,index):
        self.closeToggles[index]=1

    def CloseAll(self):
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()
        self.seg.stopEvent.set()

    def Display(self,index):
        showLabel=self.showLabels[index]
        count=0
        while self.capdict[index].isOpened():
            success, frame = self.capdict[index].read()
            if success is False:
                print("Ended")
                break

            count+=1
            if count%self.fps==0:
                cv2.imwrite('images/'+self.currentStates[index] +"_"+ str(count) + '.png', frame)


            # RGB转BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            showLabel.setPixmap(QPixmap.fromImage(img))

            if self.isCamera:
                cv2.waitKey(1)
            else:
                cv2.waitKey(int(1000 / self.frameRatedict[index]))

            # 判断关闭事件是否已触发
            if self.closeToggles[index]==1:
                self.closeToggles[index]==0
                self.currentStates[index]=="-1"
                self.capdict[index].release()
                break

            if True == self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                break
