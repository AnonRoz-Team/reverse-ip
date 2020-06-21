#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
P0 = "\033[0;35m"
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
	from bs4 import BeautifulSoup as bs
	from multiprocessing.pool import ThreadPool
except:
	print 'error : Install module requests and bs4'
udah_di_cek = []
web_list = []

try:
	os.system('clear')
	print '''%s
    ____            ________
   / __ \___ _   __/  _/ __ \\   %s|| Coded by D4RKSH4D0WS%s
  / /_/ / _ \ | / // // /_/ /   %s|| Reverse IP Unlimited%s
 / _, _/  __/ |/ // // ____/    %s|| IG @anonroz_team%s
/_/ |_|\___/|___/___/_/         %s|| FB gg.gg/AnonRoz-Team
'''%(C1,W0,C1,W0,C1,W0,C1,W0)
	op=open(sys.argv[1]).read().splitlines()
	print
	for ip in op:
		api=requests.get('https://tools.webservertalk.com/reverse-ip/?host='+ip).text
		for domains in bs(api,'html.parser').findAll('td',class_='text-left'):
			web_list.append(domains.text)
		print '%s[%s•%s] Reversing %s ...'%(W0,P0,W0,ip)
		print '%s[%s•%s] %s domains found for %s'%(W0,P0,W0,len(web_list),ip)
	print
	print '%s[%s+%s] Check the web first bro ...'%(W0,G0,W0)
	file=raw_input('\033[0;37m[\033[0;31m?\033[0;37m] Save results : ')
	if file == '':
		exit('%s[%s!%s] You stupid'%(W0,R0,W0))
	pol=raw_input('\033[0;37m[\033[0;31m?\033[0;37m] Input threadpool : ')
	if pol == '':
		exit('%s[%s!%s] You stupid'%(W0,R0,W0))
	print
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 rev.py target.txt \n%s[%s!%s] %sFill in target.txt can be ip or website not using http or https'%(W1,R1,W1,W0,W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))

def scan(web):
	try:
		cek=requests.get('http://'+web).url
		udah_di_cek.append(cek)
		sys.stdout.write("\r[\033[0;96m{}\033[0m] Checking : {}/{}".format(datetime.now().strftime('%H:%M:%S'),len(udah_di_cek),len(web_list)));sys.stdout.flush()
		open(file,"a+").write(cek+'\n')
	except:
		pass

ThreadPool(int(pol)).map(scan,web_list)
print '\n%s[\033[0;96m%s%s] Done, saved in %s'%(W0,datetime.now().strftime('%H:%M:%S'),W0,file)
