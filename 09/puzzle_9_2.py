# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:05:26 2020

@author: Marysia
Puzzle 9 part 2 from https://adventofcode.com/2020/day/9

The final step in breaking the XMAS encryption relies on the invalid
number you just found: you must find a contiguous set of at least two
numbers in your list which sum to the invalid number from step 1.
To find the encryption weakness, add together the smallest and largest
number in this contiguous range; in test example, these are 15 and 47,
producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
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

NUMBER_FOUND = INPUT[i]

for ind in range(i):
    SUM = 0
    j = ind
    while SUM <= NUMBER_FOUND:
        SUM += INPUT[j]
        j += 1
        if SUM == NUMBER_FOUND:
            print("The smallest index is {}, and the highest is {}.".format(ind, j-1))
            break
    if SUM == NUMBER_FOUND:
        break

THE_LIST = list(INPUT[ind:j])
THE_LIST.sort()
print("The sum of the smallest and highest number from contiguous set is{}.".format(
        THE_LIST[0]+THE_LIST[-1]))
