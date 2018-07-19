#coding: utf-8
'''
	for windows
'''


import os
import logging

logging.basicConfig(filename='log_icacls.log', level=logging.DEBUG)
'''
	logging.debug(...)
	logging.info(...)
	logging.warning(...)
'''

total_num = 0

def scanFile(rootPath):
	for list in os.listdir(rootPath):
		path = os.path.join(rootPath, list)
		abs_path = os.path.abspath(path)
		logging.info('path: %s' %(abs_path))
		checkPermission(path)
		#如果当前路径为文件，则继续递归
		if os.path.isdir(path):
			scanFile(path)
	logging.info('we totally scaned %d files' %total_num)


get_path_permission = {}
def checkPermission(root):
	total_num += 1
	
	cmd = 'icacls ' + root
	# 用于获得windows下文件的权限信息
	temp = os.popen(cmd)
	file_info = temp.readlines()
	'''
		file_info 格式: e.g.
		. NT AUTHORITY\\SYSTEM:(I)(OI)(CI)(F)\n,
		BUILDIN\\Administrators:(I)(OI)(CI)(F)\n,
		admin-PC\\admin:(I)(OI)(CI)(F)\n
		\n
		已顺利处理...
	'''
	# 每个用户都有一个权限, 此处，只为一个Administrators & 一个 admin
	first_record = file_info[0].split(' ')
	path = first_record[0]
	get_path_permission[path] = {}
	if len(first_record) == 2:
		tmp = first_record[1]
	else:
		tmp = first_record[2]
	file_info[0] = tmp
	for user_index in range(len(file_info)-2):
		get_path_permission[path][file_info[user_index].split(':')[0]] = file_info[user_index].split(':')[1]
		logging.info('		user: %s, permission: %s' %(file_info[user_index].split(':')[0].strip(' '),\
														file_info[user_index].split(':')[1].strip(' ')))









