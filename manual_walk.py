#!/usr/bin/env python
# import sys
#import os
#import logging
import pif
import requests

# GLOBALS
GODADDY_USERNAME = "133585652"
GODADDY_PASSWORD = "Corine33."
# The files will be created automatically
LOGFILE = '/opt/dyndns/godaddy.log'
IPFILE = '/opt/dyndns/current_ip'

LOGINURL= 'https://sso.godaddy.com'






### BEGIN MAIN PROCEDURE



result = requests.get(LOGINURL)

print(result.url)
print(result.status_code)
#print( result.headers['content-type'] )
#print( result.encoding )
#print( result.text )

#result = requests.get(LOGINURL, auth=('user', 'pass'))

#'app=www&realm=idp&layout=layout.rebrand_layout.html&name=133585652&password=Corine33.'

payload = {'app:www', 'realm:idp', 'layout:layout.rebrand_layout.html', 'name:133585652', 'password:Corine33.'}


postresult = requests.post('https://sso.godaddy.com/v1/', data=payload)

print(postresult.url)
print(postresult.status_code)
print(postresult.headers['content-type'])
print(postresult.encoding)
print(postresult.text)
