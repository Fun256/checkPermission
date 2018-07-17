#coding: utf-8
'''
	for windows
'''

from win32security import *


def decode_flags(flags):
	_flags = {
	SE_DACL_PROTECTED:"SE_DACL_PROTECTED",
	SE_DACL_AUTO_INHERITED:"SE_DACL_AUTO_INHERITED",
	OBJECT_INHERIT_ACE:"OBJECT_INHERIT_ACE",
	CONTAINER_INHERIT_ACE:"CONTAINER_INHERIT_ACE",
	INHERIT_ONLY_ACE:"INHERIT_ONLY_ACE",
	NO_INHERITANCE:"NO_INHERITANCE",
	NO_PROPAGATE_INHERIT_ACE:"NO_PROPAGATE_INHERIT_ACE",
	INHERITED_ACE:"INHERITED_ACE"
		}
			for key in _flags.keys():
				if (flags & key):
					print '\t','\t',_flags[key],"is set!"


fileList = []
pathList = []
users = ['apple']
user = 'apple'

def scanFile(rootPath):
	security_descriptor = GetFileSecurity(rootPath)
	dacl = security_descriptor.GetSecurityDescriptorDacl()
	for ace_index in range(dacl.GetAceCount()):
		# rev => (ace_type, ace_flags)
		rev, access_mask, sid = dacl.GetAce(ace_index)
		user, group, account_type = LookupAccountSid(None, sid)
		print('user: {}\{}'.format(group, user), rev, access_mask)
	
	










