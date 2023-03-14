##
##
from flask import Flask, jsonify, render_template
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

api_url = "https://192.168.1.129/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-type":"application/yang-data+json"
}

basicauth = ("cisco", "cisco123!")

def netmask_to_cidr(netmask):
    # Split the netmask into its four octets
    octets = netmask.split('.')

    # Convert each octet to binary and concatenate them
    binary = ''.join([bin(int(octet))[2:].zfill(8) for octet in octets])

    # Count the number of '1's in the binary string
    cidr = str(sum([int(bit) for bit in binary]))

    # Return the CIDR notation
    return cidr

@app.route('/')
def get_ip_addresses():
    response = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    response_json = json.loads(response.text)
    interfaces = response_json["ietf-interfaces:interfaces"]["interface"]
    interface_info = [ ]
    for interface in interfaces:
        if "ietf-ip:ipv4" in interface:
            if "address" in interface["ietf-ip:ipv4"]:
                interface_name = interface["name"]
                interface_desc = interface.get("description", "")
                ip_address = interface["ietf-ip:ipv4"]["address"][0]["ip"]
                subnet_mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"]
                cidr_notation = netmask_to_cidr(subnet_mask)
                interface_enabled = interface["enabled"]
                interface_info.append((interface_name, interface_desc, ip_address, subnet_mask, cidr_notation, interface_enabled))
    return render_template('index.html', interface_info=interface_info)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')

##
## End of file...
