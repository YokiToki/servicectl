#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

PAM_LIB = True
try:
	import PAM
except ImportError:
	PAM_LIB = False
	import pam

class Systemctl():

	def get_path(self):
		return os.path.dirname(os.path.realpath(__file__))

	def run(self, pwd, action, service):
		os.system('echo \'%s\'|sudo -S systemctl %s %s.service' % (pwd, action, service))

	def is_enabled(self, service):
		out = os.popen("systemctl is-enabled %s.service" % (service,)).read().strip()
		if out == 'enabled':
			return True
		return False

	def is_active(self, service):
		out = os.popen("systemctl is-active %s.service" % (service,)).read().strip()
		if out == 'active':
			return True
		return False

	def description(self, service):
		return os.popen("systemctl show -p Description %s.service" % (service,)).read().replace("Description=", "").strip()

	def chk_pwd(self, pwd):
		user = os.getenv('USER')
		if pwd == None:
			return False
		if PAM_LIB:
			def pam_conv(a, q, d):
				return [(pwd, 0)]

			auth = PAM.pam()
			auth.start("passwd")
			auth.set_item(PAM.PAM_USER, user)
			auth.set_item(PAM.PAM_CONV, pam_conv)
			try:
				auth.authenticate()
				auth.acct_mgmt()
			except:
				return False
			else:
				return True

		else:

			auth = pam.pam()
			return auth.authenticate(user, pwd)
