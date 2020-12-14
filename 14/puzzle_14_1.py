# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 05:59:37 2020

@author: Marysia
Puzzle 14 part 1 from https://adventofcode.com/2020/day/14

The initialization program (your puzzle input) can either update the bitmask or
write a value to memory. Values and memory addresses are both 36-bit unsigned
integers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11
would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most
significant bit (representing 2^35) on the left and the least significant bit
(2^0, that is, the 1s bit) on the right. The current bitmask is applied to values
immediately before they are written to memory: a 0 or 1 overwrites the corresponding
bit in the value, while an X leaves the bit in the value unchanged.

Execute the initialization program. What is the sum of all values left in memory
after it completes?
"""
import re

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
        positions_0 = [x.start() for x in re.finditer('0', line[7:])]
    else:
        str_end = line[4:].find(']') + 4
        address = line[4:str_end]
        value = dec_to_bin(int(line[str_end+4:]), SIZE)
        for pos in positions_0:
            value = value[:pos] + '0' + value[pos+1:]
        for pos in positions_1:
            value = value[:pos] + '1' + value[pos+1:]
        MEMORY[address] = value

SUM = 0
for value in MEMORY.values():
    SUM += int(value, 2)

print("The sum of all values left in memory is {}.".format(SUM))
