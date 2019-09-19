import vrliFunctions
import logging
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)

# First we use the login token to get a session 'bearer' token
resp = vrliFunctions.sessions()
if resp.status_code != 200:
    print 'Something is wrong with request status code returned was',(resp.status_code)
else:
    bearerToken = resp.json()["sessionId"]
    logging.debug('bearerToken value: ' + bearerToken)

# We can now make calls to functions from the library we imported

resp = vrliFunctions.getUsers(bearerToken)
if resp.status_code != 200:
    print 'Something is wrong with request status code returned was',(resp.status_code)
else:
    pprint(resp.json())
