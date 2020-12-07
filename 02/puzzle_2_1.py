# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:56:57 2020

@author: Marysia

Puzzle 2 part 1 from https://adventofcode.com/2020/day/2

Check how many passwords are valid according to their policies.
The password policy indicates the lowest and highest number of
times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least
1 time and at most 3 times.
"""

COUNT_VALID = 0

with open('passwords.txt', 'r') as file:
    PASSWORDS = file.readlines()

PASSWORDS = [x.strip() for x in PASSWORDS]

for line in PASSWORDS:
    end = line.find("-")
    minimum = int(line[0:end])
    second_end = line.find(" ")
    maximum = int(line[end+1:second_end])
    letter = line[second_end+1:second_end+2]
    occurrences = line.count(letter)-1
    if minimum <= occurrences <= maximum:
        COUNT_VALID += 1

print("The number of valid passwords is {}.".format(COUNT_VALID))
