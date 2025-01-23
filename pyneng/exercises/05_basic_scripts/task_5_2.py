# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
user = input('Please enter your network (format should be e.g. 10.1.1.0/24): ')
response = user.split('/')
prefix = response[0].split('.')
mask = f"/{int(response[1])}"
binary_mask = '1' * int(response[1]) + '0' * (32 - int(response[1]))
new_prefix = f"""
Network:
{prefix[0]:8}  {prefix[1]:8}  {prefix[2]:8}  {prefix[3]:8}
{int(prefix[0]):08b}  {int(prefix[1]):08b}  {int(prefix[2]):08b}  {int(prefix[3]):08b}

Mask:
{mask}
{int(binary_mask[0:8], 2):<8}  {int(binary_mask[8:16], 2):<8}  {int(binary_mask[16:24], 2):<8}  {int(binary_mask[24:], 2):<8}
{binary_mask[0:8]:8}  {binary_mask[8:16]:8}  {binary_mask[16:24]:8}  {binary_mask[24:]:8}
"""
print(new_prefix)