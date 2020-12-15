# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:44:01 2020

@author: Marysia
Puzzle 15 part 1 from https://adventofcode.com/2020/day/15

In this game, the players take turns saying numbers. They begin by taking turns
reading from a list of starting numbers (your puzzle input). Then, each turn
consists of considering the most recently spoken number:

- If that was the first time the number has been spoken, the current player says 0.
- Otherwise, the number had been spoken before; the current player announces how
many turns apart the number is from when it was previously spoken.

Here are a few more examples:

Given the starting numbers 1,3,2, the 2020th number spoken is 1.
Given the starting numbers 2,1,3, the 2020th number spoken is 10.
Given the starting numbers 1,2,3, the 2020th number spoken is 27.
Given the starting numbers 2,3,1, the 2020th number spoken is 78.
Given the starting numbers 3,2,1, the 2020th number spoken is 438.
Given the starting numbers 3,1,2, the 2020th number spoken is 1836.

Given your starting numbers, what will be the 2020th number spoken?
"""

def say_number(numbers):
    '''
    Computes the number to be said.
    '''
    for j in range(len(numbers[1:])):
        if numbers[j+1] == numbers[0]:
            return j+1
    return 0

#### Write here the puzzle input (in reversed order):
NUMBERS = [20, 19, 2, 7, 1, 6, 0]
LAST_ROUND = 2020
#NUMBERS = [6,3,0]
#NUMBERS = [3,1,2]
###

i = len(NUMBERS)
while i < LAST_ROUND:
    NUMBERS = [say_number(NUMBERS)] + NUMBERS
    i += 1

print("The {}th number is {}.".format(LAST_ROUND, NUMBERS[0]))
