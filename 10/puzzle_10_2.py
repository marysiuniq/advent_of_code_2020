# -*- coding: utf-8 -*-
"""
Created on Tue Dec  10 06:05:26 2020

@author: Marysia
Puzzle 10 part 2 from https://adventofcode.com/2020/day/10

To completely determine whether you have enough adapters,
you'll need to figure out how many different ways they can be arranged.
Every arrangement needs to connect the charging outlet to your device.
The previous rules about when adapters can successfully connect still apply.
You glance back down at your bag and try to remember why you brought so many
adapters; there must be more than a trillion valid ways to arrange them!
Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to
connect the charging outlet to your device?
"""

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [int(x.strip()) for x in INPUT]
INPUT.sort()
INPUT = [0] + INPUT

WAYS = [1] * len(INPUT)
JOLTAGE = [0]
INS = [0] * len(INPUT)
for i, num in enumerate(INPUT):
    if num-1 in INPUT:
        INS[i] += 1
    if num-2 in INPUT:
        INS[i] += 1
    if num-3 in INPUT:
        INS[i] += 1

for i, entry in enumerate(INS):
    if entry == 1 and i > 0:
        WAYS[i] = WAYS[i-1]
    if entry == 2:
        WAYS[i] = WAYS[i-1] + WAYS[i-2]
    if entry == 3:
        WAYS[i] = WAYS[i-1] + WAYS[i-2] + WAYS[i-3]

print("The total number of distinct ways is {}.".format(WAYS[-1]))
