# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 05:58:11 2020

@author: Marysia
Puzzle 13 part 1 from https://adventofcode.com/2020/day/13

Your notes (your puzzle input) consist of two lines. The first line is your
estimate of the earliest timestamp you could depart on a bus. The second line
lists the bus IDs that are in service according to the shuttle company; entries
that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you
can take to the airport.

What is the ID of the earliest bus you can take to the airport multiplied by
the number of minutes you'll need to wait for that bus?
"""

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

TIMESTAMP = int(INPUT[0])
BUSSES = [int(s) for s in INPUT[1].split(',') if s.isdigit()]

TIMES = {new_list: [] for new_list in BUSSES}

for bus in BUSSES:
    TIMES[bus] = TIMESTAMP - TIMESTAMP%bus + bus

TIMES = {k: v for k, v in sorted(TIMES.items(), key=lambda item: item[1])}
NEXT_BUS = next(iter(TIMES))
MINUTES_TO_WAIT = TIMES[NEXT_BUS] - TIMESTAMP

print("The answer is {}.".format(NEXT_BUS*MINUTES_TO_WAIT))
