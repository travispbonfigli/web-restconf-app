##
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
print('Here is that same JSON string now as a JSON object thanks to json.loads!')
print(jsonData)
print()

deviceInterfaces = jsonData["ietf-interfaces:interfaces"]["interface"]
print('Here is the deviceInterfaces data...')
print(deviceInterfaces)
print()

interface_info = [ ]
for interface in deviceInterfaces:
   if "ietf-ip:ipv4" in interface:
       if "address" in interface["ietf-ip:ipv4"]:
            interface_name = interface["name"]
            interface_desc = interface.get("description", "")
            ip_address = interface["ietf-ip:ipv4"]["address"][0]["ip"]
            subnet_mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"]
            interface_enabled = interface["enabled"]
            interface_info.append((interface_name, interface_desc, ip_address, subnet_mask, interface_enabled))
print('The contents of the list which are just tuples of the interface values:')
print(interface_info)
    
##
## End of file...
