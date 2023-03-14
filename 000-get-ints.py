##
## Let's start out by just taking a look at what the
## Cisco CSR1000v is going to return to us using the 
## OPEN IETF interface YANG data model and review
## the base Python code that will fire up our Flask
## web application!
##
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apiURI = "https://192.168.1.129/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-type":"application/yang-data+json"
}

basicauth = ("cisco", "cisco123!")

httpResponse = requests.get(apiURI, auth=basicauth, headers=headers, verify=False)
print('Printing the raw string of text that represents the JSON object...')
print(httpResponse.text)

##
## End of file...
