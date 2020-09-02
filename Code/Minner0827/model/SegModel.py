# -*- encoding: utf-8 -*-
import os
import sys
# import cv2
# from countOre import countOre, countInfo
# from jpg2png8 import *
# from keras import backend as K
# from PyQt5 import QtWidgets
import time
# from model import *
# from data import *
# from loadVedio import *
import threading
from PyQt5 import  QtCore

from model.model import unet
from utils.image.countOre import countInfo
from utils.image.data import testGenerator, saveResult
from utils.image.jpg2png8 import png28


class SegModel(QtCore.QObject):
    finiSignal=QtCore.pyqtSignal()
    def __init__(self):
        super(SegModel,self).__init__()
        # self.ImagePath="images"
        # self.png28_path = self.ImagePath + "/../png8_test/"
        # self.num_image=0
        # self.predict_path = self.png28_path + "/../predict/"
        self.ImagePath="data/processing/images"
        self.png28_path = self.ImagePath + "/../png8_test/"
        self.num_image=0
        self.predict_path = self.png28_path + "/../predict/"
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        self.testGene=None
        self.loaded=False

    # def reset(self):
    #     #设置应该关闭的信号
    def Load(self):
        self.model = unet()
        self.model.load_weights("data/weight/unet_ore_epoch4.hdf5")

    def Close(self):
        self.stopEvent.set()
    def Start(self):
        process = threading.Thread(target = self.Analysis())
        process.start()

    def Analysis(self):
        while True:
            if not self.loaded:
                self.Load()
                self.loaded=True
            if self.stopEvent.is_set():
                self.stopEvent.clear()
                break
            if not os.listdir(self.ImagePath):
                time.sleep(1)
                continue
            # 读取图片并转换格式
            num_image = len(os.listdir(self.ImagePath))
            # TODO 此处将png文件转为8位
            png28(self.ImagePath)
            testGene = testGenerator(self.png28_path, num_image)
            # 执行分割
            results = self.model.predict_generator(testGene, num_image,verbose=1)
            saveResult(self.png28_path, results)  # 存在test平级目录  "./../predict/"
            # 统计
            countInfo(self.predict_path)
            self.finiSignal.emit()


