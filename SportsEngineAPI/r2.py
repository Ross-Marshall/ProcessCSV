from urllib2 import Request, urlopen, URLError

#request = Request('https://api.sportngin.com/user_personas')
request = Request('https://user.sportngin.com/oauth/authorize?response_type=code&client_id=5100f9c6302f70a19393e71c3de5f52a&redirect_uri=http://www.cranfordhockeyclub.com/chcapitesting')  #GET

try:
    response = urlopen(request)
    se = response.read()
    print str(se)
except URLError, e:
    print 'There was an error: Code = ', e
