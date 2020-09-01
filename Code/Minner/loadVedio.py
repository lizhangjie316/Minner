#! /usr/bin/env python
# coding=utf-8
import cv2
import numpy as np

from countOre import Info
from mkdir import *
# import cv2.cv as cv


# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
	address = addr + str(num) + '_.jpg' # 加_防止冲突
	cv2.imwrite(address, image)


# 截取一个视频所有帧
def clipAllFps(videoPath, outputPath):
	# videoPath = "./data/ore1.mp4"
	videoCapture = cv2.VideoCapture(videoPath)  # 从文件读取视频
	# 判断视频是否打开
	if (videoCapture.isOpened()):
		print("Open")
	else:
		print("Fail to open!")

	mkdir(outputPath)
	success, frame = videoCapture.read()  # 读取第一帧

	i = 0
	while success:
		i = i + 1
		save_image(frame, outputPath, i)
		if success:
			print('save image:', i)
		success, frame = videoCapture.read()
	videoCapture.release()


# 每隔n帧提取一次
# timeF : 时间间隔
def clipSomeFps(videoPath, n, outputPath):
	# 读取视频文件
	videoCapture = cv2.VideoCapture(videoPath)
	# 通过摄像头的方式
	# videoCapture=cv2.VideoCapture(1)

	mkdir(outputPath)
	# 读帧
	success, frame = videoCapture.read()
	i = 0
	j = 0
	while success:
		i = i + 1
		if (i % n == 0):
			j = j + 1
			save_image(frame, outputPath, j)
			print('save image:', i)
		success, frame = videoCapture.read()
	videoCapture.release()


if __name__ == "__main__":
	videoPath = "./data/ore1.mp4"
	outputPath = './data/output/'
	# clipAllFps(videoPath,outputPath)
	info = Info()
	print("hello")
	# 每隔29帧读取一次
	clipSomeFps(videoPath,200,outputPath)

