# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 05:59:30 2020

@author: Marysia
Puzzle 12 part 1 from https://adventofcode.com/2020/day/12

The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring at them
for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is
currently facing.

The ship starts by facing east. Only the L and R actions change the direction
the ship is facing.

Figure out where the navigation instructions lead. What is the Manhattan distance
(sum of the absolute values of its east/west position and its north/south position)
between that location and the ship's starting position?
"""

def ship_actions(position, face, direction, value):
    '''
    Checks and executes the actions of the ship.
    '''
    if direction == 'N':
        position[1] += value
    elif direction == 'S':
        position[1] -= value
    elif direction == 'E':
        position[0] += value
    elif direction == 'W':
        position[0] -= value
    elif direction == 'L':
        face += value
        if face >= 360:
            face -= 360
    elif direction == 'R':
        face -= value
        if face < 0:
            face += 360
    elif direction == 'F':
        direction = check_direction(face)
        position, face = ship_actions(position, face, direction, value)
    return position, face

def check_direction(face):
    '''
    Checks the face direction basing on the given angle.
    '''
    if face == 0:
        direction = 'E'
    elif face == 90:
        direction = 'N'
    elif face == 180:
        direction = 'W'
    elif face == 270:
        direction = 'S'
    return direction

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

FACE = 0 # 0 degrees
POSITION = [0, 0] # position in x- and in y-direction

for line in INPUT:
    POSITION, FACE = ship_actions(POSITION, FACE, line[0], int(line[1:]))

print("The ship's Manhattan distance is {}.".format(abs(POSITION[0])+abs(POSITION[1])))
