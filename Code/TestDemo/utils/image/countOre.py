import glob
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt
import sys

import time


class Info:
	# ares ** 0.5 * cm_per_pixels > 20

	# 类的成员
	# cm_per_pixels = 参考长度/在图片上的px
	cm_per_pixels = 25/100
	areas_avg_real = 0
	#             矿石块计数、总体的像素面积面积、 总体的真实面积     >=20的真实直径列表
	count_dict = {"count":0,"area_sum_real":0,"20":[],"10":[],"5":[],"2":[]}
	percent_dict = {"p20":0,"p10":0,"p5":0,"p2":0}

	@classmethod # 类方法
	def calcPercent(cls):
		cls.percent_dict["p20"] = round(len(cls.count_dict["20"])/cls.count_dict["count"]*100,2)
		cls.percent_dict["p10"] = round(len(cls.count_dict["10"])/cls.count_dict["count"]*100,2)
		cls.percent_dict["p5"] = round(len(cls.count_dict["5"])/cls.count_dict["count"]*100,2)
		# p2 = round(len(cls.count_dict["2"])/cls.count_dict["count"]*100,2)
		cls.percent_dict["p2"] = 100-cls.percent_dict["p20"]-cls.percent_dict["p10"]-cls.percent_dict["p5"]

		print(cls.percent_dict["p20"],cls.percent_dict["p10"],cls.percent_dict["p5"],cls.percent_dict["p2"])

	@classmethod  # 类方法
	def reset(cls):
		cls.count_dict = {"count":0,"area_sum_real":0,"20":[],"10":[],"5":[],"2":[]}
		cls.percent_dict = {"p20": 0, "p10": 0, "p5": 0, "p2": 0}


def countOre(imgPath):
	"""原始图像导入"""
	img = cv2.imread(imgPath)
	CameraID=os.path.split(imgPath)[1].split("_",1)[0]

	CameraLocation=UI.Ui_MainWindow.CameraDict[CameraID].GetLocation()

	imgsavepath="results/"+os.path.split(imgPath)[1]
	# img = cv2.imread("E:/Project/Minner/data/0_predict.png")
	# print(img)
	"""转化为灰度图像"""
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imshow("gray", gray)

	"""转化为二值图像"""
	dst1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 251, 1)
	# cv2.imshow("black&white", dst1)

	"""膨胀用于排除小型黑洞"""
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # (此矩阵有关于黑点、噪点的去除)
	dst = cv2.bitwise_not(dst1)  # 取反
	# dilateImg = cv2.dilate(dst, kernel)
	dst = cv2.erode(dst, kernel)
	dst = cv2.bitwise_not(dst)
	# cv2.imshow("erodImg&wdilateImg", dst)

	"""计算数目"""
	# dilateImg = 255 - dst #黑白转换
	contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测函数
	cv2.drawContours(dst, contours, -1, (100, 0, 0), 2)  # 绘制轮廓
	# cv2.imshow("calcuate", dst)

	count = 0  # 单张图片的矿石总数
	areas_sum_real = 0  # 记录单张图片上的矿石总真实面积

	# 遍历找到的所有矿石
	for cont in contours:
		ares = cv2.contourArea(cont)  # 计算包围形状的像素面积
		# 真实直径
		realInch = round((ares ** 0.5) * Info.cm_per_pixels,2)
		# 单个闭合区域的真实面积
		real_ares = round(realInch ** 2,2)
		# 计数
		if realInch >= 20:
			Info.count_dict["20"].append(realInch)
		elif realInch >= 10:
			Info.count_dict["10"].append(realInch)
		elif realInch >= 5:
			Info.count_dict["5"].append(realInch)
		elif realInch >= 2:
			Info.count_dict["2"].append(realInch)
		else:
			continue

		count += 1
		areas_sum_real += real_ares
		print("{}-blob:{}".format(count, real_ares))  # 打印出每个矿石的真实面积

		# rect = cv2.boundingRect(cont)  # 提取矩形坐标
		# print("x:{} y:{} w:{} h:{}".format(rect[0], rect[1], rect[2], rect[3]))  # 打印坐标
		# cv2.rectangle返回值是x,y,w,h
		# cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 0, 0xff), 1)  # 绘制矩形
		# y = 10 if rect[1] < 10 else rect[1]  # 防止编号到图片之外
		# cv2.putText(img, str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)  # 在矿石左上角写上编号


	Info.count_dict["count"] += count
	Info.count_dict["area_sum_real"] += areas_sum_real
	# avg:单张图片的真实平均面积
	avg = round(areas_sum_real/count,2)
	Info.areas_avg_real = round(Info.count_dict["area_sum_real"] / Info.count_dict["count"], 2)

	print("单张图片的矿石平均面积:{}".format(avg))  # 打印出每个矿石的面积
	print("单张图片的矿石个数:{}".format(count))
	Info.calcPercent()

	#数据库处理
	db = QSqlDatabase.addDatabase('QSQLITE')
	# 设置数据库名称
	db.setDatabaseName('data/processing/db/Test1database.db')
	# 判断是否打开
	if not db.open():
		return False

	# 声明数据库查询对象
	query = QSqlQuery()
	query.exec(
		"create table SegResult(recordNumber int primary key, CameraID vchar, CameraSite vchar,FrameTime datatime ,XL float, L floatl,M float, S float)")
	query.exec("create table SegResultImage(recordNumber int primary key, ImagePath vchar)")
	query.exec("SELECT count(*) FROM SegResult")
	query.next()
	recordCount=query.value(0)+1
	query.exec("insert into SegResult values(%d,%s,%s,%s,%.2f,%.2f,%.2f,%.2f)" %(recordCount,"\'"+CameraID+"\'","\'"+CameraLocation+"\'","\'"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\'",
																		 Info.percent_dict["p20"],Info.percent_dict["p10"],Info.percent_dict["p5"],Info.percent_dict["p2"]))
	print("insert into SegResult values(%d,%s,%s,%s,%.2f,%.2f,%.2f,%.2f)" %(recordCount,"\'"+CameraID+"\'","\'"+CameraLocation+"\'","\'"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\'",
																		 Info.percent_dict["p20"],Info.percent_dict["p10"],Info.percent_dict["p5"],Info.percent_dict["p2"]))
	query.exec("insert into SegResultImage values(%d,%s)" %(recordCount,"\'"+imgsavepath+"\'"))
	Info.reset()
	db.close()
	return True
	# cv2.imshow("original", img)


	# cv2.waitKey()
	# cv2.destroyAllWindows()  # important part!

