# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:23:10 2020

@author: Marysia

Puzzle 1 part 1 from https://adventofcode.com/2020/day/1#part1

Calcuting the product of two numbers that add up to 2020.

Notes:
1. You do not have to check the last number; if there was a pair you would
   have already found it by then.
2. Notice that the membership check (which is quite costly in lists) is
   optimized since it considers the slice numbers[i+1:] only.
   The previous numbers have been checked already. A positive side-effect
   of the slicing is that the existence of one 4 in the list, does not give
   a pair for a target value of 8.
3. This is an excellent setup to explain the miss-understood and often
     confusing use of else in for-loops. The else triggers only if the loop
     was not abruptly ended by a break.
"""


TARGET_NUMBER = 2020

with open('numbers.txt', 'r') as file:
    NUMBERS = file.readlines()

NUMBERS = [int(x.strip()) for x in NUMBERS]

for i, number in enumerate(NUMBERS[:-1]):  # note 1
    complementary = TARGET_NUMBER - number
    if complementary in NUMBERS[i+1:]:  # note 2
        print("The numbers that add up to {} are: {} and {}.".format(TARGET_NUMBER,
                                                                     number, complementary))
        print("The product of these numbers is {}.".format(number*complementary))
        break
else:  # note 3
    print("No solutions exist")
