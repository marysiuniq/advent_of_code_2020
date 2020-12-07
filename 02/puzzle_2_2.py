# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:56:57 2020

@author: Marysia

Puzzle 2 part 2 from https://adventofcode.com/2020/day/2#part2

Check how many passwords are valid according to their policies.
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character,
and so on. (Be careful; Toboggan Corporate Policies have no concept
of "index zero"!) Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy
enforcement.
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
    string_to_check = line[second_end+4:]
    if bool(string_to_check[minimum-1] == letter) != bool(string_to_check[maximum-1] == letter):
        COUNT_VALID += 1

print("The number of valid passwords is {}.".format(COUNT_VALID))
