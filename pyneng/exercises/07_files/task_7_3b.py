# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
with open("CAM_table.txt") as f:
    file = f.read().split('\n')
    vlan_list = []
    for line in file:
        if line.startswith(' ') and 'Gi' in line:
             vlan_list.append(line.split())
    for item in vlan_list:
        item[0] = int(item[0])   
    
    user = int(input("Enter VLAN number: "))
    
    for vlan in sorted(vlan_list):
        if user in vlan:
            vlan.remove('DYNAMIC')
            v, mac, port = vlan
            print("{:<9}{:20}{}".format(v, mac, port))