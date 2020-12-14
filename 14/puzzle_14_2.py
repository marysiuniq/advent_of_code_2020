# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:12:23 2020

@author: Marysia
Puzzle 14 part 1 from https://adventofcode.com/2020/day/14

A version 2 decoder chip doesn't modify the values being written at all. Instead,
it acts as a memory address decoder. Immediately before a value is written to memory,
each bit in the bitmask modifies the corresponding bit of the destination memory
address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably.
In practice, this means the floating bits will take on all possible values,
potentially causing many memory addresses to be written all at once!

Execute the initialization program using an emulator for a version 2 decoder chip.
What is the sum of all values left in memory after it completes?
"""

import re
import itertools

def dec_to_bin(number, size):
    '''
    Converts the decimal number to size-bit long binary number.
    '''
    number = bin(number)[2:]
    return '0' * (size - len(number)) + number

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

SIZE = 36
MEMORY = {}
for line in INPUT:
    if line[0:4] == 'mask':
        positions_1 = [x.start() for x in re.finditer('1', line[7:])]
        positions_X = [x.start() for x in re.finditer('X', line[7:])]
    else:
        str_end = line[4:].find(']') + 4
        address = line[4:str_end]
        value = int(line[str_end+4:])
        key = dec_to_bin(int(address), SIZE)
        for pos in positions_1:
            key = key[:pos] + '1' + key[pos+1:]
        X_values = [p for p in itertools.product([1, 0], repeat=len(positions_X))]
        for combination in X_values:
            for i, val in enumerate(combination):
                key = key[:positions_X[i]] + str(val) + key[positions_X[i]+1:]
            MEMORY[key] = value

SUM = 0
for value in MEMORY.values():
    SUM += value

print("The sum of all values left in memory is {}.".format(SUM))
