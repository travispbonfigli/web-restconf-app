##
## Now that we have the list which contains dictionaries,
## with each dictionary in the list representing an individual
## interface and all of its IPv4 and IPv6 information!
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

print("Pretty cool! But now we need to programmatically parse out")
print("all of the values that we would want to see on our web page:")
print("for the different interfaces:")
print("Here is the interface name: {}".format(deviceInterfaces[0]["name"]))
print("Here is the interface description: {}".format(deviceInterfaces[0]["description"]))
print("Is the interface up: {}".format(deviceInterfaces[0]["enabled"]))
print("Here is the IPv4 address: {}".format(deviceInterfaces[0]['ietf-ip:ipv4']['address'][0]['ip']))
print("Here is the IPv4 address: {}".format(deviceInterfaces[0]['ietf-ip:ipv4']['address'][0]['netmask']))
##
## End of file...
