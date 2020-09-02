# -*- encoding: utf-8 -*-
import os

# 递归删除目录
def del_file(path):
	ls = os.listdir(path)
	for i in ls:
		c_path = os.path.join(path, i)
		if os.path.isdir(c_path):
			del_file(c_path)
		else:
			os.remove(c_path)

# 创建新目录，只支持创建一层，不支持创建多层
def mkdir(path):
	try:
		del_file(path)
		os.rmdir(path)
	except Exception as e:
		os.mkdir(path)
	else:
		os.mkdir(path)

