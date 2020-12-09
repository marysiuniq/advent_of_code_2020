# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:05:26 2020

@author: Marysia
Puzzle 9 part 1 from https://adventofcode.com/2020/day/9
The first step of attacking the weakness in the XMAS data is to find
the first number in the list (after the preamble) which is not the sum
of two of the 25 numbers before it. What is the first number that does
not have this property?

"""

def is_sum_of_two(lst, num):
    '''
    checks if there are any two numbers in the lst summing up to num
    '''
    for _ in lst:
        if num - _ in lst:
            return True
    return False


with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [int(x.strip()) for x in INPUT]

PREAMB_LENGTH = 25
i = PREAMB_LENGTH
while i < len(INPUT)+1:
    if is_sum_of_two(INPUT[i-PREAMB_LENGTH:i], INPUT[i]):
        i += 1
        continue
    break

print("The first number without the given property is {}.".format(INPUT[i]))
