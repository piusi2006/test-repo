# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

with open("ospf.txt") as f:
    for line in f:
        ospf = line.strip().split()
        prefix = ospf[1]
        AD_Metric = ospf[2].strip('[').strip(']')
        Next_Hop = ospf[4].strip(',')
        update = ospf[5].strip(',')
        outbound = ospf[6]
        print("""
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
""".format(prefix, AD_Metric, Next_Hop, update, outbound).lstrip())
