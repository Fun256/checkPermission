#coding: utf-8

import sys
sys.path.append('../src')

import scanFile as fileTest

fileTest.getFile('.')
print(fileTest.fileList)

