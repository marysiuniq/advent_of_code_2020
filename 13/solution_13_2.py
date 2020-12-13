# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:45:22 2020

@author: Suitable_Split_1524
https://www.reddit.com/user/Suitable_Split_1524/

"""

with open("input.txt", "r") as f:
    f = f.read().splitlines()

busses = [(int(b), i) for i, b in enumerate(f[1].split(",")) if b != "x"]

jump = i = busses[0][0] 
for b in busses[1:]:
    while (i+b[1])%b[0] != 0:
        i += jump
    jump *= b[0]

print(i)