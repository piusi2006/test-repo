print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]

for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )