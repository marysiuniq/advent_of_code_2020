# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:36:23 2020

@author: Marysia

Puzzle 3 part 1 from https://adventofcode.com/2020/day/3

Starting at the top-left corner of your map and following
a slope of right 3 and down 1, how many trees would you encounter?
"""

with open('map.txt', 'r') as file:
    MAP = file.readlines()

MAP = [x.strip() for x in MAP]
ROW_LENGTH = len(MAP[0])
COLUMN = 0
STEP_RIGHT = 3
STEP_DOWN = 1
COUNTER = 0

i = 0
while i < len(MAP):
    if COLUMN < (ROW_LENGTH):
        ENTRY = MAP[i][COLUMN % (ROW_LENGTH)]
        print(ENTRY, i, COLUMN)
        i += STEP_DOWN
        COLUMN += STEP_RIGHT
    else:
        COLUMN -= ROW_LENGTH
        #i -= STEP_DOWN
        ENTRY = MAP[i][COLUMN % (ROW_LENGTH)]
        print(ENTRY, i, COLUMN)
        i += STEP_DOWN
        COLUMN += STEP_RIGHT
    if ENTRY == '#':
        COUNTER += 1

print("The number of trees encountered is {}.".format(COUNTER))
