# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:23:10 2020

@author: Marysia

Puzzle 1 part 1 from https://adventofcode.com/2020/day/1#part1

Calcuting the product of three numbers that add up to 2020.
"""


TARGET_NUMBER = 2020

with open('numbers.txt', 'r') as file:
    NUMBERS = file.readlines()

NUMBERS = [int(x.strip()) for x in NUMBERS]

for i, first_number in enumerate(NUMBERS[:-2]):  
    first_complementary = TARGET_NUMBER - first_number
    for j, second_number in enumerate(NUMBERS[:-1]):
        second_complementary = first_complementary - second_number
        if second_complementary in NUMBERS[i+1:]:  
            print("The numbers that add up to {} are: {}, {} and {}.".format(TARGET_NUMBER,
                                                                             first_number,
                                                                             second_number,
                                                                             second_complementary))
            print("The product of these numbers is {}.".format(first_number*second_number*second_complementary))
            break
