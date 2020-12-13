# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 06:36:49 2020

@author: Marysia (I used the solution_13_2.py as a hint but I think it works
just for coprime bus numbers. I believe that mine would work for arbitrary numbers.)
Puzzle 13 part 2 from https://adventofcode.com/2020/day/13

For example, suppose you have the same list of bus IDs as above:

7,13,x,x,59,x,31,19
An x in the schedule means there are no constraints on what bus IDs must depart
at that time.

This means you are looking for the earliest timestamp (called t) such that:

Bus ID 7 departs at timestamp t.
Bus ID 13 departs one minute after timestamp t.
There are no requirements or restrictions on departures at two or three minutes
after timestamp t.
Bus ID 59 departs four minutes after timestamp t.
There are no requirements or restrictions on departures at five minutes after
timestamp t.
Bus ID 31 departs six minutes after timestamp t.
Bus ID 19 departs seven minutes after timestamp t.
The only bus departures that matter are the listed bus IDs at their specific
offsets from t. Those bus IDs can depart at other times, and other bus IDs can
depart at those times. For example, in the list above, because bus ID 19 must
depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7 will
always also be departing with bus ID 19 at seven minutes after timestamp t.

In this example, the earliest timestamp at which this occurs is 1068781

What is the earliest timestamp such that all of the listed bus IDs depart at
offsets matching their positions in the list?
"""

import math

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

def lcm(x_in, y_in):
    '''
    Computes the least common multiply of two numbers
    '''
    return x_in * y_in // math.gcd(x_in, y_in)

BUSES = INPUT[1].split(',')

DIFFERENCES = []
VALID_BUSES = []
for i, bus in enumerate(BUSES):
    if not bus == 'x':
        DIFFERENCES += [i]
        VALID_BUSES += [int(bus)]

step = timestamp = VALID_BUSES[0]
for i, bus in enumerate(VALID_BUSES[1:]):
    while (timestamp+DIFFERENCES[i+1]) % bus != 0:
        timestamp += step
    step = lcm(step, bus)

print("The earliest timestamp is {}.".format(timestamp))
