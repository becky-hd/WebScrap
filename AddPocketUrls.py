import sys
import pocket
from pocket import Pocket

consumer_key = '33911-bc95ccb4c509ede133a36791'

request_token = Pocket.get_request_token(
		    consumer_key=consumer_key,
		    redirect_uri='http://www.whatever.com',
			)
print 'request token'
print request_token

auth_url = Pocket.get_auth_url(
		    code=request_token,
		    redirect_uri='http://www.whatever.com',
			)
print 'Please authorize the app using the following url and press ENTER here'
print auth_url
raw_input()

access_token = Pocket.get_access_token(
		    consumer_key=consumer_key,
		        code=request_token,
			)
print 'Got authenticated request token'
print request_token


def add_url(url):
	print 'adding', url
	print Pocket_instance.add(url=url)

Pocket_instance = Pocket(consumer_key, access_token)
for arg in sys.argv[1:]:
	if arg.startswith('http'):
		add_url(arg)
	else:
		print 'Reading urls from %r' % arg
		for line in open(arg):
			add_url(line)
