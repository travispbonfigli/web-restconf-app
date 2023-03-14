##
## Now, let's convert that raw string of JSON data we got back
## from our HTTP response object and convert it to a Python
## dictionary using json.loads()
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

jsonData = json.loads(httpResponse.text)
print('Here is that same JSON raw string of JSON text as a Python dictionary!')
print('All thanks to the built-in Python json module and the loads method!')
print(jsonData)
print()

##
## End of file...
