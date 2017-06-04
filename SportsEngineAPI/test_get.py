import requests

api_test_page = 'https://user.sportngin.com/oauth/authorize?response_type=code&client_id=5100f9c6302f70a19393e71c3de5f52a&redirect_uri=http://www.cranfordhockeyclub.com/chcapitesting'

accesscode = requests.get( api_test_page )

print 'HEADERS     : ' + str( accesscode.headers )

access_code = accesscode.headers[ 'x-request-id' ]
print 'ACCESS CODE : ' + access_code 

post_url = 'https://user.sportngin.com/oauth/token?grant_type=authorization_code&client_id=5100f9c6302f70a19393e71c3de5f52a&client_secret=aea454ec3e2ea9bc9e3cf9c42dab99ee&code=' + access_code
print 'POST URL    : ' + post_url

r = requests.post( post_url )

print str( r )
