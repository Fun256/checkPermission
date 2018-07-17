#coding: utf-8
'''
	for windows
'''


import os



def scanFile(rootPath):
	for list in os.listdir(rootPath):
		path = os.path.join(rootPath, list)
		checkPermission(path)
		#如果当前路径为文件，则继续递归
		if os.path.isdir(path):
			scanFile(path)


get_path_permission = {}
def checkPermission(root):
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
	path = file_info[0].split(' ')[0]
	get_path_permission[path] = {}
	tmp = file_info[0].split(' ')[2]
	file_info[0] = tmp
	for user_index in range(len(file_info)-2):
		get_path_permission[path][file_info[user_index].split(':')[0]] = file_info[user_index].split(':')[1]









