#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, pam

class Systemctl():

	def run(self, pwd, action, service):
		os.system('echo \'%s\'|sudo -S systemctl %s %s.service' % (pwd, action, service))

	def is_active(self, service):
		out = os.popen("systemctl is-active %s.service" % (service,)).read().strip()
		if out == 'active':
			return True
		return False

	def chk_pwd(self, pwd):
		username = os.getenv('USER')
		p = pam.pam()
		if pwd == None:
			return False
		return p.authenticate(username, pwd)