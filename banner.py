#!/usr/bin/env python

import urllib
import re
import pdb
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#M is the 
def finding(m):
    response = ''
    for n in range(2,12):
        print('trying: '+str(m)+'.'+str(n))
        try:
            response = urllib.urlopen('https://192.168.'+str(m)+'.' + str(n),context=ctx)
        except:
            next
            if response:
                html = response.read()
                print html
                i = re.search('trend', html)
                j = re.search('Trend', html)
                if i or j:
                    print('--success--')
                    print(m+'.'+n)



finding(10)
finding(20)
finding(30)

#192.168.10.121
#pdb.set_trace()
