# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Please enter an ip address in the format (10.0.1.1): ')
while True:
    try:
        test = ip.split('.')
        byte1 = int(test[0])
        byte2 = int(test[1])
        byte3 = int(test[2])
        byte4 = int(test[3])
    except:
        print('Invalid IP Address')
        break
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
    