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

#total_num = 0

def scanFile(rootPath):
	for list in os.listdir(rootPath):
		path = os.path.join(rootPath, list)
		abs_path = os.path.abspath(path)
		logging.info('path: %s' %(abs_path))
		#remove_space(path)
		checkPermission(path)
		#如果当前路径为文件，则继续递归
		if os.path.isdir(path):
			scanFile(path)
#logging.info('we totally scaned %d files' %total_num)


def remove_space(path):
	if ' ' in path:
		new_path = path.replace(' ', '_')
		os.rename(path, new_path)


get_path_permission = {}
def checkPermission(root):
	#	global total_num
	#	total_num += 1
	
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
	first_record = file_info[0].lstrip(root + ' ')
	removed_space = first_record.split(' ')
	get_path_permission[root] = {}
	if len(removed_space) == 1:
		temp = remove_space[0]
	else:
		temp = removed_space[1]
	file_info[0] = temp
	for user_index in range(len(file_info)-2):
		get_path_permission[root][file_info[user_index].split(':')[0]] = file_info[user_index].split(':')[1]
		logging.info('		user: %s, permission: %s' %(file_info[user_index].split(':')[0].strip(' '),\
														file_info[user_index].split(':')[1].strip(' ')))









