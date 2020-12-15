# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 06:36:31 2020

@author: Marysia
Puzzle 15 part 2 from https://adventofcode.com/2020/day/15

Impressed, the Elves issue you a challenge: determine the 30000000th number
spoken. For example, given the same starting numbers as above:

Given 0,3,6, the 30000000th number spoken is 175594.
Given 1,3,2, the 30000000th number spoken is 2578.
Given 2,1,3, the 30000000th number spoken is 3544142.
Given 1,2,3, the 30000000th number spoken is 261214.
Given 2,3,1, the 30000000th number spoken is 6895259.
Given 3,2,1, the 30000000th number spoken is 18.
Given 3,1,2, the 30000000th number spoken is 362.

Given your starting numbers, what will be the 30000000th number spoken?
"""

#### Write here the puzzle input:
NUMBERS = [0, 6, 1, 7, 2, 19, 20]
LAST_ROUND = 30000000
###

Dictionary = {k:(v+1) for v, k in enumerate(NUMBERS)}

last_number = [0, len(Dictionary)+1]
i = len(NUMBERS)+2
while i < LAST_ROUND:
    while last_number[0] in Dictionary.keys():
        temp_key = last_number[0]
        temp_value = last_number[1]
        last_number[0] = last_number[1] - Dictionary[last_number[0]]
        last_number[1] = i
        Dictionary[temp_key] = temp_value
        if i == LAST_ROUND:
            break
        i += 1
    Dictionary[last_number[0]] = last_number[1]
    if i == LAST_ROUND:
        break
    last_number = [0, i]
    i += 1

print("The {}th number is {}.".format(LAST_ROUND, last_number[0]))
