#coding: utf-8

import sys
sys.path.append('../src')

import icaclsForWin as ifw


def scan(path):
	ifw.scanFile(path)
#ifw.scanFile('.')
#path = ifw.get_path_permission
#print(path)

'''
def getAllPathAndPermission(path):
	
	# 获得每一层的路径
	each_layer_path = list(path.keys())
	for key_index in range(len(each_layer_path)):
		if
'''


