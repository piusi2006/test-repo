# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
ignore = ["duplex", "alias", "configuration"]
filename = "config_sw1.txt"
with open(filename) as f:
    file = f.read().strip().split('\n')
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
            print(line)
    
