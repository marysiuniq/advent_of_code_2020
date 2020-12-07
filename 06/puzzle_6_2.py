# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 06:15:33 2020

@author: Marysia

Puzzle 6 part 2 from https://adventofcode.com/2020/day/6
For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""
from collections import Counter
import string

with open('answers.txt', 'r') as file:
    ANSWERS = file.readlines()

for i, line in enumerate(ANSWERS):
    if line.isspace():
        ANSWERS[i] = 'marysia'

ANSWERS = [x.strip() for x in ANSWERS]

COUNT = 0
i = 0

ALPHABET_STRING = string.ascii_lowercase

while i < len(ANSWERS):
    LIST = []
    STRING_1 = Counter(ALPHABET_STRING)
    while i < (len(ANSWERS)) and ANSWERS[i] != 'marysia':
        STRING_2 = Counter(ANSWERS[i])
        COMMON_DICT = STRING_1 & STRING_2
        STRING_1 = Counter(''.join(list(COMMON_DICT.elements())))
        i += 1
    COUNT += len(COMMON_DICT)
    i += 1
#    TEST = [_ in STRING_TO_CHECK for _ in KEYWORDS]

print("The sum of counts is {}.".format(COUNT))
