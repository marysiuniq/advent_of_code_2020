# -*- coding: utf-8 -*-
"""
Created on Tue Dec  10 06:05:26 2020

@author: Marysia
Puzzle 10 part 1 from https://adventofcode.com/2020/day/10

Each of your joltage adapters is rated for a specific output joltage
(your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts
lower than its rating and still produce its rated output joltage.

Find a chain that uses all of your adapters to connect the charging outlet
to your device's built-in adapter and count the joltage differences
between the charging outlet, the adapters, and your device. What is the
number of 1-jolt differences multiplied by the number of 3-jolt differences?
"""

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [int(x.strip()) for x in INPUT]

DIFF_1 = 0
DIFF_2 = 0
DIFF_3 = 0
JOLTAGE = 0
for i in range(len(INPUT)):
    if JOLTAGE + 1 in INPUT:
        JOLTAGE += 1
        DIFF_1 += 1
    elif JOLTAGE + 2 in INPUT:
        JOLTAGE += 2
        DIFF_2 += 1
    elif JOLTAGE + 3 in INPUT:
        JOLTAGE += 3
        DIFF_3 += 1

print("The answer is {}.".format(DIFF_1*(DIFF_3+1)))
