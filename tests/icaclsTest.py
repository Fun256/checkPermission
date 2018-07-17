#coding: utf-8

import sys
sys.path.append('../src')

import icaclsForWin as ifw

ifw.scanFile('.')
print(ifw.get_path_permission)
