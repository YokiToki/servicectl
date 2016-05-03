#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, pam

class Systemctl():

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
		username = os.getenv('USER')
		p = pam.pam()
		if pwd == None:
			return False
		return p.authenticate(username, pwd)