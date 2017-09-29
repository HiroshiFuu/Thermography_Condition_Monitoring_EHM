import pycurl
import urllib
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--hp', required=True, help='Mobile phone number') 
ap.add_argument('-m', '--msg', required=True, help='Message to send to') 
args = vars(ap.parse_args())

Url = "http://smsgateway.me/api/v3/messages/send";
c = pycurl.Curl()
formdata = {'number':args['hp'], 'message':args['msg'], 'device':'61672', 'email':'rr.iotlab@gmail.com', 'password':'1qaz2wsx'}
result = urllib.urlencode(formdata)
c.setopt(pycurl.POST, 5)
c.setopt(pycurl.POSTFIELDS, result)
c.setopt(pycurl.URL, Url)
#c.setopt(pycurl.RETURNTRANSFER,1)
c.setopt(pycurl.HEADER , False)
c.setopt(pycurl.SSL_VERIFYPEER, False)
c.perform()
c.close()
