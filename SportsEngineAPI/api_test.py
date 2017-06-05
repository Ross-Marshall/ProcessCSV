import httplib
#from http.client import HTTPSConnection
from base64 import b64encode
import sys
import urllib
import ast

#
# Get the variables from the properties file.
#
dicts_from_file = []
with open('api.properties','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))

d = dicts_from_file[0]

client_template        = d[ 'client_template' ] 
secret                 = d[ 'secret' ]
login_url              = d[ 'login_url' ]
redirect_url           = d[ 'redirect_url' ]
client_id              = d[ 'client_id' ]
redirect_template      = d[ 'redirect_template' ]
api_site_id            = d[ 'api_site_id' ]
access_url             = d[ 'access_url' ]
secret_template        = d[ 'secret_template' ]
authorization_template = d[ 'authorization_template' ]
username               = d[ 'username' ]
password               = d[ 'password' ]
url                    = d[ 'url' ]

#This sets up the https connection
#url = ''
c = httplib.HTTPSConnection( url )
#c = httplib.HTTPSConnection( 'user.sportngin.com' )

#we need to base 64 encode it 
#and then decode it to acsii as python 3 stores it as a byte string
userAndPass = b64encode( username + ':' + password.encode('utf-8')  ).decode("ascii")

print 'userAndPass [' + userAndPass + ']'
headers = { 'Authorization' : 'Basic %s' %  userAndPass }

#client_id    = '5100f9c6302f70a19393e71c3de5f52a'
#secret       = 'aea454ec3e2ea9bc9e3cf9c42dab99ee'
#redirect_url = 'http://www.cranfordhockeyclub.com/chcapitesting'
#api_site_id  = '9497'

login_url = '/oauth/authorize?response_type=code&client_id=[CLIENT_IDENTIFIER]&redirect_uri=[REDIRECT_URI]'
login_url = login_url.replace( '[CLIENT_IDENTIFIER]', client_id ).replace( '[REDIRECT_URI]', redirect_url ) 
print 'url       [' + url + ']'
print 'login_url [' + login_url + ']'
#login_url = login_url.replace( client_template, client_id ).replace( redirect_template, redirect_url )
print 'login_url [' + login_url + ']'
print '-----------------------------------------------------'

#then connect
c.request('GET', login_url, headers=headers)

#get the response back
res = c.getresponse()

print 'response ====> ' + str( res )
print 'Request after Step 1 POST getheader : ' + str( res.getheader )
print 'Request after Step 1 POST msg       : ' + str( res.msg )
print 'Request after Step 1 POST verson    : ' + str( res.version )
print 'Request after Step 1 POST status    : ' + str( res.status )
print 'Request after Step 1 POST reason    : ' + str( res.reason )
#print 'Request after Step 1 POST read()    : ' + str( res.read() )

# at this point you could check the status etc
# this gets the page text
data = res.read() 
print 'Login data: ' + data
print 'Data 1 : data ====> ' + str( data )

code=data.split('=')[2].split('"')[0]
print 'code = ' + code

#access_url='https://user.sportngin.com/oauth/token?grant_type=authorization_code&client_id=[CLIENT_IDENTIFIER]&client_secret=[CLIENT_SECRET]&code=[AUTHORIZATION CODE]'.replace( '[CLIENT_IDENTIFIER]', client_id ).replace( '[CLIENT_SECRET]', secret ).replace( '[AUTHORIZATION CODE]', code )
access_url='/oauth/token?grant_type=authorization_code&client_id=[CLIENT_IDENTIFIER]&client_secret=[CLIENT_SECRET]&code=[AUTHORIZATION CODE]'.replace( '[CLIENT_IDENTIFIER]', client_id ).replace( '[CLIENT_SECRET]', secret ).replace( '[AUTHORIZATION CODE]', code )
access_url2=access_url.replace( client_template, client_id ).replace( secret_template, secret ).replace( authorization_template, code )

print 'access_url  = ' + access_url
print 'access_url2 = ' + access_url2

params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

#c.request('POST', access_url)
c.request('POST', access_url, params, headers)
res = c.getresponse()
print 'Request after Step 2 POST getheaders: ' + str( res.getheaders() )
print 'Request after Step 2 POST msg       : ' + str( res.msg )
print 'Request after Step 2 POST verson    : ' + str( res.version )
print 'Request after Step 2 POST status    : ' + str( res.status )
print 'Request after Step 2 POST reason    : ' + str( res.reason )
data_str = res.read()
print str( type(data)  )
data = ast.literal_eval( data_str )
print 'Data 2 : data ====> ' + str( data )
  
access_token = data['access_token']
refresh_token = data['refresh_token']

print 'access_token  : ' + access_token
print 'refresh_token : ' + refresh_token

test_access_url='/oauth/me?access_token="' + access_token + '"'
print 'test_access_url : ' + test_access_url
 
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
c.request('GET', test_access_url, headers=headers)

#get the response back
res = c.getresponse()

print 'response ====> ' + str( res )
print 'Request after Step 3 GET getheader : ' + str( res.getheaders() )
print 'Request after Step 3 GET msg       : ' + str( res.msg )
print 'Request after Step 3 GET verson    : ' + str( res.version )
print 'Request after Step 3 GET status    : ' + str( res.status )
print 'Request after Step 3 GET reason    : ' + str( res.reason )
data_str = res.read()
print str( type(data_str)  )
print data_str
#data = ast.literal_eval( data_str )
#print 'Data 3 : data ====> ' + str( data )

