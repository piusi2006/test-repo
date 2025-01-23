from ncclient import manager
from pprintpp import pprint
import xmltodict
import xml.dom.minidom
# Above we are importing the 'Manager' Module from the 'Ncclient' python library.

# Here we are creating an instance of a device API call using the 'connect' method from the 'Manager' module and storing the result in a variable named device. 
with manager.connect(host='192.168.0.42', port=830, username='admin', 
                         password='test123', hostkey_verify=False,
                         device_params={}, allow_agent=False,
                         look_for_keys=False) as m:

# Here we are creating a for loop to iterate over every capability mentioned by the server in the hello message.
  for capability in m.server_capabilities:
      print('*' * 50)
      print(capability)

# Here we are defining our filter that we will use when we make our NETCONF request:
get_filter = """
<filter type="subtree">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>GigabitEthernet1</name>
            <ip>
              <address>
                <primary>
                  <address/>
                  <mask/>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </filter>
"""

# Next we pass the 'get_filter' and the subtree filter as a tuple parameter into our RPC method as it only takes 1 object as an argument:
netconf_reply = m.get(('subtree', get_filter))
print(netconf_reply)

