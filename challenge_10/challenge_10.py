import json
import requests







ipHosts = "192.168.56.103"
username = "cisco"
password = "cisco123!"
url = f"https://{ipHosts}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
basicauth = (username, password)

headers = {"Accept": "application/yang-data+json", "Content-type": "application/yang-data+json"}

response = request.options(url, auth=basicauth, headers=headers, verify=False)

print(statusCode)

for k, v in response.headers.items():
    print(f"{k}: {v}")

print(response.raw.version)