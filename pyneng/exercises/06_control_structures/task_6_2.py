# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
while True:
    ip = input('Please enter an ip address in the format (10.0.1.1): ')
    test = ip.split('.')
    ip_bin = '{:08b}'.format(int(test[0]))
    byte1 = int(ip_bin, 2)
    if byte1 in range(1,224):
        print('unicast')
    elif byte1 in range(224,240):
        print('multicast')
    elif '255.255.255.255' in ip:
        print('local broadcast')
    elif '0.0.0.0' in ip:
        print('unassigned')
    else:
        print('unused')
        

