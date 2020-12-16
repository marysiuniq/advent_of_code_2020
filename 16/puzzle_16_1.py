# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 05:56:53 2020

@author: Marysia
Puzzle 16 part 1 from https://adventofcode.com/2020/day/16

You collect the rules for ticket fields, the numbers on your ticket, and the
numbers on other nearby tickets for the same train service (via the airport
security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the
ticket and the valid ranges of values for each field. For example, a rule like
class: 1-3 or 5-7 means that one of the fields in every ticket is named class
and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are
both valid in this field, but 4 is not).
Start by determining which tickets are completely invalid; these are tickets that
contain values which aren't valid for any field. Ignore your ticket for now.
Adding together all of the invalid values produces your ticket scanning error
rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket
scanning error rate?
"""

def read_rules(input_note):
    '''
    Read the rules for nubers in ticket's fields.
    Yes, it's terrible. But I don't care.
    '''
    list_of_valids = []
    for line_num, line in enumerate(input_note):
        if len(line) != 0:
            start = line.find(": ") + 2
            middle = line.find("-")
            end = line.find(" or ")
            first_number = int(line[start:middle])
            last_number = int(line[middle+1:end])
            list_of_valids += list(range(first_number, last_number+1))
            line = line[end+4:]
            middle = line.find("-")
            first_number = int(line[:middle])
            last_number = int(line[middle+1:])
            list_of_valids += list(range(first_number, last_number+1))
        else:
            return set(list_of_valids), line_num
    
with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

LIST_OF_VALIDS, START_LINE = read_rules(INPUT)
START_LINE += 2

SUM = 0
for row in INPUT[START_LINE:]:
    if ',' in row:
        numbers = [int(entry) for entry in row.split(',')]
        for number in numbers:
            if not number in LIST_OF_VALIDS:
                SUM += number

print(SUM)
