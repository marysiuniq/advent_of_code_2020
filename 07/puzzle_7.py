# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 05:57:23 2020

@author: tymofiy (only modified by Marysia)

Puzzle 7 from https://adventofcode.com/2020/day/7

Part 1: How many bag colors can eventually contain at least one shiny gold bag?
Part 2: How many individual bags are required inside your single shiny gold bag?
"""

from collections import defaultdict
import re

COLOR_CONTENTS = defaultdict(list)
COLOR_ANCESTORS = defaultdict(list)

for line in open('rules.txt').readlines():
    color, rest = line.split(' bags contain ')
    if rest == "no other bags.":
        continue
    bag_amounts = re.findall(r'(\d+) ([^\.,]+) bags?', rest)
    COLOR_CONTENTS[color] = bag_amounts
    for _, name in bag_amounts:
        COLOR_ANCESTORS[name].append(color)

# Part 1: in how many different bags we can put a shiny gold bag
STACK = ['shiny gold']
ANCESTORS = set()
while STACK:
    COLOR = STACK.pop(0)
    for ancestor in COLOR_ANCESTORS[COLOR]:
        ANCESTORS.add(ancestor)
        STACK.append(ancestor)

print(len(set(ANCESTORS)))

# Part 2: how many other bags fit in a shiny gold bag
def count_bags_inside(bag_color):
    '''
    Counts bags inside a bag of given color.
    '''
    contents = COLOR_CONTENTS[bag_color]
    return 1 + sum([int(n)*count_bags_inside(bag_color) for (n, bag_color) in contents])

print(count_bags_inside('shiny gold')-1)
