# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:36:23 2020

@author: Marysia

Puzzle 3 part 2 from https://adventofcode.com/2020/day/3#part2

What do you get if you multiply together the number of trees
encountered on each of the listed slopes?
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

with open('map.txt', 'r') as file:
    MAP = file.readlines()

MAP = [x.strip() for x in MAP]
ROW_LENGTH = len(MAP[0])
STEP_RIGHT = [1, 3, 5, 7, 1]
STEP_DOWN = [1, 1, 1, 1, 2]
COUNTER = [0] * len(STEP_RIGHT)
PRODUCT = 1

for case, step_right in enumerate(STEP_RIGHT):
    step_down = STEP_DOWN[case]
    i = 0
    COLUMN = 0
    print(case, step_right, step_down)
    while i < len(MAP):
        if COLUMN < (ROW_LENGTH):
            entry = MAP[i][COLUMN % (ROW_LENGTH)]
            print(entry, i, COLUMN)
            i += step_down
            COLUMN += step_right
        else:
            COLUMN -= ROW_LENGTH
            entry = MAP[i][COLUMN % (ROW_LENGTH)]
            print(entry, i, COLUMN)
            i += step_down
            COLUMN += step_right
        if entry == '#':
            COUNTER[case] += 1
    PRODUCT *= COUNTER[case]

print("The number of trees encountered multiplied together is {}.".format(PRODUCT))
