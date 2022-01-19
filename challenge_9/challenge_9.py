import json
import requests
requests.packages.urllib3.disable_warnings()

restconf_router_ip = input("Router IP? ")
restconf_user = input("Username? ")
restconf_psw = input("Password? ")

basicauth = (restconf_user, restconf_psw)
headers = { "Accept": "application/yang-data+json",
"Content-type":"application/yang-data+json" }

api_url = "https://{0}/restconf/data/ietf-interfaces:interfaces".format(restconf_router_ip)
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

response_json = resp.json()
print(json.dumps(response_json, indent=4))