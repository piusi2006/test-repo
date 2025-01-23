# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
ignore = ["duplex", "alias", "configuration"]
source = "config_sw1.txt"
dest = "config_sw1_v2.txt"
with open(source) as src, open(dest, 'w') as dst:
    file = src.read().strip().split('\n')
    while '!' in file:
        file.remove('!')
    for line in file:
        if ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        elif '!' in line:
            pass
        else:
            dst.write(f"{line}\n")
    
