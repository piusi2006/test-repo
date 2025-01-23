# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
while True:
    ip = input('Please enter an ip address in the format (10.0.1.1): ')
    try:
        test = ip.split('.')
        byte1 = int(test[0])
        byte2 = int(test[1])
        byte3 = int(test[2])
        byte4 = int(test[3])
    except:
        print('Invalid IP Address')
    else:
        if byte1 in range(1,224):
            print('unicast')
        elif byte1 in range(224,240):
            print('multicast')
        elif '255.255.255.255' in ip:
            print('local broadcast')
        elif '0.0.0.0' in ip:
            print('unassigned')
        else:
            print('Invalid IP Address')