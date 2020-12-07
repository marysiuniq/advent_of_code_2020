# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 06:00:47 2020

@author: Marysia

Puzzle 5 part 1 from https://adventofcode.com/2020/day/5

"""
import numpy as np

COUNT_VALID = 0

with open('boarding.txt', 'r') as file:
    BOARDING = file.readlines()

BOARDING = [x.strip() for x in BOARDING]

HIGHEST_NUMBER = 0
SEATS = np.ndarray.tolist(np.arange(8*128))

for line in BOARDING:
    i = 0
    START_ROW = 0
    END_ROW = 127
    START_COLUMN = 0
    END_COLUMN = 7
    while i < len(line):
        if i < 7: # rows
            if line[i] == 'F': # lower half
                END_ROW = END_ROW - int((END_ROW-START_ROW)/2) - 1
            elif line[i] == 'B': # upper half
                START_ROW = START_ROW + int((END_ROW-START_ROW)/2) + 1
            else:
                print("Wrong letter in poarding pass. Exit.")
                break
        else: # colums
            if line[i] == 'L': # lower half
                END_COLUMN = END_COLUMN - int((END_COLUMN-START_COLUMN)/2) -1
            elif line[i] == 'R': # upper half
                START_COLUMN = START_COLUMN + int((END_COLUMN-START_COLUMN)/2) + 1
            else:
                print("Wrong letter in poarding pass. Exit.")
                break
        i += 1
    print("Row {}, columnn {}, seat {}.".format(START_ROW, START_COLUMN, 
                                            8*START_ROW+START_COLUMN))
    NUMBER = 8*START_ROW+START_COLUMN
    if NUMBER > HIGHEST_NUMBER:
        HIGHEST_NUMBER = NUMBER
    SEATS.remove(NUMBER)

ind = 0
MY_SEAT = SEATS
for seat in SEATS:
    check = 1+seat
    if check in SEATS:
        MY_SEAT.pop(ind)
    else:
        ind += 1
    print(seat)
    

print("The highest seat ID is {}.".format(HIGHEST_NUMBER))
    
