#coding:utf-8

import os


fileList = []

def getFile(rootPath):
	'''
		遍历根目录下的文件, 存于list中
	'''

	for lists in os.listdir(rootPath):
		path = os.path.join(rootPath, lists)
		# 判断是否是文件
		if os.path.isdir(path):
			getFile(path)
		else:
			fileList.append(path)


