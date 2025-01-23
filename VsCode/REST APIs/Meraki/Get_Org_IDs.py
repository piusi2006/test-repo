# This is a script to make API call to Meraki Dashboard to retrieve the Organization Networks. You will need the Organization ID for this.
import requests
import json
from prettytable import PrettyTable

url = "https://api.meraki.com/api/v1/organizations/570268302815789229/networks"
apikey = 'Bearer 517104080ea9ee1e8cc9c22710794bf3e55dc38a'

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': apikey
}

response = requests.request("GET", url, headers=headers, data=payload)
network = response.json()
headers = list(network[2])

def print_report(report_name, networks):

    table = PrettyTable()
    table.field_names = ["id", "name", "productTypes"]
    for item in networks:
        table.add_row(
            [item['id'],
            item['name'],
            item['productTypes']]
        )
        
    print(f"\n*** MY REPORT: {report_name} ***\n")
    print(table)


report = "Meraki ERM Organization Networks"

print_report(report, network)
