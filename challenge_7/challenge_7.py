import os
import requests
import json
requests.packages.urllib3.disable_warnings()

IP_HOST="10.0.2.15"
os.system("ping -c 5 " + IP_HOST) 
INTERFACE="GigabitEthernet1"
USERNAME="cisco"
PASSWORD="Cisco123!"
URL="https://" + IP_HOST + "/restconf/data/ietf-interfaces:interfaces/interface=" + INTERFACE
HEADER={"Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}
AUTH= (USERNAME, PASSWORD)
status=requests.get(URL, auth=AUTH, headers=HEADER, verify=False)
status_code=str(status.status_code)

print(status_code)

if ( status_code == 200 ): 
   print ("Yes - interface is up - returning status code: 200")
else:
   print ("No - interface is down - returning status code:" + status_code)