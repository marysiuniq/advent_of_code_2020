# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 06:21:44 2020

@author: Marysia

Puzzle 4 part 1 from https://adventofcode.com/2020/day/4

Count the number of valid passports - those that have all required fields.
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Treat cid as optional. In your batch file, how many passports are valid?
"""

KEYWORDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
CID = 'cid:'

with open('pasports.txt', 'r') as file:
    PASSPORTS = file.readlines()

#empties = sum(line.isspace() for line in PASSPORTS)
#CHECK = [line.isspace() for line in PASSPORTS]
for i, line in enumerate(PASSPORTS):
    if line.isspace():
        PASSPORTS[i] = 'marysia'
PASSPORTS = [x.strip() for x in PASSPORTS]

i = 0
VALIDS = 0
while i < len(PASSPORTS):
    STRING_TO_CHECK = ''
    while i < len(PASSPORTS) and PASSPORTS[i] != 'marysia':
        STRING_TO_CHECK += PASSPORTS[i]
        i += 1
        print(i)
    TEST = [_ in STRING_TO_CHECK for _ in KEYWORDS]
    if all(TEST):
        print('ok')
        VALIDS += 1
    print(i)
    i += 1

print("The number of valid passports is {}.".format(VALIDS))
