#coding: utf-8

import os
import pwd
import stat

def is_readable(path, user):
	user_info = pwd.getpwnam(user)
	uid = user_info.pw_uid
	gid = user_info.pw_gid
	s = os.stat(path)
	mode = s[stat.ST_MODE]
	return (
		((s[stat.ST_UID] == uid) and (mode & stat.S_IRUSR > 0)) or
		((s[stat.ST_GID] == gid) and (mode & stat.S_IRGRP > 0)) or
		(mode & stat.S_IROTH > 0)
	)

def is_writable(path, user):
	user_info = pwd.getpwnam(user)
	uid = user_info.pw_uid
	gid = user_info.pw_gid
	s = os.stat(path)
	mode = s[stat.ST_MODE]
	return (
		((s[stat.ST_UID] == uid) and (mode & stat.S_IWUSR > 0)) or
		((s[stat.ST_GID] == gid) and (mode & stat.S_IWGRP > 0)) or
		(mode & stat.S_IWOTH > 0)
	)

def is_executable(path, user):
	user_info = pwd.getpwnam(user)
	uid = user_info.pw_uid
	gid = user_info.pw_gid
	s = os.stat(path)
	mode = s[stat.ST_MODE]
	return (
		((s[stat.ST_UID] == uid) and (mode & stat.S_IXUSR > 0)) or
		((s[stat.ST_GID] == gid) and (mode & stat.S_IXGRP > 0)) or
		(mode & stat.S_IXOTH > 0)
	)

fileList = []
pathList = []
users = ['apple']
user = 'apple'

def scanFile(rootPath):
	for lists in os.listdir(rootPath): # 遍历当前路径下的所有文件
		path = os.path.join(rootPath, lists)
		checkPermission(path, user)
		if (check_user_permission[user]['R'] | check_user_permission[user]['W'] | check_user_permission[user]['X']) == False:
			continue;
		else:
			pathList.append(path)
			# 当前路径为文件，则继续递归
			if os.path.isdir(path):
				scanFile(path)



check_user_permission = {}
def checkPermission(path, user):
	Read = is_readable(path, user)
	Write = is_writable(path, user)
	Excute = is_executable(path, user)
	check_user_permission[user] = {'R': Read, 'W': Write, 'X': Excute}










