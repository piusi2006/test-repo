import requests
from prettytable import PrettyTable

url = "https://api.meraki.com/api/v1/organizations/570268302815789229/devices"
apikey = 'Bearer 517104080ea9ee1e8cc9c22710794bf3e55dc38a'

payload = {}
headers = {
    "Accept": 'application/json',
    "Authorization": apikey
}

response = requests.request("GET", url, headers=headers, data=payload)
payload1 = response.json()

table = PrettyTable()
table.field_names = ["no.", "name", "serial", "productType", "model", "firmware"]
number = 0
for item in payload1:
    number += 1 
    table.add_row(
        [number,
         item['name'],
         item['serial'],
         item['productType'],
         item['model'],
         item['firmware']]
    )

report = "ERM Network Devices"
print(f"\n***Report Name: {report}***\n")
print(table)