#coding: utf-8

import sys
sys.path.append('../src')

import checkPermission as CP

CP.scanFile('.')
print(CP.fileList)
print(CP.pathList)

