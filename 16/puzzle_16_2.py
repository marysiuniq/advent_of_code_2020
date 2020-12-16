# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 06:37:11 2020

@author: Marysia

Now that you've identified which tickets contain invalid values, discard those
tickets entirely. Use the remaining valid tickets to determine which field is which.
Using the valid ranges for each field, determine what order the fields appear
on the tickets.

Once you work out which field is which, look for the six fields on your ticket
that start with the word departure. What do you get if you multiply those six
values together?
"""

def read_rules(input_note):
    '''
    Read the rules for nubers in ticket's fields.
    Yes, it's terrible. But I don't care.
    '''
    list_of_valids = []
    fields_with_numbers = {}
    for line_num, line in enumerate(input_note):
        tmp = []
        if len(line) != 0:
            start = line.find(": ") + 2
            middle = line.find("-")
            end = line.find(" or ")
            field_name = line[:start-1]
            first_number = int(line[start:middle])
            last_number = int(line[middle+1:end])
            list_of_valids += list(range(first_number, last_number+1))
            tmp += list(range(first_number, last_number+1))
            line = line[end+4:]
            middle = line.find("-")
            first_number = int(line[:middle])
            last_number = int(line[middle+1:])
            list_of_valids += list(range(first_number, last_number+1))
            tmp += list(range(first_number, last_number+1))
            fields_with_numbers[field_name] = tmp
        else:
            return set(list_of_valids), line_num, fields_with_numbers

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

LIST_OF_VALIDS, START_LINE, FIELDS_WITH_NUMBERS = read_rules(INPUT)
START_LINE += 2

# Delete invalid tickets:
for i, row in reversed(list(enumerate(INPUT))):
    if ',' in row:
        numbers = [int(entry) for entry in row.split(',')]
        if bool(set(numbers).difference(LIST_OF_VALIDS)):
            INPUT.remove(INPUT[i])
    if '-' in row:
        YOUR_TICKETS = [int(_) for _ in INPUT[i+3].split(',')]
        INPUT[:i+6] = []
        break

entries = {k: [] for k in range(len(numbers))} # positions in tickets
tickets = {k: [] for k in range(len(numbers))} # columns

for row in INPUT:
    numbers = [int(entry) for entry in row.split(',')]
    for j, num in enumerate(numbers):
        tickets[j] += [num]

for tkey, tval in tickets.items():
    for field, field_vals in FIELDS_WITH_NUMBERS.items():
        if bool(set(tval).difference(set(field_vals))):
            continue
        entries[tkey] += [field]

i = 0
done = []
while i < (len(numbers)):
    if len(entries[i]) == 1 and i not in done:
        for k, val in entries.items():
            if k != i and entries[i][0] in val:
                entries[k].remove(entries[i][0])
        done += [i]
        i = 0
    else:
        i += 1

RESULT = 1
WORD = 'departure'
for k, v in entries.items():
    if WORD in v[0]:
        RESULT *= YOUR_TICKETS[k]

print(RESULT)
