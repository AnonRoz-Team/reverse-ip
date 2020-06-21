#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"

try:
	import requests, os, sys, json
	from datetime import datetime
	from multiprocessing.pool import ThreadPool
except:
	print 'error : Install modul requests'
udah_di_cek = []
web_list = []

try:
	os.system('clear')
	print '''%s
    ____            ________
   / __ \___ _   __/  _/ __ \\
  / /_/ / _ \ | / // // /_/ /   %s|| Coded by D4RKSH4D0WS%s
 / _, _/  __/ |/ // // ____/    %s|| Reverse IP Unlimited%s
/_/ |_|\___/|___/___/_/
'''%(C1,W0,C1,W0,C1)
	op=open(sys.argv[1]).read().splitlines()
	print
	for ip in op:
		api=requests.get('http://reverseip.logontube.com/?url='+ip+'&output=json').text
		for domains in json.loads(api)['response']['domains']:
			web_list.append(domains)
		print '%s[%s*%s] %sReversing %s ...'%(W1,R1,W1,W0,ip)
		print '%s[%s*%s] %s%s domains found for %s'%(W1,R1,W1,W0,json.loads(api)['response']['domain_count'],ip)
	print
	print '%s[%s*%s] %sCheck the web first bro ...'%(W1,G1,W1,W0)
	file=raw_input('\033[1;37m[\033[1;31m?\033[1;37m] \033[0;37mSave results : ')
	if file == '':
		exit('%s[%s!%s] %sYou stupid'%(W1,R1,W1,W0))
	pol=raw_input('\033[1;37m[\033[1;31m?\033[1;37m] \033[0;37mInput threadpool : ')
	if pol == '':
		exit('%s[%s!%s] %sYou stupid'%(W1,R1,W1,W0))
	print
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 rev.py ip.txt'%(W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))

def scan(web):
	try:
		cek=requests.get('http://'+web).url
		udah_di_cek.append(cek)
		sys.stdout.write("\r[\033[0;96m{}\033[0m] Checking : {}/{}".format(datetime.now().strftime('%H:%M:%S'),len(udah_di_cek),len(web_list)))
		sys.stdout.flush()
		open(file,"a+").write(cek+'\n')
	except:
		pass

ThreadPool(int(pol)).map(scan,web_list)
print '\n%s[\033[0;96m%s%s] Done, saved in %s'%(W0,datetime.now().strftime('%H:%M:%S'),W0,file)
