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

from model.unet import unet
from utils.image.countOre import countInfo
from utils.image.data import *
from utils.image.jpg2png8 import png28, SingleImageTransform


class SegModel(QtCore.QObject):
    finiSignal=QtCore.pyqtSignal()
    def __init__(self):
        super(SegModel,self).__init__()
        # self.ImagePath="images"
        # self.png28_path = self.ImagePath + "/../png8_test/"
        # self.num_image=0
        # self.predict_path = self.png28_path + "/../predict/"

        '''
        暂且先注释掉
        '''
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
        self.model.load_weights("C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\weight/unet_ore_epoch4.hdf5")

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
                # time.sleep(1)
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

    '''
        分割单张图片，并将结果进行保存
    '''
    def segSingleImage(self,imgPath,weightPath,savePath):
        self.model = unet()
        self.model.load_weights(weightPath)
        img = SingleImageTransform(imgPath)
        # 将数据组装进生成器
        testGene = dataGenerator(img)
        # 进行分割
        # https://keras.io/zh/models/model/#predict_generator
        results = self.model.predict_generator(testGene,1,verbose=1)
        # print(results.shape)  # (1, 320, 480, 1)
        # print(type(results))  # <class 'numpy.ndarray'>
        # print(results)
        # cv2.imshow("haha",results[0])
        savePredict(savePath,results)
        # cv2.imwrite("1.png",results)

if __name__ == "__main__":
    '''
    1. 组装
    '''
    # segModel = SegModel()
    # segModel.model = unet()
    # weightPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\weight/unet_ore_epoch4.hdf5"
    # segModel.model.load_weights(weightPath)
    # imgPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\images/1.jpg"
    # img = SingleImageTransform(imgPath)
    # savePath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\predict"
    # testGene = dataGenerator(img)
    # # 进行分割
    # # https://keras.io/zh/models/model/#predict_generator
    # results = segModel.model.predict_generator(testGene,1,verbose=1)
    # # print(results.shape)  # (1, 320, 480, 1)
    # # print(type(results))  # <class 'numpy.ndarray'>
    # # print(results)
    # # cv2.imshow("haha",results[0])
    # savePredict(savePath,results)
    # # cv2.imwrite("1.png",results)
    '''
    2. 测试组装好的数据
    '''
    segModel = SegModel()
    weightPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\weight/unet_ore_epoch4.hdf5"
    imgPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\images/1.jpg"
    savePath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\predict"
    segModel.segSingleImage(imgPath,weightPath,savePath)

