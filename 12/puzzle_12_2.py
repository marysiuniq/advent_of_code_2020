# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 07:03:24 2020

@author: Marysia
Puzzle 12 part 1 from https://adventofcode.com/2020/day/12

Almost all of the actions indicate how to move a waypoint which is relative to
the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise)
the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the
given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the
given value.
The waypoint starts 10 units east and 1 unit north relative to the ship.
The waypoint is relative to the ship; that is, if the ship moves, the waypoint
moves with it.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""

def ship_actions(position, waypoint, direction, value):
    '''
    Updates the positions of the ship or waypoint.
    '''
    if direction == 'N':
        waypoint[1] += value
    elif direction == 'S':
        waypoint[1] -= value
    elif direction == 'E':
        waypoint[0] += value
    elif direction == 'W':
        waypoint[0] -= value
    elif direction == 'L':
        relative_pos_waypoint = [waypoint[0]-position[0], WAYPOINT[1]-position[1]]
        rotated_pos = rotate_waypoint_left(value, relative_pos_waypoint)
        waypoint[0] = position[0] + rotated_pos[0]
        waypoint[1] = position[1] + rotated_pos[1]
    elif direction == 'R':
        relative_pos_waypoint = [waypoint[0]-position[0], waypoint[1]-position[1]]
        rotated_pos = rotate_waypoint_left(360-value, relative_pos_waypoint)
        waypoint[0] = position[0] + rotated_pos[0]
        waypoint[1] = position[1] + rotated_pos[1]
    elif direction == 'F':
        relative_pos_waypoint = [waypoint[0]-position[0], waypoint[1]-position[1]]
        position[0] += value*relative_pos_waypoint[0]
        position[1] += value*relative_pos_waypoint[1]
        waypoint[0] += value*relative_pos_waypoint[0]
        waypoint[1] += value*relative_pos_waypoint[1]
    return position, waypoint

def rotate_waypoint_left(angle, position):
    '''
    Finds the relative waypoint position after rotation about given angle.
    '''
    if angle == 90:
        tmp = position[0]
        position[0] = -position[1]
        position[1] = tmp
    elif angle == 180:
        position[0] = -position[0]
        position[1] = -position[1]
    elif angle == 270:
        tmp = position[0]
        position[0] = position[1]
        position[1] = -tmp
    return position

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

POSITION = [0, 0] # position of the ship in x- and in y-direction
WAYPOINT = [10, 1] # position of the waypoint in x- and in y-direction

for line in INPUT:
    POSITION, WAYPOINT = ship_actions(POSITION, WAYPOINT, line[0], int(line[1:]))

print("The ship's Manhattan distance is {}.".format(abs(POSITION[0])+abs(POSITION[1])))
