# This is an example of using the 'Requests' library to interact with REST APIs on the DNAC platform.
# This script is performing an Authentication request.

import requests
import my_report

url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"  # The URI (Endpoint) that we will be contacting.

# Below are the headers for the request, if needed.
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

# Here we are making a request using the 'request' method from the requests library and we store the response as an object.
response = requests.request("POST", url, auth=("devnetuser", "Cisco123!"), verify=False)
my_token = response.json()['Token']  # Here we are using JSON to parse the response using the value that is stored in the dict key 'Token'
# so that it can be stored in python's native structure and later reused.

# Next we are issuing a GET request to retrieve the network devices.

url = "https://sandboxdnac.cisco.com/api/v1/network-device"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': my_token
}

get_response = requests.request("GET", url, headers=headers, verify=False)
devices = get_response.json()['response']

report_devices = []

for device in devices:
    report_devices.append({
        "hostname": device["hostname"],
        "platform": device["platformId"],
        "mgmt_ip": device["managementIpAddress"],
        "version": device["softwareVersion"]})

report_name = 'DNAC Devices Report'
my_report.print_report(report_name, report_devices)
