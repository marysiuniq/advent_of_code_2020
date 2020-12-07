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

Conditions:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Count the number of valid passports - those that have all required fields and
valid values. Continue to treat cid as optional. In your batch file, how many
passports are valid?
"""

def check_conditions(string_to_check):
    """
    cheks if all the conditions for valid passport are met
    """
    string_to_check = string_to_check.split(' ')
    for entry in string_to_check:
        if 'byr:' in entry:
            if not(entry[4:].isnumeric() and 1920 <= int(entry[4:]) <= 2002):
                return 0
        if 'iyr:' in entry:
            if not(entry[4:].isnumeric() and 2010 <= int(entry[4:]) <= 2020):
                return 0
        if 'eyr:' in entry:
            if not(entry[4:].isnumeric() and 2020 <= int(entry[4:]) <= 2030):
                return 0
        if 'hgt:' in entry:
            if not(entry[-2:] == 'cm' or entry[-2:] == 'in'):
                return 0
            if entry[-2:] == 'cm':
                if not(entry[4:-2].isnumeric() and 150 <= int(entry[4:-2]) <= 193):
                    return 0
            if entry[-2:] == 'in':
                if not(entry[4:-2].isnumeric() and 59 <= int(entry[4:-2]) <= 76):
                    return 0
        if 'hcl:' in entry:
            #pattern = re.compile("[A-Za-z0-9]+")
            #pattern.fullmatch(entry) != None
            if not(entry[4] == '#' and len(entry) == 11 and entry[5:].isalnum()):
                return 0
        if 'ecl:' in entry:
            if not((entry[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                   and len(entry) == 7):
                return 0
        if 'pid:' in entry:
            if not(entry[4:].isnumeric() and len(entry) == 13):
                return 0
    return 1
    #re.search('asdf=5;(.*)123jasd', string_to_check)

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
        STRING_TO_CHECK += PASSPORTS[i] + ' '
        i += 1
    TEST = [_ in STRING_TO_CHECK for _ in KEYWORDS]
    print(STRING_TO_CHECK)
    if all(TEST):
        if check_conditions(STRING_TO_CHECK.strip()):
            print('ok')
            VALIDS += 1
    print(i)
    i += 1

print("The number of valid passports is {}.".format(VALIDS))
