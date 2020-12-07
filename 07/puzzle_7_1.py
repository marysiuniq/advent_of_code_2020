# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 05:57:23 2020

@author: Marysia

Puzzle 7 from https://adventofcode.com/2020/day/7

Part 1: How many bag colors can eventually contain at least one shiny gold bag?

failed. Not finished.
"""

"""
def check_if_bag(rules, bags, counter, target):
    '''
    Checks if a  given target is contained in bags.
    '''
    for i, line in enumerate(rules):
    if "shiny gold" in line:
        COUNT += 1
        POSITIONS += [i]
    return COUNT
"""

with open('test.txt', 'r') as file:
    RULES = file.readlines()
        
RULES = [x.strip() for x in RULES]
COUNT = 0
POSITIONS = []
BAGS = []
for i, line in enumerate(RULES):
    if "shiny gold" in line:
        COUNT += 1
        POSITIONS += [i]

for pos in POSITIONS:
    end = RULES[pos].find(' bags')
    if RULES[pos][:end] !=  "shiny gold":
        BAGS += [RULES[pos][:end]]
    else:
        COUNT -= 1

counter = [0, 0, 0, 0, 0]
positions = []
new_bags = []
for ind, bag in enumerate(BAGS):
    for i, line in enumerate(RULES):
        end = line.find(' bags')
        if bag in line:
            if line[:end] != bag:
                counter[ind] += 1
                positions += [i]
                new_bags += [line[0:end]]

counter2 = [0]* len(positions)
positions2 = []
new_bags2 = []
for ind, bag in enumerate(new_bags):
    for i, line in enumerate(RULES):
        end = line.find(' bags')
        if bag in line:
            if line[:end] != bag:
                counter2[ind] += 1
                positions2 += [i]
                new_bags2 += [line[0:end]]

'''  
for pos in positions:
    end = RULES[pos].find(' bags')
    if RULES[pos][:end] !=  bag:
        BAGS += [RULES[pos][:end]]
    else:
        COUNT -= 1
'''

