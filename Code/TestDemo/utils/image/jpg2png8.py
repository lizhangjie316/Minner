import cv2
import os
import glob


def myRename(filePath):
	i = 0
	for pic in os.listdir(filePath):
		if not pic.index(".") >= 0:
			# 说明是目录
			raise

		src = filePath + "/" + pic
		dst = filePath + "/%d" % i + ".jpg"
		# print(src)
		# print(dst)
		os.rename(src, dst)
		i = i + 1
	print("目录为: %s" % os.listdir(filePath))


# 递归删除目录
def del_file(path):
	ls = os.listdir(path)
	for i in ls:
		c_path = os.path.join(path, i)
		if os.path.isdir(c_path):
			del_file(c_path)
		else:
			os.remove(c_path)


# 单张图片转jpg=>png
def jpg2png(filePath):
	save_path = filePath + "/../png_test/"
	# print(save_path)
	try:
		del_file(save_path)
		os.rmdir(save_path)
	except Exception as e:
		os.mkdir(save_path)
	else:
		os.mkdir(save_path)
	# 循环转化=>png
	i = 0
	try:
		for file in glob.glob(filePath + "/*.jpg"):
			# print(file)
			img = cv2.imread(file)
			# print(img)
			cv2.imwrite(save_path + '%d' % i + '.png', img)
			i = i + 1
	except:
		raise
	# print(save_path + "*.jpg")


# 单张图片转为8位
def togrey(img, outdir):
	src = cv2.imread(img)
	try:
		dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
		cv2.imwrite(os.path.join(outdir, os.path.basename(img)), dst)
	except Exception as e:
		print(e)


# 目录下的png图片转成8位
def png28(filePath):
	# 图片路径传进来，
	save_path = filePath + "/../png8_test/"
	print(save_path)
	# save_path = filePath
	try:
		del_file(save_path)
		os.rmdir(save_path)
	except Exception as e:
		os.mkdir(save_path)
	else:
		os.mkdir(save_path)
	try:
		for file in glob.glob(filePath + "/*.png"):
			togrey(file, save_path)
		del_file(filePath)
	except:
		raise

'''
传入图片的路径imgPath，将jpg图片转成8位的灰度图，先不输出到传入图片所在路径了，
直接返回一个图片的numpy数组
'''
def SingleImageTransform(imgPath):
	# imgPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\images/1.jpg";
	savePath = imgPath.split('.')[0] # "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\images/1"
	# 读取进来
	img = cv2.imread(imgPath)
	# 转换为8位
	try:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imwrite(os.path.join(outdir, os.path.basename(img)), dst)
	except Exception as e:
		print(e)
	# 写出为jpg图片
	# TODO:先不写出了
	# cv2.imwrite(savePath + '.png', img)

	# os.remove(imgPath)

	# cv2.imshow("img",img)
	# cv2.waitKey(0)
	# print(type(img))  # <class 'numpy.ndarray'>
	# print(img.shape)  # (320, 480)
	# print(img)
	return img

if __name__ == "__main__":
	# filePath = "data/abc"
	# jpg2png(filePath)
	#
	# png28(filePath+"./../png_test/")
	# myRename(filePath)
	# 1. 将图片从jpg转换成png格式
	imgPath = "C:/Users\Keen\Desktop\Project\Github\Minner\Code\TestDemo\data\processing\images/1.jpg"
	# save_path = imgPath.split('.')[0]
	# # os.renames()
	# # 读取进来
	# img = cv2.imread(imgPath)
	# # 转换为8位
	# dst = None
	# try:
	# 	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# 	# cv2.imwrite(os.path.join(outdir, os.path.basename(img)), dst)
	# except Exception as e:
	# 	print(e)
	# # cv2.imwrite(save_path + '%d' % i + '.png', img)
	# # 写出为jpg图片
	# cv2.imwrite(save_path + '.png', img)
	# os.remove(imgPath)
	# cv2.imshow("image",img)
	# cv2.waitKey(0)
	# print(type(img))  # <class 'numpy.ndarray'>
	SingleImageTransform(imgPath)


