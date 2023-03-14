##
## Now that we have our Python dictionary object that we
## can programmatically work with, let's go ahead and parse
## some data from it! Specifically, I want to parse/pull out
## the list that would contain all of the CSR1kv interfaces!
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
print('Here is that same JSON raw string of text as a Python dictionary!')
print('All thanks to the built-in Python json module and the loads method!')
print(jsonData)
print()

print('Here, we programmatically parse some of the information from')
print('our new Python dictionary - thanks again, json.loads()!')
print('Here is the Python parse action: jsonData["ietf-interfaces:interfaces"]["interface"]')
deviceInterfaces = jsonData["ietf-interfaces:interfaces"]["interface"]
print(deviceInterfaces)
print()

##
## End of file...
