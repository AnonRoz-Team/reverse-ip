#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
# RIKOD BOLEH TAPI
# JANGAN HAPUS NAMA AUTHOR YA ANJENG !
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
	os.system('pip2 install requests bs4')

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
	file=raw_input('%s[%s•%s] Save results : '%(W0,C0,W0))
	if file == '':
		exit('%s[%s!%s] You stupid'%(W0,R0,W0))
	print
	for ip in op:
		web=requests.post('https://tools.hack.co.id/reverseip/',data={'domain':ip}).text
		parse=bs(web,'html.parser').find('table').findAll('a')
		for domains in parse:
			open(file,'a+').write(domains['href']+'\n')
		print '%s[%s•%s] Reversing %s ...'%(W0,P0,W0,ip)
		print '%s[%s•%s] %s domains found for %s'%(W0,P0,W0,len(parse),ip)
	print
	print '%s[%s•%s] Done, saved in %s'%(W0,C0,W0,file)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 rev.py target.txt \n%s[%s!%s] %sFill in target.txt with ip not with website'%(W1,R1,W1,W0,W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))

