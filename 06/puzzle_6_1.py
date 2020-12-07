# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 06:15:33 2020

@author: Marysia

Puzzle 6 part 1 from https://adventofcode.com/2020/day/6
For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?
"""

with open('answers.txt', 'r') as file:
    ANSWERS = file.readlines()

for i, line in enumerate(ANSWERS):
    if line.isspace():
        ANSWERS[i] = 'marysia'

ANSWERS = [x.strip() for x in ANSWERS]

COUNT = 0
i = 0

while i < len(ANSWERS):
    LIST = []
    while i < len(ANSWERS) and ANSWERS[i] != 'marysia':
        for entry in ANSWERS[i]:
            if not entry in LIST:
                LIST += [entry]
        i += 1
    COUNT += len(LIST)
    i += 1
#    TEST = [_ in STRING_TO_CHECK for _ in KEYWORDS]

print("The sum of counts is {}.".format(COUNT))
