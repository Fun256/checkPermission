#coding: utf-8
'''
	for windows
'''


import os



def scanFile(rootPath):
	for list in os.listdir(rootPath):
		path = os.path.join(rootPath, list)
		checkPermission(path)

get_path_permission = {}
def checkPermission(path):
	cmd = 'icacls ' + path
	# 用于获得windows下文件的权限信息
	temp = os.popen(cmd)
	file_info = temp.readlines()
	get_path_permission[path] = {}
	'''
		file_info 格式: e.g.
		. NT AUTHORITY\\SYSTEM:(I)(OI)(CI)(F)\n,
		BUILDIN\\Administrators:(I)(OI)(CI)(F)\n,
		admin-PC\\admin:(I)(OI)(CI)(F)\n
	'''
	# 每个用户都有一个权限, 此处，只为一个Administrators & 一个 admin
	get_path_permission[path][file_info[0].split(':')[0]] = file_info[0].split(':')[1]
	get_path_permission[path][file_info[1].split(':')[0]] = file_info[1].split(':')[1]
	get_path_permission[path][file_info[2].split(':')[0]] = file_info[2].split(':')[1]