'''
统计信息，并规整到Info类中
'''
def countInfo(filePath):
	# save_path = filePath + "./../count/"
	# mkdir(save_path)
	print(filePath)
	try:
		for file in os.listdir(filePath):
			countOre(filePath+file)
	except:
		raise
	print("hello")


if __name__ == "__main__":
	print("================================")
	'''
	1. 之前的测试
	'''
	# # imgPath = "E:/Project/Minner/data/1_predict.png"
	# # print(sys.argv[0])
	# # imgPath = "./data/1_predict.png"
	# info = Info()
	# # countOre(imgPath)
	# # print(len(Info.count_dict['20']))
	#
	# countInfo("C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\predict")
	# print("----------------------------------------------------------------")
	# print(len(Info.count_dict["20"]),len(Info.count_dict["10"]),len(Info.count_dict["5"]),len(Info.count_dict["2"]))   # 69 101 215 492
	# print(Info.count_dict["count"]) # 877
	# Info.calcPercent() # 7.87 11.52 24.52 56.09    和为100
	# # print("hello")
	'''
	2. 构建单张图片的分割结果，并保存到数据库中去
	'''
	# info = Info()
	# imgPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\predict/1599029866.png"
	# img = cv2.imread(imgPath)
	#
	# """转化为灰度图像"""
	# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imshow("gray", gray)

	# """转化为二值图像"""
	# dst1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 251, 1)
	# # cv2.imshow("black&white", dst1)
	# # cv2.waitKey(0)
	# """膨胀用于排除小型黑洞"""
	# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # (此矩阵有关于黑点、噪点的去除)
	# dst = cv2.bitwise_not(dst1)  # 取反
	# # dilateImg = cv2.dilate(dst, kernel)
	# dst = cv2.erode(dst, kernel)
	# dst = cv2.bitwise_not(dst)
	# # cv2.imshow("erodImg&wdilateImg", dst)
	#
	#
	# """计算数目"""
	# # dilateImg = 255 - dst #黑白转换
	# contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测函数
	# cv2.drawContours(dst, contours, -1, (100, 0, 0), 2)  # 绘制轮廓
	# cv2.imshow("calcuate", dst)
	# cv2.waitKey(0)
	#
	# count = 0  # 单张图片的矿石总数
	# areas_sum_real = 0  # 记录单张图片上的矿石总真实面积
	#
	# # 遍历找到的所有矿石
	# for cont in contours:
	# 	ares = cv2.contourArea(cont)  # 计算包围形状的像素面积
	# 	# 真实直径
	# 	realInch = round((ares ** 0.5) * Info.cm_per_pixels,2)
	# 	# 单个闭合区域的真实面积
	# 	real_ares = round(realInch ** 2,2)
	# 	# 计数
	# 	if realInch >= 20:
	# 		Info.count_dict["20"].append(realInch)
	# 	elif realInch >= 10:
	# 		Info.count_dict["10"].append(realInch)
	# 	elif realInch >= 5:
	# 		Info.count_dict["5"].append(realInch)
	# 	elif realInch >= 2:
	# 		Info.count_dict["2"].append(realInch)
	# 	else:
	# 		continue
	#
	# 	count += 1
	# 	areas_sum_real += real_ares
	# 	print("{}-blob:{}".format(count, real_ares))  # 打印出每个矿石的真实面积
	#
	# Info.count_dict["count"] += count
	# Info.count_dict["area_sum_real"] += areas_sum_real
	# # avg:单张图片的真实平均面积
	# avg = round(areas_sum_real/count,2)
	# Info.areas_avg_real = round(Info.count_dict["area_sum_real"] / Info.count_dict["count"], 2)
	#
	# print("单张图片的矿石平均面积:{}".format(avg))  # 打印出每个矿石的面积
	# print("单张图片的矿石个数:{}".format(count))
	# Info.calcPercent()